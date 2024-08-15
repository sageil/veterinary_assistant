from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_openai import ChatOpenAI
import streamlit as st
from typing import Union, List, Tuple, Dict
from langchain_core.agents import AgentFinish
import json
from langchain_community.llms import Ollama
import uuid
diagnosticianllm = Ollama(model="openhermes:v2.5", base_url="http://host.docker.internal:11434", temperature=0.1)
reportinganalystllm = Ollama(model="gemma:latest", base_url="http://host.docker.internal:11434", temperature=0.30)

@CrewBase
class veterinaryAssistantCrew:
    """veterinaryAssistant crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    def step_callback(
            self,
            agent_output: Union[str, List[Tuple[Dict, str]], AgentFinish],
            agent_name,
            *args,
        ):
            with st.chat_message("AI"):
                # Try to parse the output if it is a JSON string
                if isinstance(agent_output, str):
                    try:
                        agent_output = json.loads(agent_output)
                    except json.JSONDecodeError:
                        pass

                if isinstance(agent_output, list) and all(
                    isinstance(item, tuple) for item in agent_output
                ):

                    for action, description in agent_output:
                        # Print attributes based on assumed structure
                        st.write(f"Agent Name: {agent_name}")
                        st.write(f"Tool used: {getattr(action, 'tool', 'Unknown')}")
                        st.write(f"Tool input: {getattr(action, 'tool_input', 'Unknown')}")
                        st.write(f"{getattr(action, 'log', 'Unknown')}")
                        with st.expander("Show observation"):
                            st.markdown(f"Observation\n\n{description}")

                # Check if the output is a dictionary as in the second case
                elif isinstance(agent_output, AgentFinish):
                    st.write(f"Agent Name: {agent_name}")
                    output = agent_output.return_values
                    st.write(f"I finished my task:\n{output['output']}")

                # Handle unexpected formats
                else:
                    st.write(type(agent_output))
                    st.write(agent_output)

    @agent
    def diagnostician(self) -> Agent:
        return Agent(
            config=self.agents_config["diagnostician"],
            verbose=True,
            llm=diagnosticianllm,
            allow_delegation=False,
            max_iter=5,
            step_callback=lambda step: self.step_callback(step, "Diagnostician"),   
            )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["reporting_analyst"], 
            verbose=True,
            llm=reportinganalystllm, 
            allow_delegation=False,
            max_iter=10,
            step_callback=lambda step: self.step_callback(step, "Reporting Analyst"),   
        )

    @task
    def research_task(self) -> Task:
        return Task(config=self.tasks_config["research_task"], agent=self.diagnostician())

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config["reporting_task"],
            agent=self.reporting_analyst(),
            output_file="./reports/"+str(uuid.uuid4())+".md",
        )

    @crew
    def crew(self) -> Crew:
        """Creates the veterinaryAssistant crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=2,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )


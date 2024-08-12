from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="mistral:latest", base_url="http://host.docker.internal:11434/v1", temperature= 0.7, max_tokens=2048
)


@CrewBase
class veterinaryAssistantCrew:
    """veterinaryAssistant crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def diagnostician(self) -> Agent:
        return Agent(
            config=self.agents_config["diagnostician"],
            verbose=True,
            llm=llm,
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["reporting_analyst"], verbose=True, llm=llm, allow_delegation=False,
        )

    @task
    def research_task(self) -> Task:
        return Task(config=self.tasks_config["research_task"], agent=self.diagnostician())

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config["reporting_task"],
            agent=self.reporting_analyst(),
            output_file="report.md",
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


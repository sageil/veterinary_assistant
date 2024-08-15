import streamlit as st
from veterinary_assistant.crew import veterinaryAssistantCrew


class VeterinaryAssistantWeb:
    def generate_diagnostic(self, topic):
        inputs = {
            "input": topic,
        }
        return veterinaryAssistantCrew().crew().kickoff(inputs=inputs)

    def render(self):
        st.title("Veterinary Assistant Diagnostic")
        self.sidebar()
        if "running" not in st.session_state:
            st.session_state["running"] = False
        if "topic" not in st.session_state:
            st.session_state["topic"] = ""
        if st.session_state["running"]:
                self.generate_diagnostic(st.session_state["topic"])
                st.session_state["running"] = False

    #) 
    def chat_actions(self):
            st.session_state["chat_history"].append(
            {"role": "user", "content": st.session_state["topic"]},
        )
    def sidebar(self):
        with st.sidebar:
            st.sidebar.info(
                """
                This is a veterinary assistant diagnostic tool that helps you get answers to your questions about pet care, health, and nutrition. 
                Just enter the topic of your question in the box below and press enter to get an answer.
                """
            )
            if "chat_history" not in st.session_state:
                st.session_state["chat_history"] = []
            messages = st.container(height=300)
            if prompt := st.chat_input("Ask away!", disabled=False, key="topic",on_submit=self.chat_actions):
                st.session_state["running"] = True
                for i in st.session_state["chat_history"]:
                    messages.chat_message("user").write(i["content"])

if __name__ == "__main__":
    st.set_page_config(
        page_title="Veterinary Assistant Diagnostic ", page_icon="📧"
    )
    VeterinaryAssistantWeb().render()

#!/usr/bin/env python
import sys, os
from veterinary_assistant.crew import veterinaryAssistantCrew
os.environ["OTEL_SDK_DISABLED"] = "true"

def run():
    """
    Run the crew.
    """
    inputs = {
        'input': input("Describe your pet species, age, medical history if any, and current condition\n"),
    }
    veterinaryAssistantCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "input": input("Describe your pet Animal Species, age, medical history if any and current condition: ")
    }
    try:
        veterinaryAssistantCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        veterinaryAssistantCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

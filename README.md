# Veterinary Assistant Crew

Welcome to the Veterinary Assistant Crew project, powered by [crewAI](https://crewai.com) and [crewAI docker image](https://github.com/sageil/crewai-docker-image). This repository is dedicated to creating an ***experimental***, comprehensive Veterinary Assistant application that leverages artificial intelligence for efficient and accurate medical consultations.

## Project Overview
The Veterinary Assistant Crew project aims to develop an AI-powered veterinary assistant capable of providing insights, diagnoses, treatment plans, and prescriptions based on symptoms provided by pet owners. The system will utilize advanced machine learning algorithms and natural language processing to assist veterinarians in making informed decisions.

The project utilizes my [sageil/crewai-docker-image](https://github.com/sageil/crewai-docker-image) crewAI development Docker image. You can build the image locally or pull it from [Docker Hub](https://hub.docker.com/r/sageil/crewai/tags) to get started quickly.

## Running the Application

### Option 1: Using a docker mount locally 

> [!NOTE]  
> In its current state, this project depends on locally running LLMS using Ollama.<br/>
> install (Ollama)[https://ollama.com/].<br/>
> Once Ollama installed, install ollama run openhermes:v2.5 and  by running `ollama run openhermes:v2.5` and `ollama run gemma:latest` from your terminal.<br/>
> See changing models below to use other models<br/>

To run the application your machine, follow these steps:
1. Install Docker on your machine if you haven't already.
2. Install Ollama
2. Clone this repository to your local machine.
3. Run the following command to start the container
```bash
docker container run -e P="veterinary_assistant" --network host -it --rm --mount type=bind,source="$(pwd)",target=/app sageil/crewai:latest bash
```
4. Run `poetry install`
5. Run `poetry shell`
6. Edit the project files using your favourite IDE or editor.
7. To use the terminal, run the application using `poetry run veterinary_assistant` or if you prefer to use the web interface, run `streamlit run web/app.py`
8. Access the crew using http://localhost:8501/

### Option 2: Running the application in Docker

1. Start a container using 
```bash
docker container run --name veterinary_assistance --network host -it sageil/crewai:latest bash
```
2. Once the container starts, navivate to the `/app/` directory `cd /app/` 
3. Close the repository `git clone https://github.com/sageil/veterinary_assistant.git`
4. Change directory to `veterinary_assistant` directory 
5. Run `poetry install`
6. Run `poetry shell`
7. To use the terminal, run the application using `poetry run veterinary_assistant` or if you prefer to use the web interface, run `streamlit run web/app.py`
8. Access the crew using http://localhost:8501/
9. Use the included neovim installation to edit the project by typing `nvim .` in the project directory

## Changing currently used models

> [!CAUTION]
> Using local large models will have a performance impact.
> If you observe performance issues, change to a smaller model like `phi3:3.8b`

To change the model used by the agents, you need to update the `model` parameter in the `crew.py` file located at `veterinary_assistant/src/veterinary_assistant`.
```python
diagnosticianllm = Ollama(model="openhermes:v2.5", base_url="http://host.docker.internal:11434", temperature=0.1)
reportinganalystllm = Ollama(model="gemma:latest", base_url="http://host.docker.internal:11434", temperature=0.30)
```
## Using publicly available LLMs.
If you want to use publicly available models, please use the following steps;

1. Change the model property to match the desired LLM.
2. import model's langchain_openai implementation.

To use ChatGPT, import it using `from langchain_openai import ChatOpenAI` then use it to configure the LLMs using the following:
```bash
# GPT based LLMS
diagnosticianllm = ChatOpenAI(
    model="gpt-40",  temperature= 0.1)
reportinganalystllm== ChatOpenAI(
    model="gpt-4-turbo",  temperature= 0.30)
```
3. Include your `OPENAI_API_KEY` in the .env file in the root of the project.  
### Example 
The `reports` directory contains a few answers provided by my locally installed agents
[Reports](https://github.com/sageil/veterinary_assistant/tree/main/reports).

## Docker Desktop Users

Enabling host network on Docker Desktop is required to run this project locally. 
while the feature is ready for Linux, it is in beta on Windows and Mac. [Read more](https://docs.docker.com/engine/network/tutorials/host/).

### Having issues?
[Report any issues](https://github.com/sageil/veterinary_assistant/issues)
### Screen Capture

![Browser](assets/Veterinary-Assistant-Diagnostic.png)

### TODO
- [X] Recreate report.md using the prompt
- [X] Create GUI for user interaction using [streamlit](https://streamlit.io/)
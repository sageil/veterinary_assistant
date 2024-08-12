# Veterinary Assistant Crew

Welcome to the Veterinary Assistant Crew project, powered by [crewAI](https://crewai.com) and [crewAI docker image](https://github.com/sageil/crewai-docker-image). This repository is dedicated to creating an ***experimental***, comprehensive Veterinary Assistant application that leverages artificial intelligence for efficient and accurate medical consultations.

## Project Overview
The Veterinary Assistant Crew project aims to develop an AI-powered veterinary assistant capable of providing insights, diagnoses, treatment plans, and prescriptions based on symptoms provided by pet owners. The system will utilize advanced machine learning algorithms and natural language processing to assist veterinarians in making informed decisions.

The project utilizes my [sageil/crewai-docker-image](https://github.com/sageil/crewai-docker-image) crewAI development Docker image. You can build the image locally or download it from [Docker Hub](https://hub.docker.com/r/sageil/crewai/tags)

## Running the Application

### Option 1: Using a docker mount locally 

> [!NOTE]  
> In its current state, this project depends on locally running LLMS using Ollama.<br/>
> install (Ollama)[https://ollama.com/] and run it on your local machine.<br/>
> Once Ollama installed, install mistral by running `ollama run mistral` from your terminal.<br/>
> See changing models below to use other models<br/>

To run the application your machine, follow these steps:
1. Clone this repository to your local machine.
2. Install Docker on your machine if you haven't already.
5. Navigate to the ***parent*** directory of where you cloned the repository. project directory in your terminal or command prompt.

> [!IMPORTANT]  
> If you run the container in any directory besides the parent directory of where you cloned the repository, a new crewAi project with the name `veterinary_assistant` will be created.

6. Run the following command to start the container
```bash
docker container run -e P="veterinary_assistant" --network host -it --rm --mount type=bind,source="$(pwd)",target=/app sageil/crewai:latest bash
```
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
7. Run `source .venv/bin/activate` to activate the project python environment
8. Run the application using `poetry run veterinary_assistant`

## Changing model to another one

> [!CAUTION]
> Using large models will have a performance impact.
> If you observe performance issues, change to a smaller model like `phi3:3.8b`

To change the model used by the agents, you need to update the `model` parameter in the `crew.py` file located at `veterinary_assistant/src/veterinary_assistant`. You can also change the temperature and max_token:
```python
llm = ChatOpenAI(
    model="mistral:latest", base_url="http://host.docker.internal:11434/v1", temperature= 0.7, max_tokens=2048
)
```

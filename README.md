# valPDB-Agent

A LangChain-based agent for protein structure evaluation.
The agent uses large language models to orchestrate protein analysis tools,
supports local Ollama models, and runs in a Docker-based sandbox.

The system provides an interactive command-line interface for protein
structure assessment (for example, Ramachandran plot generation).


# Usage

## 1. Build the Docker image

```bash
docker pull swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/continuumio/anaconda3:latest
docker tag  swr.cn-north-4.myhuaweicloud.com/ddn-k8s/docker.io/continuumio/anaconda3:latest  docker.io/continuumio/anaconda3:latest
```

```bash
docker build -t protein-agent:latest .
```

## 2. Prepare environment variables

Create a `.env` file in the project root, for example:

```env
LLM_PROVIDER=ollama
LLM_MODEL=modelscope.cn/Qwen/Qwen3-4B-GGUF:latest
LLM_BASE_URL=http://<host-ip>:11434
LLM_API_KEY=dummy
```

Note:  
If Ollama is running on the host machine, `LLM_BASE_URL` must point to a
host-accessible address. Do not use `localhost` inside the container.

## 3. Run the agent (interactive mode)

```bash
docker run -it \
  --network=host \
  --env-file .env \
  -v /your/data/path:/data \
  --name protein-agent \
  protein-agent:latest
```

The agent will start in interactive mode.
If required information (such as file paths or output locations) is missing,
the agent will ask for clarification before executing any tool.

## 4. Retrieve outputs

To copy results from the container to the host:

```bash
docker cp protein-agent:/app/output ./output
```

This workflow does not require mounting any host directories.

## 5. Cleanup

```bash
docker rm -f protein-agent
```

# Status

This project is under active development.
Additional protein evaluation and generation capabilities will be added.

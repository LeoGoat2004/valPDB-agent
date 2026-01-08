FROM condaforge/mambaforge:24.1.2-0

WORKDIR /app

COPY environment.yml /app/environment.yml
RUN mamba env create -f /app/environment.yml \
    && conda clean -afy

SHELL ["bash", "-lc"]
ENV CONDA_DEFAULT_ENV=protein-agent
ENV PATH=/opt/conda/envs/protein-agent/bin:$PATH

COPY src /app/src

RUN mkdir -p /app/output

CMD ["python", "-m", "src.agent.run_agent"]
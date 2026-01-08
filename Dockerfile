FROM docker.io/continuumio/anaconda3:latest

WORKDIR /app

# Switch conda channels to China mirrors
RUN conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main \
    && conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r \
    && conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge \
    && conda config --set show_channel_urls yes

# Copy environment definition
COPY environment.yml /app/environment.yml

# Create conda environment
RUN conda env create -f /app/environment.yml \
    && conda clean -afy

# Activate environment
SHELL ["bash", "-lc"]
ENV CONDA_DEFAULT_ENV=protein-agent
ENV PATH=/opt/conda/envs/protein-agent/bin:$PATH

# Copy project source
COPY src /app/src

# Prepare output directory
RUN mkdir -p /app/output

# Default command
CMD ["python", "-m", "src.agent.run_agent"]

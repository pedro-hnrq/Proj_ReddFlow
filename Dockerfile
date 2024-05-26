FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1
ENV DJANGO_ENV=dev
ENV DOCKER_CONTAINER=1

RUN apt-get update && \
         apt-get install -y --no-install-recommends \
         gcc \
         libpq-dev \
         && rm -rf /var/lib/apt/lists/*

# Cria o diretório de trabalho dentro do contêiner
RUN mkdir /app
WORKDIR /app

# Exponha a porta 8000 para acesso externo
EXPOSE 8000

# Copie o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instale as dependências do projeto
RUN pip install -U pip && pip install -r requirements.txt

# Copie todos os arquivos do projeto para o contêiner
COPY . .


CMD ["python3", "manage.py", "runserver"]

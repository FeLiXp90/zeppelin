FROM python:3.10-slim-bullseye

# Variáveis de ambiente
ENV DJANGO_SETTINGS_MODULE=zeppelin.settings.local
#ENV PYTHONPATH=/app
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV DEBUG=true

# Define o diretório de trabalho
WORKDIR /app

# Copia tudo do projeto (raiz, onde está o docker-compose.yml)
COPY ./src/ .

# Instala dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    netcat \
    gcc \
    libpq-dev \
    libffi-dev \
    musl-dev \
    python3-dev \
    supervisor \
    && rm -rf /var/lib/apt/lists/*

# Instala dependências Python
#RUN pip install flower
RUN pip install -r requirements.txt

RUN python manage.py collectstatic --noinput --no-post-process
RUN mkdir -p /app/logs

COPY supervisord.conf /etc/supervisord.conf

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

CMD ["supervisord", "-c", "/etc/supervisord.conf"]
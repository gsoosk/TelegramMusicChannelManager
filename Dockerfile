FROM python:3.5-jessie
WORKDIR /app
COPY config.json /app/config.json
COPY main.py /app/main.py
RUN pip install python-telegram-bot
RUN pip install mutagen


CMD ["python", "./main.py"]

FROM python:3.10

RUN apt-get update && \
    apt-get install -y ffmpeg

WORKDIR /usr/src/app

RUN pip3 install --no-cache-dir python-osc pandas openai-whisper requests sshtunnel

COPY . .

EXPOSE 80

ENV NAME world

CMD ["python", "main.py"]

FROM python:3.10


WORKDIR /usr/src/app

RUN pip3 install --no-cache-dir python-osc tensorflow tensorflow-io-gcs-filesystem pandas tensorflow-datasets

COPY . .

EXPOSE 80

ENV NAME World

CMD ["python", "main.py"]

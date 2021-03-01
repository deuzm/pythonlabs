FROM python:3

WORKDIR /usr/src/app

ADD ./requirements.txt /usr/src/app/requirements.txt

RUN set -ex \
    \
    pip install --no-cache-dir -r requirements.txt \
    && rm /usr/src/app/requirements.txt

COPY main.py .

ENTRYPOINT ["python", "./main.py"]

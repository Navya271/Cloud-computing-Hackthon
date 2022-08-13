# Follow Task-0 subtask-1

FROM python:3.8-alpine

WORKDIR /app

COPY . /app

COPY ./requirements.txt /app/requirements.txt

RUN apk add --update  && pip install --upgrade pip  && pip install -r requirements.txt  && rm -rf /var/cache/apk/*

CMD ["python","lcm.py"]
FROM python:3.12-alpine

COPY ./codmart/ codmart/

RUN apk add postgresql-dev curl

COPY ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "codmart/manage.py", "runserver", "0.0.0.0:8000"]
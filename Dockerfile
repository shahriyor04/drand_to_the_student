FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/
COPY . /code/

RUN pip install -r req.txt

CMD ["python", "manage.py", "runserver"]

#FROM postgres:latest
#
#WORKDIR /code/
#COPY . /code//
#ENV POSTGRES_DB=grand_student
#ENV POSTGRES_USER=myuser
#ENV POSTGRES_PASSWORD=mypassword
#
## Install PostgreSQL client tools
#RUN apt-get update && apt-get install -y postgresql-client

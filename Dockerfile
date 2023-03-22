FROM python:3.10.10-slim-buster

# set work directory
WORKDIR /usr/src/app

# install dependencies
RUN pip install --upgrade pip

COPY ./requirements.txt /usr/src/app

RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app

EXPOSE 8001
# run application

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]

# pull the official base image
FROM python:3.11.2-alpine3.17
 
# set work directory
WORKDIR /usr/src/app
 
# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt
 
# copy project
COPY . /usr/src/app
 
# build up application
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
 
EXPOSE 8002
 
# run application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]
FROM python:3

# set a directory for the app
WORKDIR /app

# copy all the files to the container
COPY . .

RUN apt-get update 

# port number
EXPOSE 80


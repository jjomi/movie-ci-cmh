FROM python:3

# set a directory for the app
WORKDIR /app

# copy all the files to the container
COPY . .

RUN apt-get update 
RUN pip install flask flask_restx

# port number
EXPOSE 80

# run command
CMD ["python", "source/app.py"]

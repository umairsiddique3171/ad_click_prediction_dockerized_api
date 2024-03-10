# setting up the container with python 3.10
FROM python:3.10-slim

# copying everything to the /app directory in the container
COPY . /app

# changing working directory
WORKDIR /app

# installing the dependencies
RUN pip install -r requirements.txt

# exposing port 80 of the container
EXPOSE 80

# command to run
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","80"]







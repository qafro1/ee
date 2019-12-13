# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:alpine3.7

# Copy local code to the container image.
COPY . /app
WORKDIR /app

# Install required dependencies.
RUN pip install -r requirements.txt

#expose the port 5000
EXPOSE 5000

#run the command
CMD python ./helloworld.py


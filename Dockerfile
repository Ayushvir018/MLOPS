#PULL the python image from docker hub
#Use a light weigt Python image
FROM python:3.9-slim

#set the working directry inside container
WORKDIR /app

#Copy the requirements file into the container before application code
COPY requirement.txt .
# install the dependencies
RUN pip install -r requirement.txt

#Copy the application code into the container and save mode inseide app directory
COPY . .

#Expose the port on which the application will run(8000 pe hi chl rha tha backend in main.py)
EXPOSE 8000

#Start the api server when container is ready to run the application
#0.0.0.0 - allow access from any IP address, 8000 - port number
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
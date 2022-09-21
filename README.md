# Mini Project--Docker Container
## 1. Business Scenario
Create a docker container for data process.

## 2. Business Requirements
- The python script is in the container
- The **input** and **output** folder is in the host, in another word, outside the container
- Mount the 2 folders from host to the container

## 3. Specification Detail
1. Create an image to generate a Docker container, and in the container:
- Use a python script to read the data from **input** folder
- The data will be appended to a csv file named all_years.csv
- Write the result data into **output** folder

## 2. Make the container run first, and then run python script to permit troubleshooting the container. 
- This means when docker run us executed to start up the container, the python script will not run. 
- The python script only runs when you give the container an order using the docker exec command

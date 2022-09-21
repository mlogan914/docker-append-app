# Mini Project -- Docker Container
## 1. Business Scenario
Create a docker container for data process.

## 2. Business Requirements
- The python script is in the container
- The **input** and **output** folder is in the host, in another word, outside the container
- Mount the 2 folders from host to the container
- All scripts, data and final csv file is pushed to this Github repository using shell commands.

## 3. Specification Detail
1. Construct a dockerfile to create an image to generate a Docker container, and in the container:
- Use a python script to read the data **t1.csv** and **t2.csv** from **input** folder
- The data will be appended to a csv file named **all_years.csv**
- Write the result data into the **output** folder

2. Make the container run first, then run the python script to permit troubleshooting the container
- This means when _docker run_ is executed to start up the container, the python script will not run
- You will need to make the container remain active until the python scrytp is manually executed
- The python script only runs when you give the container the order using the docker _docker exec_ command

## Project Diagram:
![Docker_lab_Process](https://user-images.githubusercontent.com/74939090/191591390-3b93c7b8-a7c2-4dce-8f61-049a65102652.jpg)

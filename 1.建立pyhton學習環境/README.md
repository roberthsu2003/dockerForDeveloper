### 建立pyhton學習環境

- Dockerfile
  
```Dockerfile

FROM python:3.10-slim

# set the working directory
WORKDIR /code

# install dependencies
COPY ./requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# copy the src to the folder

# start the server
CMD ["tail", "-f", "/dev/null"]

```

###  建立docker Image

    docker build -t python-learning-image:v01 .

1.查看docker images
	
	docker images

1.查看docker images

	docker image ls
	
2.刪除docker images

	docker image rm python-learning-image:v01
	
### 建立docker container

	docker run --name python-learning-container -it -d python-learning-image:v01 
	
1.查詢目前running的container

	docker ps
	
1.查詢目前running的container

	docker container ls
	
2.查詢目前所有的container

	docker ps -a
	
3.停止conatiner

	docker container stop python-learning-container
	
4.啟動container

	docker container start python-learning-container
	
5.刪除container

	docker container rm python-learning-container

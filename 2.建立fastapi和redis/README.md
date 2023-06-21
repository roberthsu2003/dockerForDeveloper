### 工作區建立

- 建立一個requirements.txt

```
fastapi
uvicorn
redis
```

### 建立pyhton學習環境

- 建立Dockerfile
  
```Dockerfile

FROM python:3.10-slim

WORKDIR /code

COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]

```

###  建立docker Image

    docker build -t fastapi-image .

1.查看docker images
	
	docker images

1.查看docker images

	docker image ls
	
2.刪除docker images

	docker image rm fastapi-image
	
### 建立docker container

	docker run --name fastapi-container  -p 80:80  fastapi-image
	
-背景執行

	docker run --name fastapi-container  -d -p 80:80  fastapi-image
	
	
1.查詢目前running的container

	docker ps
	
1.查詢目前running的container

	docker container ls
	
2.查詢目前所有的container

	docker ps -a
	
3.停止conatiner

	docker container stop fastapi-container
	
4.啟動container

	docker container start fastapi-container
	
5.刪除container

	docker container rm fastapi-container
	
### 建立docker container 並同時使用volumes

	docker run --name fastapi-container -p 80:80 -d -v $(pwd):/code fastapi-images	

### 使用vscode 連結至正在執行的容器

- 安裝 python extension


### 使用docker compose建立volumes



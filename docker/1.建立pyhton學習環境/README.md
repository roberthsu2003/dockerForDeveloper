### 1. 工作區建立
- 建立一個空的requirements.txt

### 2. 建立pyhton學習環境

- Dockerfile
  
```Dockerfile

FROM python:3.10-slim

# set the working directory
WORKDIR /code

# install dependencies
COPY ./requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt



# start the server
CMD ["tail", "-f", "/dev/null"]

```

###  3. 建立docker Image

    docker build -t python-learning-image:v01 .

1.查看docker images
	
	docker images

1.查看docker images

	docker image ls
	
2.刪除docker images

	docker image rm python-learning-image:v01
	
### 4. 建立docker container(沒有建立Volumns)

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
	
### 4. 建立docker container 並同時使用volumes和開啟ssh port

	docker run --name python-learning-container -itd -v $(pwd):/code -p 2200:22 python-learning-image 
	
### 5. 執行container的shell
#### 5.1 方法1 利用vscode 擴充套件docker,找到container,按右鍵並選擇使用attach shell
#### 5.2 方法2 

```bash
docker exec -it container名稱 /bin/bash
```

### 6.在container安裝openssh-server
[參考影片](https://youtu.be/GicWz2OF0sk?si=siBDADg6V9xPxeLv)

## Dockerfile建立python學習環境,並且同時安裝git,openssh-server
 - ssh連線,user=root
 - ssh連線,password=root

### 7.1 Dockerfile

```dockerfile
FROM python:3.12.4-bookworm

WORKDIR /code

COPY ./requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN apt-get update && apt-get upgrade\
    && apt-get install -y git-all
RUN git config --global user.name "robertHsu"
RUN git config --global user.email "roberthsu2003@gmail.com"
RUN git config --global init.defaultBranch main
RUN git init

RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd

RUN echo 'root:root' | chpasswd

RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
```

### 7.2 建立image:python_env

```bash
docker build -t python_env .
```

### 7.3 建立docker container 並同時使用volumes和開啟ssh port

```bash
docker run --name python_env_container -itd -v $(pwd):/code -p 2200:22 python_env 
```

### 7.4 查看container執行時,是否有出錯

```bash
docker logs python_env_container
```

### 7.5 ssh連線至container

```
ssh root@127.0.0.1 -p 2200
```

## 使用docker compose建立volumes

```
version: "3.8"
services:
  app:
    build: .
    container_name: python-server
    volumes:
      - .:/code
```

##### 啟動docker-compose

```
docker-compose up
```
	

##### 關閉docker-compose
- container會被清除

```
Docker-compose down
```

### 清理docker

	docker system prune

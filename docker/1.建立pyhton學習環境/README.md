# 開發環境建立

# Docker安裝python_conda_git開發環境
- 電腦必需有安裝Docker Desktop

## 方法1:使用Docker Hub Repository
- 使用以下的repository

`continuumio/miniconda3`

### 步驟1 **下載repository**

```
docker pull continuumio/miniconda3
```

### 步驟2 **建立容器**
- 請不要直接使用Docker Desktop直接啟動(因為容器啟動後會直接關閉)
- 使用以下指令,建立容器,並且要求可互動,和配置一個偽TTY(容器啟動後不會自動關閉)

```bash
docker run -it --name python-miniconda continuumio/miniconda3

#-it 要求可互動,和配置一個偽TTY
#--name python-miniconda 建立容器名稱
#continuumio/miniconda3 映像名稱(一定在最後面)
```

### 步驟3 **使用VSCode Docker容器開發工具**
### 步驟4 **下載github專案**
### 步驟5 **安裝VSCode套件**
- python
- jupyter
### 步驟6 **安裝python外部套件**

## 方法2.手動建立

### 1. 建立環境變數

**1.1 mac建立環境變數**

```bash
#檢查所有環境變數
$ env

#檢查單1個環境變數
$ echo $HOME

#建立環境變數
$ export REPO_NAME=<repo名稱>
$ export REPO_PATH=${HOME}/Documents/GitHub/<repo名稱>
```

**1.2 windows cmd 建立環境變數**

```
#檢查所有環境變數
$ set

#檢查單1個環境變數

$ echo %VARIABLE_NAME%

#建立環境變數
$ set REPO_NAZME=<repo名稱>
$ set REPO_PATH=%USERPROFILE%\Documents\GitHub\%REPO_NAME%
```

### 2. 建立pyhton學習環境Dockerfile

- Dockerfile
  
```Dockerfile
FROM python:3.11.10-bookworm

#定義常數
ARG REPO_NAME

# set the working directory
WORKDIR /root/${REPO_NAME}


# start the server
CMD ["tail", "-f", "/dev/null"]
```

### 3. 建立docker Image

```bash
$ docker build --build-arg REPO_NAME=${REPO_NAME} -t host<dockerHub_USER_NAME>/<image_名稱>:v01 .
```

- **3.1 看docker image**

```bash
 docker images
```

- **3.2 查看docker image**

```bash
docker image ls
```

- **3.3 刪除docker image**

```bash
docker image rm python-learning-image:v01
```

- **3.4 上傳docker image**

  - **注意,如果要上傳到docker hub,建立的image必需前面包含github帳號**

```bash
docker push <您的docker hub 帳號>/<image name>
```

### 4. 建立docker container(沒有建立Volumns)

```bash
 docker run --name <container名稱> -itd <docker_hup user_name>/<images名稱>
```

### 4. 建立docker container 並同時使用volumes和開啟ssh port
- **使用$(command name)**

```bash
docker run --name <container名稱> -itd -v $(pwd):/code -p 2200:22 <docker_hup user_name>/<images名稱>
```

### 4. 建立docker container 並同時使用volumes和開啟ssh port
- **使用${環境變數名稱}**

```bash
docker run --name <container名稱> -itd -v $(pwd):/code -p 2200:22 <docker_hup user_name>/<images名稱>
```



- **4.1 查詢目前running的container**

```bash
docker ps
```

- **4.2 查詢目前running的container**

```bash
docker container ls
```

- **4.3 查詢目前所有的container**

```bash
docker ps -a
```

- **4.4 停止conatiner**

```bash
docker container stop python-learning-container
```

- **4.5 啟動container**

```bash
docker container start python-learning-container
```

- **4.6 刪除container**

```bash
docker container rm python-learning-container
```

### 5. 建立docker container 並同時使用volumes和開啟ssh port

```bash
docker run --name python-learning-container -itd -v $(pwd):/code -p 2200:22 python-learning-image
```

### 6. 執行container的shell

- **6.1 方法1 利用vscode 擴充套件docker,找到container,按右鍵並選擇使用attach shell**

- **6.2 方法2**

```bash
docker exec -it container名稱 /bin/bash
```

### 7. 在container安裝openssh-server

[參考影片](https://youtu.be/GicWz2OF0sk?si=siBDADg6V9xPxeLv)

### 8. 實際案例
### 8.1 建立python學習環境,同時安裝miniconda,git,並且使用下載的REPO資料夾

```bash
export REPO_NAME=LLMs-API
echo $REPO_NAME
```

## 建立Docker file

```bash
docker build --build-arg REPO_NAME=${REPO_NAME} -t roberthsu2003/llms-api:v01
```


## 建立Container

```bash
docker run --name llms-api -itd -v $(pwd):/root/${REPO_NAME} roberthsu2003/llms-api:v01
```


## 方法3 Dockerfile建立python學習環境,並且同時安裝git,openssh-server

- ssh連線,user=root
- ssh連線,password=root

### 1 Dockerfile

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

### 2 建立image:python_env

```bash
docker build -t python_env .
```

### 3 建立docker container 並同時使用volumes和開啟ssh port

```bash
docker run --name python_env_container -itd -v $(pwd):/code -p 2200:22 python_env 
```

### 4 查看container執行時,是否有出錯

```bash
docker logs python_env_container
```

### 5 ssh連線至container

```bash
ssh root@127.0.0.1 -p 2200
```


# 簡單的Docker file範例
- 依據lessons資料夾

## 範例1-透過Docker_Hub下載python開發環境
- 直接使用Docker_Hub內python官方網站的python image

**使用docker pull 下載docker image**

```bash
docker pull python:3.11-slim
```

**檢查python:3.11-slim是否被下載至docker cache images

```bash
docker images
```

**進入01-starter-code目錄,使用pwd查詢目錄的絕對路徑

```bash
pwd
#=====output=====
/home/pi/Documents/lessons/01-starter-code
```

**使用docker run建立container**
- docker container被建立並執行,執行完成後就關閉
- 使用docker container自動建立的container名稱

```bash
docker run -v "/home/pi/Documents/lessons/01-starter-code:/src/app" \
python:3.11-slim \
python /src/app/python-app.py

#=====output=======
  ____        _   _                  _
   |  _ \ _   _| |_| |__   ___  _ __  / \
   | |_) | | | | __| '_ \ / _ \| '_ \/  /
   |  __/| |_| | |_| | | | (_) | | | /\_/
   |_|    \__, |\__|_| |_|\___/|_| |_(_)
          |___/

             -- Python --
```

![](./images/pic1.png)

**檢查docker container**

```bash
docker container -a

#====output========
CONTAINER ID   IMAGE                                COMMAND                  CREATED              STATUS                          PORTS     NAMES
6f7ac971ed54   python:3.11-slim                     "python /src/app/pyt…"   About a minute ago   Exited (0) About a minute ago             interesting_shaw
```

**使用container ID刪除container**

```bash
docker rm 6f7ac971ed54
```

**刪除docker image**

```bash
docker image rm python:3.11-slim
```

## 範例2-使用Dockerfile擴充docker image的功能
- 擴充那一個base image(FROM)
- 設定工作目錄(WORKDIR)
- 複制檔案至工作目錄(COPY)
- 應用程式執行(CMD)

**建立Dockerfile**

```bash
## 1. Which base image do you want to use?
FROM python:3.11-slim

## 2. Set the working directory inside the container.
WORKDIR /src/app

## 3. Copy your source code file to the working directory inside the container.
COPY ./python-app.py .

## 4. Define the command to run when the container starts.
CMD ["python", "/src/app/python-app.py"]
```

**使用docker build建立docker image**

```bash
docker build -t flask-application:0.0.1 .
```

**建立docker image**

```bash
docker images

#======output========
REPOSITORY                      TAG         IMAGE ID       CREATED              SIZE
flask-application               0.0.1       c4e1daaa874c   About a minute ago   155MB
```

**建立container**

```bash
docker run flask-application:0.0.1

#==========output==============
    ____        _   _                  _
   |  _ \ _   _| |_| |__   ___  _ __  / \
   | |_) | | | | __| '_ \ / _ \| '_ \/  /
   |  __/| |_| | |_| | | | (_) | | | /\_/
   |_|    \__, |\__|_| |_|\___/|_| |_(_)
          |___/

             -- Python --
```




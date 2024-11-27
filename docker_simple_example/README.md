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


## 範例3:Dockerfile增加Dependencies

![](./images/pic2.png)

- WORKDIR設定完成後,後面的路徑就以此為根目錄
- RUN是安裝系統需要的套件
- CMD是代表container建立後,要執行的指令

**建立Dockerfile**

```bash
## 1. Which base image do you want to use?
FROM python:3.11-slim

## 2. Set the working directory in the container.
WORKDIR "/src/app/"

## 3. Copy the project files into the working directory.
COPY . .

## 4. Install the dependencies
RUN pip install -r flask-demo/requirements.txt

## 5. Document and inform the developer that the application will use PORT 5000 of the container.
EXPOST 5000

## 6. Define the command to run when the conta/iner starts.
CMD ["python", "flask-demo/app.py"]
```

**建立docker image**

```bash
docker build -t flask-demo:0.0.1 .
```

**使用docker inspect 檢查docker images**

```bash
docker images
#=======output=====
REPOSITORY                      TAG         IMAGE ID       CREATED         SIZE
flask-demo                      0.0.1       e125d92c883a   3 minutes ago   172MB
```

```bash
docker inspect e125d92c883a

#檢查ContainerConfig,查expose port
```

**建立docker container**

```bash
docker run -p 5000:5000 flask-demo:0.0.1
```

**測試連線**
![](./images/pic3.png)

**檢查docker container**

```bash
docker ps

#=======output=====
CONTAINER ID   IMAGE                                COMMAND                  CREATED         STATUS                 PORTS                                       NAMES
2d5da4bef308   flask-demo:0.0.1                     "python flask-demo/a…"   5 minutes ago   Up 5 minutes           0.0.0.0:5000->5000/tcp, :::5000->5000/tcp   awesome_elbakyan
85bfdf0b0ef4   ghcr.io/open-webui/open-webui:main   "bash start.sh"          6 weeks ago     Up 2 weeks (healthy)                                               open-webui
```

**停止docker container**

```bash
docker container stop 2d5da4bef308
```

**刪除docker container**

```bash
docker rm 2d5da4bef308
```

**刪除docker image**

```bash
docker images

#=====output=========
REPOSITORY                      TAG         IMAGE ID       CREATED          SIZE
flask-demo                      0.0.1       e125d92c883a   21 minutes ago   172MB
```

```bash
docker image rm flask-demo:0.0.1
```

## 範例4:push Dockerfile至Docker Hub
- 必需建立一個Docker Hub的帳號
- 必需使用docker login登入帳號
- 適合建立多位開發者共同開發環境

**建立**docker file**

```bash
FROM python:3.8-slim

WORKDIR /usr/service/grade-submission-application

COPY . .

RUN pip install -r grade-submission/requirements.txt

EXPOSE 5000

CMD ["python", "grade-submission/app.py"]

```

**建立docker image**
- 建立的docker image name 必需前面使用docker hub的帳號(帳號名稱/name:tag)

```bash
docker build -t roberthsu2003/grade-submission:flask-0.0.1 .
```

**檢查docker image**

```bash
docker images

#=======output========
REPOSITORY                       TAG           IMAGE ID       CREATED         SIZE
roberthsu2003/grade-submission   flask-0.0.1   685a3901f6e1   2 minutes ago   162MB
```

```bash
docker inspect 685a3901f6e1

#======output======
檢查"ContainerConfig"內的資料,有expost port的資訊和env的資訊
```


**上傳至Docker Hub**

```bash
docker push roberthsu2003/grade-submission:flask-0.0.1

#=====output========
The push refers to repository [docker.io/roberthsu2003/grade-submission]
6c179026ab9b: Pushed
15ed0e796a70: Pushed
9d8107f6d0f5: Pushed
71be48336db2: Mounted from library/python
68927dfce826: Mounted from library/python
01183e0d6e03: Mounted from library/python
054df1200f3e: Mounted from library/python
flask-0.0.1: digest: sha256:1a12cea806601102d4a053c316748721885581be0a991ff0a50fbecb2253eae5 size: 1785
```

**檢查docker hsu內是否有上傳**

![](./images/pic4.png)

**其他開發者可以使用docker pull下載docker image**

```bash
docker pull roberthsu2003/grade-submission:flask-0.0.1
```

**透過docker inspect了解images內的設定**

```bash
docker inspect roberthsu2003/grade-submission:flask-0.0.1
```

![](./images/pic5.png)

**建立docker container**

-- 其它開發者透過docker inspect,了解有expose 5000

```bash
docker run -p 2741:5000 roberthsu2003/grade-submission:flask-0.0.1
```

**使用:2741(tcp port)開啟flash 應用程式**
![](./images/pic6.png)


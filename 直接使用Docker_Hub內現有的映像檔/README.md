# Docker Hub 使用教學指南

了解如何使用Docker Hub網站來查看、搜尋和使用Docker映像檔。

## 目錄
1. [什麼是Docker 映像檔](#什麼是docker-映像檔)
2. [什麼是Docker Hub](#什麼是docker-hub)
3. [如何訪問Docker Hub](#如何訪問docker-hub)
4. [搜尋映像檔](#搜尋映像檔)
5. [查看映像檔詳細資訊](#查看映像檔詳細資訊)
6. [下載和使用映像檔](#下載和使用映像檔)
7. [實作範例](#實作範例)
8. [常用映像檔推薦](#常用映像檔推薦)
## 什麼是Docker 映像檔

Docker 映像檔（Image）是 Docker 用來建立容器（Container）的模板。它包含了運行應用程式所需的一切，包括程式碼、運行時環境、系統工具和庫等。

- 想像Image就是要安裝電腦作業系統時的光碟片

## 什麼是Docker Hub

Docker Hub是Docker官方提供的雲端映像檔倉庫服務，您可以在這裡：
- 🔍 搜尋和瀏覽數百萬個公開映像檔
- 📥 下載需要的映像檔到本地環境
- 📤 上傳自己建立的映像檔（需要註冊帳號）
- 📚 查看映像檔的使用說明和文件

## 如何訪問Docker Hub

1. **開啟瀏覽器**，前往 [https://hub.docker.com](https://hub.docker.com)
2. **首頁介面**包含：
   - 搜尋欄：用於搜尋映像檔
   - 熱門映像檔：顯示最受歡迎的映像檔
   - 分類瀏覽：按照不同類別瀏覽映像檔

## 搜尋映像檔

### 基本搜尋
1. 在首頁頂部的**搜尋欄**輸入關鍵字
2. 按下 **Enter** 或點擊搜尋按鈕
3. 瀏覽搜尋結果

### 搜尋技巧
- 使用**具體的關鍵字**：如 `python`、`nginx`、`mysql`
- 查看**官方映像檔**：標有 "Official Image" 標籤
- 注意**下載次數**：通常下載次數多的映像檔較可靠
- 查看**星級評分**：星級越高表示社群評價越好

### 篩選功能
- **Image Type**：選擇官方映像檔或社群映像檔
- **Categories**：按照應用類別篩選
- **Operating System**：選擇作業系統類型

## 查看映像檔詳細資訊

點擊任一映像檔後，您可以看到：

### 1. 基本資訊
- **映像檔名稱**和**描述**
- **官方標籤**（如果是官方映像檔）
- **下載次數**和**星級評分**
- **最後更新時間**

### 2. Tags 標籤頁
- 查看所有可用的**版本標籤**
- 每個標籤的**大小**和**更新時間**
- **架構支援**（如 amd64、arm64）

### 3. Dockerfile 標籤頁
- 查看映像檔的**建構指令**
- 了解映像檔的**建構過程**

### 4. 使用說明
- **Quick Reference**：快速參考指南
- **使用範例**：常見的使用方式
- **環境變數**：可設定的環境變數
- **Volume掛載點**：資料持久化設定

## 下載和使用映像檔

### 1. 複製下載指令
在映像檔頁面右側找到：
```bash
docker pull [映像檔名稱]:[標籤]
```

### 2. 在終端機執行
```bash
# 下載最新版本
docker pull python

# 下載特定版本
docker pull python:3.11-slim

# 查看已下載的映像檔
docker images
```

### 3. 執行容器
```bash
# 基本執行

> 執行一個基於 python 映像檔的容器（預設會執行 python 直譯器，通常container會自動結束）
> 下方會自動下載python:latest的映像檔,並且執行建立一個容器,並且執行python直譯器

docker run python

> 可以使用`docker images`查詢已下載的映像檔
> 可以使用`docker ps`查詢正在執行的container
> 可以使用`docker ps -a`查詢所有container
```

```bash
# 互動式執行
> 如果執行 docker run -it python 而省略了 bash，Docker 會執行該映像檔 (image) 預設的指令 (Default Command)。對於官方的 python 映像檔來說，它的預設指令就是啟動 Python 的互動式直譯器 (REPL)。

docker run -it python bash

```

```bash
# 背景執行並映射埠口
docker run -d -p 8080:80 nginx

> 指令拆解
> 讓我們來分解這個指令的每一個部分：docker run -d -p 8080:80 nginx

> docker run

> 這是最基本的指令，用來從一個映像檔 (image) 建立並啟動一個新的容器 (container)。

> -d 或 --detach

> 這是「分離模式 (detached mode)」的意思。

> 它會讓容器在背景中執行，而不是佔據你目前的終端機視窗。指令執行後，你會立刻拿回你的命令提示字元，可以繼續做其他事。

> 如果沒有-d，你看到的畫面是 Nginx 主程序的標準輸出 (Standard Output) 和標準錯誤 (Standard Error)。

>簡單來說：

> python 映像檔的預設程式是 Python 直譯器 (REPL)。所以沒有 bash 時，你看到的是 Python REPL。

> nginx 映像檔的預設程式是 Nginx 網頁伺服器。所以沒有 -d 時，你看到的是 Nginx 伺服器自己的運行日誌。

> 這與我們之前用的 -it (互動模式) 相反，-d 非常適合用來執行像網頁伺服器、資料庫這類需要長時間運行的服務。

> -p 8080:80 或 --publish

> 這是「發布 (publish)」或「連接埠映射 (port mapping)」的意思，是這個指令最關鍵的部分。

> 它的格式是 [本機電腦的 Port]:[容器內的 Port]。

> 8080 (本機 Port): 這是你自己電腦對外開放的連接埠。你可以把它想像成你家大樓的門牌號碼。你可以把它改成任何你電腦上未被佔用的 Port，例如 3000、8888 等。

> 80 (容器 Port): 這是 Nginx 應用程式在容器內部監聽的預設連接埠。Nginx 作為一個 HTTP 網頁伺服器，預設就是在 80 Port 提供服務。

> 整個 -p 8080:80 的意思就是：「請把所有送到我電腦 8080 Port 的網路流量，全部轉發到這個容器裡的 80 Port。」

nginx

> 這是你要使用的映像檔 (image) 名稱。Docker 會尋找本地是否有名為 nginx 的映像檔，如果沒有，它會自動從 Docker Hub 公共倉庫下載官方的 Nginx 映像檔。
```

## 實作範例

讓我們以三個常用映像檔為例，示範完整的使用流程：

### 範例1：Python 3.11-slim

1. **搜尋**：在Docker Hub搜尋 "python"
2. **選擇**：點擊官方的 "python" 映像檔
3. **查看標籤**：在Tags頁面找到 "3.11-slim"
4. **下載**：
   ```bash
   docker pull python:3.11-slim
   ```
5. **使用**：
   ```bash
   # 執行Python互動式環境
   docker run -it python:3.11-slim python

   # 指令解譯：
   # docker run -it python:3.11-slim python
   #
   # - `docker run`：建立並執行一個新的容器。
   # - `-it`：啟動互動式終端機（-i 保持標準輸入開啟，-t 分配一個虛擬終端）。
   # - `python:3.11-slim`：指定要使用的映像檔（這裡是官方 Python 3.11 的精簡版）。
   # - `python`：在容器內執行 Python 直譯器，進入互動式 Python 命令列。
   #
   # 執行這個指令後，您會進入一個可以直接輸入 Python 指令的互動式環境，非常適合用來測試 Python 程式碼或學習 Python。

   # 執行Python腳本（假設腳本在當前目錄）
   docker run -v $(pwd):/app -w /app python:3.11-slim python script.py
   ```

   **指令詳解**：
   - `docker run`: 建立並執行容器。
   - `-it`: 啟動互動式終端機。
   - `-v $(pwd):/app`: 將本機目錄掛載到容器內的 `/app`。
   - `-w /app`: 設定容器內的工作目錄,會影響後續指令的執行路徑,如果不設定，默認為容器的根目錄,啟動容器後，您會在 `/app` 目錄下執行指令。
   - `python:3.11-slim`: 指定映像檔。
   - `python`: 執行Python互動式直譯器或腳本。

### 範例2：Miniconda3

1. **搜尋**：搜尋 "miniconda"
2. **選擇**：選擇 "continuumio/miniconda3"
3. **下載**：
   ```bash
   docker pull continuumio/miniconda3
   ```
4. **使用**：
   ```bash
   # 啟動Jupyter Notebook
   docker run -p 8888:8888 continuumio/miniconda3 jupyter notebook --ip=0.0.0.0 --allow-root
   ```

   **用途**：
   - 該指令用於啟動一個基於 Miniconda 的容器，並在容器內啟動 Jupyter Notebook 服務。
   - 映射本機埠 `8888` 到容器內的埠 `8888`，使您可以通過瀏覽器訪問 Jupyter Notebook。
   - 適合用於數據分析、機器學習或科學計算等需要互動式編程的場景。

   ```bash
   # 進入容器安裝套件
   docker run -it continuumio/miniconda3 bash
   ```

   **指令詳解**：
   - `docker run`: 建立並執行容器。
   - `-p 8888:8888`: 將容器的埠8888映射到本機的埠8888，這樣您可以通過瀏覽器訪問Jupyter Notebook。
     - 左側的 `8888` 是本機埠號，右側的 `8888` 是容器內的埠號。
   - `continuumio/miniconda3`: 指定使用的映像檔名稱。
   - `jupyter notebook --ip=0.0.0.0 --allow-root`:
     - 啟動Jupyter Notebook服務。
     - `--ip=0.0.0.0`：允許所有IP地址訪問容器內的Jupyter Notebook。
     - `--allow-root`：允許以root身份運行Jupyter Notebook（通常在容器內需要這樣做）。
   - `-it`: 啟動互動式終端機。
     - `-i`：保持標準輸入開啟，允許與容器交互。
     - `-t`：分配一個虛擬終端機。
   - `bash`: 進入容器內的Shell環境，允許您手動執行命令或安裝套件。

### 範例3：PostgreSQL

1. **搜尋**：搜尋 "postgres"
2. **選擇**：選擇官方的 "postgres" 映像檔
3. **查看文件**：了解必要的環境變數設定
4. **下載**：
   ```bash
   docker pull postgres
   ```
5. **使用**：
   ```bash
   # 啟動PostgreSQL資料庫
   docker run --name my-postgres \
     -e POSTGRES_PASSWORD=mypassword \
     -e POSTGRES_DB=mydatabase \
     -p 5432:5432 \
     -d 
     postgres
   
   **指令解釋：**

   這條指令會啟動一個 PostgreSQL 資料庫容器，並進行以下設定：

   - `docker run`：建立並執行一個新的容器。
   - `--name my-postgres`：將這個容器命名為 `my-postgres`，方便後續管理與操作。
   - `-e POSTGRES_PASSWORD=mypassword`：設定資料庫的管理者密碼為 `mypassword`。這是 PostgreSQL 映像檔啟動時必須指定的環境變數。
   - `-e POSTGRES_DB=mydatabase`：啟動時自動建立一個名為 `mydatabase` 的資料庫。
   - `-p 5432:5432`：將本機的 5432 埠對應到容器內的 5432 埠。這樣可以讓本機或其他應用程式連接到這個資料庫服務。
   - `-d`：讓容器在背景（detached mode）執行，不會佔用目前的終端機。
   - `postgres`：指定要使用的映像檔名稱（這裡是官方的 PostgreSQL 映像檔）。

   **簡單來說，這條指令會在本機啟動一個 PostgreSQL 資料庫服務，並設定好密碼與預設資料庫，方便你直接連線使用。**


   # 連接到資料庫
   docker exec -it my-postgres psql -U postgres -d mydatabase

   # 使用dbeaver的連線方式
   URL設定方式 -> jdbc:postgresql://10.170.1.218:5432/mydatabase
   username(使用預設) -> postgres
   password(密碼) -> raspberry
   ```

### 範例4：MongoDB

1. **搜尋**：搜尋 "MongoDB"
2. **選擇**：選擇官方的 "MongoDB" 映像檔(樹莓派4.4.18)
3. **查看文件**：了解必要的環境變數設定
4. **下載**： 
5. **使用**:

**第 1 步：建立一個本地資料夾來存放數據**

首先，我們需要在樹莓派上建立一個資料夾，用來永久保存 MongoDB 的數據。這樣即使您刪除或重建 Docker 容器，您的資料庫內容也不會遺失。

```
mkdir -p $HOME/mongodb-data
```

- mkdir -p 會建立 mongodb-data 資料夾（如果它不存在的話）。

- $HOME 代表您目前使用者的家目錄 (例如 /home/pi)。

**第 2 步：執行 Docker 指令來啟動 MongoDB**

> 因為樹莓派所以使用mongo:4.4.18 

接下來，複製並執行以下指令。請務必將 YOUR_STRONG_PASSWORD 替換成您自己的高強度密碼。

```
docker run -d \
   --name my-mongodb \
   -p 27017:27017 \
   -v $HOME/mongodb-data:/data/db \
   -e MONGO_INITDB_ROOT_USERNAME=myuser \
   -e MONGO_INITDB_ROOT_PASSWORD=YOUR_STRONG_PASSWORD \
   --restart unless-stopped \
   mongo:4.4.18
```

**指令參數詳解**

讓我們來分解一下這個指令的各個部分，這樣您就能明白它的作用：

- docker run: 這是啟動一個新容器的基礎指令。

- -d: Detached 模式，讓容器在背景執行。

- --name my-mongodb: 為您的容器取一個好記的名稱，方便日後管理。

- -p 27017:27017: 端口映射。將樹莓派主機的 27017 埠映射到容器內部的 27017 埠。這樣您就可以從樹莓派的其他應用程式連接到這個資料庫了。

- -v $HOME/mongodb-data:/data/db: 掛載儲存卷 (Volume)。這是實現資料持久化的關鍵。它將我們剛才建立的 $HOME/mongodb-data 資料夾掛載到容器內部存放資料庫檔案的 /data/db 路徑。

- -e MONGO_INITDB_ROOT_USERNAME=myuser: 設定環境變數。設定 MongoDB 的初始 root 使用者名稱為 myuser。

- -e MONGO_INITDB_ROOT_PASSWORD=YOUR_STRONG_PASSWORD: 設定 MongoDB 的初始 root 使用者密碼。請務必更換成您自己的安全密碼！

- --restart unless-stopped: 自動重啟。這是一個很好的策略，確保 Docker 服務啟動或樹莓派重開機時，這個容器也會自動啟動，除非您手動將它停止。

- mongo: 要使用的 Docker 映像檔名稱。Docker 會自動抓取支援您樹莓派 (aarch64) 架構的版本。

**第 3 步：驗證與連線**

1. 檢查容器狀態：

```
docker ps
```

2. 查看日誌:

```
docker logs my-mongodb
```


**第4步 使用Mongo Compass連線方式**:

- myuser, YOUR_STRONG_PASSWORD,localhost:要依據建立的方式更新

```
mongodb://myuser:YOUR_STRONG_PASSWORD@localhost:27017/
```


## 常用映像檔推薦

### 程式語言
- **python**: Python官方映像檔
- **node**: Node.js官方映像檔
- **openjdk**: Java官方映像檔
- **golang**: Go語言官方映像檔

### 資料庫
- **postgres**: PostgreSQL資料庫
- **mysql**: MySQL資料庫
- **redis**: Redis記憶體資料庫
- **mongodb**: MongoDB文件資料庫

### 網頁伺服器
- **nginx**: 高效能網頁伺服器
- **apache**: Apache HTTP伺服器
- **httpd**: Apache HTTP伺服器（官方版本）

### 作業系統
- **ubuntu**: Ubuntu Linux
- **alpine**: 輕量級Linux發行版
- **centos**: CentOS Linux

## 學習小貼士

### ✅ 最佳實務
1. **優先選擇官方映像檔**：更安全、更穩定
2. **選擇適當的標籤**：如選擇 `slim` 版本減少映像檔大小
3. **閱讀使用文件**：了解正確的使用方式
4. **檢查更新頻率**：選擇維護良好的映像檔

### ⚠️ 注意事項
1. **安全性考量**：避免使用來源不明的映像檔
2. **版本管理**：在生產環境中指定具體版本標籤
3. **資源使用**：注意映像檔大小，避免不必要的資源浪費
4. **授權條款**：確認映像檔的使用授權

## 練習作業

1. **基礎練習**：
   - 搜尋並下載 `hello-world` 映像檔
   - 執行該映像檔並觀察輸出結果

2. **進階練習**：
   - 比較 `python:3.11` 和 `python:3.11-slim` 的大小差異
   - 使用 `nginx` 映像檔建立一個簡單的網頁伺服器

3. **實戰練習**：
   - 組合使用多個映像檔建立一個完整的應用環境
   - 例如：前端(nginx) + 後端(python) + 資料庫(postgres)

## 總結

Docker Hub是學習和使用Docker的重要資源。透過本教學，您應該已經學會：
- 如何在Docker Hub上搜尋和瀏覽映像檔
- 如何查看映像檔的詳細資訊和使用說明
- 如何下載和使用不同類型的映像檔
- 如何選擇適合的映像檔版本和標籤
## 總結

Docker Hub是學習和使用Docker的重要資源。透過本教學，您應該已經學會：
- 如何在Docker Hub上搜尋和瀏覽映像檔
- 如何查看映像檔的詳細資訊和使用說明
- 如何下載和使用不同類型的映像檔
- 如何選擇適合的映像檔版本和標籤

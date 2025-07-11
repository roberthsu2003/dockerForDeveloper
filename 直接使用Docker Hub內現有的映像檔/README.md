# Docker Hub 使用教學指南

本教學將帶您了解如何使用Docker Hub網站來查看、搜尋和使用Docker映像檔。

## 目錄
1. [什麼是Docker Hub](#什麼是docker-hub)
2. [如何訪問Docker Hub](#如何訪問docker-hub)
3. [搜尋映像檔](#搜尋映像檔)
4. [查看映像檔詳細資訊](#查看映像檔詳細資訊)
5. [下載和使用映像檔](#下載和使用映像檔)
6. [實作範例](#實作範例)
7. [常用映像檔推薦](#常用映像檔推薦)

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
docker run python

# 互動式執行
docker run -it python bash

# 背景執行並映射埠口
docker run -d -p 8080:80 nginx
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
   
   # 執行Python腳本（假設腳本在當前目錄）
   docker run -v $(pwd):/app -w /app python:3.11-slim python script.py
   ```

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
   
   # 進入容器安裝套件
   docker run -it continuumio/miniconda3 bash
   ```

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
     -d postgres
   
   # 連接到資料庫
   docker exec -it my-postgres psql -U postgres -d mydatabase
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

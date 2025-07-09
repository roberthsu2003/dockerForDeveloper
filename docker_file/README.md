# Dockerfile 介紹（Python 版）

Dockerfile 是一個用來自動建立 Docker 容器映像的文字檔。對於 Python 開發者來說，Dockerfile 可以幫助你快速建立一個乾淨、一致的 Python 執行環境，讓你的程式在任何電腦上都能順利執行。

## 為什麼要用 Dockerfile？

- 讓你的 Python 程式不會因為每台電腦環境不同而出錯。
- 可以快速分享、部署你的應用程式。
- 學會 Dockerfile，未來在團隊合作或上雲端都很有幫助。

## Dockerfile 的基本結構

Dockerfile 由一行一行的「指令」組成，每一行都在描述如何建立你的環境。

```dockerfile
# 這是註解
INSTRUCTION 參數
```

常見的指令有：

- **`FROM`**
  - **說明**：這是每個 Dockerfile 的第一行指令，用來指定你的新映像要基於哪個「基礎映像」來建立。你可以把它想像成蓋房子的地基。
  - **範例**：
    ```dockerfile
    # 使用官方 Python 3.11 的輕量版 (slim) 作為基礎
    FROM python:3.11-slim
    ```

- **`WORKDIR`**
  - **說明**：設定容器內的工作目錄。之後的 `RUN`、`CMD`、`COPY` 等指令都會在這個目錄下執行。如果目錄不存在，它會自動被建立。
  - **範例**：
    ```dockerfile
    # 設定容器內的工作目錄為 /app
    WORKDIR /app
    ```

- **`COPY`**
  - **說明**：將你電腦本機的檔案或資料夾，複製到容器的檔案系統裡面。
  - **範例**：
    ```dockerfile
    # 將本機的 requirements.txt 複製到容器的 /app 目錄下
    COPY requirements.txt .

    # 將本機的 src 資料夾內所有東西，複製到容器的 /app/src 目錄下
    COPY src/ ./src
    ```

- **`RUN`**
  - **說明**：在映像建立過程中執行指令，通常用來安裝套件或軟體。每執行一次 `RUN` 都會建立一個新的映像層 (layer)。
  - **範例**：
    ```dockerfile
    # 更新套件庫並安裝 git
    RUN apt-get update && apt-get install -y git

    # 使用 pip 安裝 Python 套件
    RUN pip install -r requirements.txt
    ```

- **`CMD`**
  - **說明**：設定當容器啟動時，預設要執行的指令。一個 Dockerfile 只能有一個 `CMD`。如果在 `docker run` 時指定了其他指令，`CMD` 的設定會被覆蓋。
  - **範例**：
    ```dockerfile
    # 設定容器啟動時，執行 python app.py
    CMD ["python", "app.py"]
    ```

- **`EXPOSE`**
  - **說明**：這是一個「聲明」或「文件」，告訴別人這個容器內的應用程式會使用哪個 port。它本身不會真的把 port 開放給外部存取，你還是需要在 `docker run` 時使用 `-p` 參數來對應 port。
  - **範例**：
    ```dockerfile
    # 聲明容器會使用 5000 port
    EXPOSE 5000
    ```

- **`ENV`**
  - **說明**：用來設定容器內的環境變數。這個變數可以在後續的指令（如 `RUN`）中使用，也可以被容器中執行的應用程式讀取。
  - **範例**：
    ```dockerfile
    # 設定一個名為 APP_VERSION 的環境變數
    ENV APP_VERSION=1.0
    ```

## Python Dockerfile 範例

假設你有一個簡單的 Python 程式 `hello.py`：

```python
print("Hello, Docker!")
```

你還有一個 `requirements.txt`（如果有用到第三方套件，這裡可以先放空）：

```
# 這裡可以列出你要安裝的 Python 套件，例如：
# requests
```

### 對應的 Dockerfile

```dockerfile
# 1. 選擇官方 Python 映像作為基礎
FROM python:3.11-slim

# 2. 設定工作目錄
WORKDIR /app

# 3. 複製需求檔與程式碼到映像中
COPY requirements.txt ./
COPY hello.py ./

# 4. 安裝 Python 套件（如果 requirements.txt 有內容）
RUN pip install --no-cache-dir -r requirements.txt

# 5. 設定容器啟動時執行的指令
CMD ["python", "hello.py"]
```

### 建立與執行步驟

1. 把上面的 `hello.py`、`requirements.txt` 和 `Dockerfile` 放在同一個資料夾。
2. 在該資料夾下打開終端機，執行：
   ```sh
   docker build -t my-python-app .
   ```
   這會建立一個名為 `my-python-app` 的映像。
3. 執行容器：
   ```sh
   docker run --rm my-python-app
   ```
   你會看到畫面輸出：
   ```
   Hello, Docker!
   ```

---

這樣就完成了最基本的 Python Dockerfile 教學！你可以把 `hello.py` 換成自己的 Python 程式，或在 `requirements.txt` 加上需要的套件。

---

## 更多實用範例

### 範例 1：Flask 網頁應用程式

假設你有一個 Flask 應用程式 `app.py`：

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Flask in Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

對應的 `requirements.txt`：
```
Flask==2.3.3
```

**Dockerfile：**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# 先複製 requirements.txt 並安裝套件（利用 Docker 快取機制）
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 再複製應用程式碼
COPY app.py .

# 聲明使用的 port
EXPOSE 5000

# 啟動 Flask 應用程式
CMD ["python", "app.py"]
```

**執行方式：**
```sh
docker build -t flask-app .
docker run -p 5000:5000 flask-app
```
然後在瀏覽器開啟 `http://localhost:5000`

### 範例 2：使用資料庫的應用程式

假設你的應用程式需要連接 PostgreSQL 資料庫：

```python
# db_app.py
import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health():
    try:
        # 從環境變數讀取資料庫連線資訊
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            database=os.getenv('DB_NAME', 'mydb'),
            user=os.getenv('DB_USER', 'user'),
            password=os.getenv('DB_PASSWORD', 'password')
        )
        conn.close()
        return jsonify({"status": "healthy", "database": "connected"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

`requirements.txt`：
```
Flask==2.3.3
psycopg2-binary==2.9.7
```

**Dockerfile：**
```dockerfile
FROM python:3.11-slim

# 安裝系統相依套件
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY db_app.py .

# 設定預設環境變數
ENV DB_HOST=localhost
ENV DB_NAME=mydb
ENV DB_USER=user
ENV DB_PASSWORD=password

EXPOSE 5000

CMD ["python", "db_app.py"]
```

### 範例 3：多階段建置（Multi-stage Build）

適合需要編譯步驟或想要減少最終映像大小的情況：

**Dockerfile：**
```dockerfile
# 第一階段：建置階段
FROM python:3.11 as builder

WORKDIR /app

# 安裝建置工具
RUN pip install --upgrade pip setuptools wheel

# 複製並安裝相依套件
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# 第二階段：執行階段
FROM python:3.11-slim

# 建立非 root 使用者
RUN useradd --create-home --shell /bin/bash app

WORKDIR /app

# 從建置階段複製已安裝的套件
COPY --from=builder /root/.local /home/app/.local

# 複製應用程式碼
COPY app.py .

# 更改檔案擁有者
RUN chown -R app:app /app

# 切換到非 root 使用者
USER app

# 確保使用者安裝的套件在 PATH 中
ENV PATH=/home/app/.local/bin:$PATH

EXPOSE 5000

CMD ["python", "app.py"]
```

### 範例 4：使用 Docker Compose 的完整應用程式

當你的應用程式需要多個服務時，可以使用 Docker Compose：

**docker-compose.yml：**
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - DB_HOST=db
      - DB_NAME=myapp
      - DB_USER=postgres
      - DB_PASSWORD=password
    depends_on:
      - db
    volumes:
      - ./logs:/app/logs

  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=myapp
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  postgres_data:
```

**執行方式：**
```sh
docker-compose up --build
```

### 範例 5：機器學習應用程式

適合需要科學計算套件的 ML 應用：

**Dockerfile：**
```dockerfile
FROM python:3.11-slim

# 安裝系統相依套件
RUN apt-get update && apt-get install -y \
    build-essential \
    libhdf5-dev \
    libopenblas-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 複製需求檔案
COPY requirements.txt .

# 安裝 Python 套件
RUN pip install --no-cache-dir -r requirements.txt

# 複製模型檔案和應用程式碼
COPY models/ ./models/
COPY predict.py .

# 建立輸出目錄
RUN mkdir -p /app/output

EXPOSE 8000

# 使用 gunicorn 作為 WSGI 伺服器
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "predict:app"]
```

對應的 `requirements.txt`：
```
numpy==1.24.3
pandas==2.0.3
scikit-learn==1.3.0
flask==2.3.3
gunicorn==21.2.0
```

### 範例 6：開發環境 Dockerfile

適合開發時使用，包含開發工具：

**Dockerfile.dev：**
```dockerfile
FROM python:3.11

WORKDIR /app

# 安裝開發工具
RUN pip install --upgrade pip
RUN pip install pytest black flake8 mypy jupyter

# 複製需求檔案
COPY requirements.txt requirements-dev.txt ./
RUN pip install -r requirements.txt -r requirements-dev.txt

# 設定開發環境變數
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

# 掛載程式碼目錄（在 docker run 時使用 -v）
VOLUME ["/app"]

EXPOSE 5000 8888

# 預設啟動 bash，方便開發
CMD ["/bin/bash"]
```

**使用方式：**
```sh
# 建置開發映像
docker build -f Dockerfile.dev -t my-app-dev .

# 執行開發容器
docker run -it -v $(pwd):/app -p 5000:5000 -p 8888:8888 my-app-dev
```

---

## 最佳實踐建議

1. **利用快取機制**：先複製 `requirements.txt` 並安裝套件，再複製程式碼
2. **使用 .dockerignore**：排除不需要的檔案，減少建置時間
3. **多階段建置**：分離建置和執行環境，減少最終映像大小
4. **非 root 使用者**：提高安全性
5. **環境變數**：讓容器更有彈性
6. **健康檢查**：確保應用程式正常運作

**範例 .dockerignore：**
```
.git
.gitignore
README.md
Dockerfile
.dockerignore
node_modules
npm-debug.log
.coverage
.pytest_cache
__pycache__
*.pyc
*.pyo
*.pyd
.env
.venv
```

---

> 💡 **小提示**：選擇適合的基礎映像很重要！`python:3.11-slim` 比 `python:3.11` 小很多，但如果需要編譯套件，可能需要完整版本。

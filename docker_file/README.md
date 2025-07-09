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

- **FROM**：指定要用哪個基礎映像（例如 Python 3.11）。
- **WORKDIR**：設定之後指令的工作目錄。
- **COPY**：把本機的檔案複製到映像裡。
- **RUN**：在映像裡執行指令（例如安裝套件）。
- **CMD**：設定容器啟動時要執行的預設指令。
- **EXPOSE**：告訴 Docker 這個容器會用到哪些 port（通常給網頁伺服器用，純 Python 程式可省略）。
- **ENV**：設定環境變數。

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

> 進階：如果你的程式需要網頁伺服器（例如用 Flask)，可以加上 `EXPOSE 5000`，並修改 `CMD` 來啟動 Flask。




# Dockerfile 介紹

Dockerfile 是一個包含建立 Docker 容器映像指示的文字檔。它可以自動為您的應用程式建立一致、可重複的環境。

## 基本結構

**Dockerfile 由指令和參數組成,格式如下:**

```dockerfile
# Comment
INSTRUCTION arguments
```

Dockerfile 通常由以下幾部分組成：

- **基礎映像資訊**：指定所使用的基礎映像。
- **維護者資訊**：標明負責此映像的維護者。
- **映像操作指令**：定義如何安裝軟體、配置環境等。
- **容器啟動時執行指令**：指定容器啟動時的默認命令。

### 常用指令

以下是一些在 Dockerfile 中常用的指令：

- **FROM**: 定義基礎映像，必須是 Dockerfile 的第一條指令。
  
```dockerfile
FROM ubuntu:20.04
```

- **MAINTAINER**: 指定維護者的聯絡資訊（現在建議使用 LABEL 替代）。
  
```dockerfile
MAINTAINER your_name <your_email@example.com>
```
  
- **WORKDIR**: 設定後續指令的工作目錄

```dockerfile
WORKDIR /app
```

- **COPY**: 將檔案從主機複製到映像中。
  
```dockerfile
COPY ./requirements.txt ./
```

- **ADD**: 與 COPY 類似，但可以自動解壓縮 tar 檔案或從 URL 複製檔案。
  
```dockerfile
ADD https://example.com/file.tar.gz ./
```


- **RUN**: 執行命令，通常用於安裝應用程式或執行其他必要的配置。
  
```dockerfile
RUN apt-get update && \
		apt-get install -y python3
```
  
  - **EVN**: 設定環境變數

```dockerfile
ENV NODE_ENV=production \
	PORT=3000
```

- **EXPOSE**: 設定開放port，以便外部訪問。
  
```dockerfile
EXPOSE 80
```



- **CMD**: 指定容器啟動時執行的命令。每個 Dockerfile 最多只能有一條 CMD 指令。
  
```dockerfile
CMD ["nginx", "-g", "daemon off;"]
```

- **ENTRYPOINT**: 設置容器啟動後執行的命令，與 CMD 不同的是，ENTRYPOINT 不會被 docker run 提供的參數覆蓋。
  
```dockerfile
ENTRYPOINT ["python"]
```


### 使用範例1

以下是一個簡單的 Dockerfile 範例，用於創建一個運行 Nginx 的映像：

```dockerfile
# 使用官方 Nginx 基礎映像
FROM nginx

# 複製本地檔案到容器中
COPY ./index.html /usr/share/nginx/html/index.html

# 暴露端口
EXPOSE 80

# 設置默認命令
CMD ["nginx", "-g", "daemon off;"]
```

這個 Dockerfile 將創建一個包含 Nginx 的映像，並將本地的 `index.html` 文件複製到 Nginx 的默認網頁目錄中。當容器啟動時，它會運行 Nginx 並監聽在端口 80 上。

### 使用範例2
為了Node.js應用程式

```dockerfile
# Use official Node.js image as base
FROM node:16-slim

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY package*.json ./
RUN npm install

# Bundle app source
COPY . .

# Create non-root user
RUN useradd -r appuser && \
    chown -R appuser /usr/src/app
USER appuser

# Expose port
EXPOSE 3000

# Define entry command
CMD ["npm", "start"]
```




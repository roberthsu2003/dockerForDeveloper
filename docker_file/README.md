# Dockerfile 介紹

Dockerfile 是一個用來自動化構建 Docker 映像的文本文件。它包含了一系列的指令，這些指令定義了如何從基礎映像創建新的映像。以下是 Dockerfile 的基本結構和常用指令。

## 基本結構

Dockerfile 通常由以下幾部分組成：

- **基礎映像資訊**：指定所使用的基礎映像。
- **維護者資訊**：標明負責此映像的維護者。
- **映像操作指令**：定義如何安裝軟體包、配置環境等。
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

- **RUN**: 執行命令，通常用於安裝應用程式或執行其他必要的配置。
  
  ```dockerfile
  RUN apt-get update && apt-get install -y nginx
  ```

- **COPY**: 將檔案從主機複製到映像中。
  
  ```dockerfile
  COPY ./local-file.txt /app/file.txt
  ```

- **ADD**: 與 COPY 類似，但可以解壓縮 tar 檔案或從 URL 複製檔案。
  
  ```dockerfile
  ADD https://example.com/file.tar.gz /app/
  ```

- **CMD**: 指定容器啟動時執行的命令。每個 Dockerfile 最多只能有一條 CMD 指令。
  
  ```dockerfile
  CMD ["nginx", "-g", "daemon off;"]
  ```

- **ENTRYPOINT**: 設置容器啟動後執行的命令，與 CMD 不同的是，ENTRYPOINT 不會被 docker run 提供的參數覆蓋。
  
  ```dockerfile
  ENTRYPOINT ["python"]
  ```

- **EXPOSE**: 聲明容器所使用的端口，以便外部訪問。
  
  ```dockerfile
  EXPOSE 80
  ```

### 使用範例

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




# Docker python開發者環境建立
## 1. 為何要使用Docker?(Why Docker?)
- ***建立虛擬環境***
- ***建立完全獨立環境專案,並提供該專案所有附屬套件***
- 可建立多個服務,如資料庫服務
- 容易部署和發佈
- 讓共同開發者在不同平台有***相同開發環境***
  
## 2. Dockerize an App

- [建立一個python學習的環境](1.建立pyhton學習環境)

  
## 3. Immediate file changes(Volumes)
- volumes可設定本機資料夾為container所管理的資料夾
- 在docker run 時建立Volumes 

```
 docker run -d \
  --name devtest \
  -v myvol2:/app \
  nginx:latest
```


## 4. Use IDE In Docker
## 5. Docker Compose
## 6. Add more services
## 7. Debug Python code inside Docker
# docker run指令常用的參數

以下是一些 Docker run 常見指令，幫助你更靈活地啟動與管理容器：

## 1. 基本啟動指令

**docker run：啟動一個新的容器實例。**

```
docker run my-image
```

-	-d：將容器以背景模式運行（detached mode），適合服務型應用程式。
-	--name：給容器命名，方便之後管理，例如 --name my-container。

## 2. port轉送

**-p：將主機的端口映射到容器的端口，使容器內的服務可以被外部訪問。**

```bash
docker run -d -p 8080:80 my-image
```

> 範例說明：此指令將主機的 8080 端口映射到容器的 80 端口。

## 3. 掛載卷（Volumes）

**-v：將主機的目錄或檔案掛載到容器中，實現資料持久化。**

```bash
docker run -d -v /path/on/host:/path/in/container my-image
```

> 範例說明：/path/on/host 是主機目錄，/path/in/container 是容器內掛載點。

## 4. 環境變數設定

**e：設置環境變數，將設定值傳遞給容器。**

```bash
docker run -d -e MY_VAR=my_value my-image
```

> 範例說明：設置環境變數 MY_VAR，值為 my_value。

## 5. 限制資源使用

**•	--memory：限制容器的最大記憶體使用量。**

```bash
docker run -d --memory="512m" my-image
```

>	範例說明：將容器的記憶體使用限制為 512 MB。

**--cpus：限制容器使用的 CPU 數量。**

```bash
docker run -d --cpus="1.5" my-image
```

> 範例說明：限制容器最多使用 1.5 個 CPU。

## 6. 互動模式

**-it：以互動模式啟動容器，通常搭配 Bash 進入容器內操作**

```
docker run -it my-image /bin/bash
```

> 範例說明：這樣可以直接進入容器的終端執行指令。

## 7. 網路設定

**•	--network：指定容器要連接的網路，方便多容器間通訊。**

```
docker run -d --network my-network my-image
```

> 範例說明：將容器連接到一個自定義的網路 my-network，可以與其他在同網路內的容器通訊。

## 8. 自動重啟

**•	--restart：設定容器的重啟策略，例如在容器崩潰時自動重啟。**

```
docker run -d --restart=always my-image
```

```
•	選項說明：
•	no：不重啟（預設）。
•	on-failure：僅在容器異常停止時重啟。
•	always：無論什麼情況都重啟容器。
```

## 9. 刪除退出的容器

**•	--rm：當容器停止時自動刪除，適合短暫執行的容器。**

```
docker run --rm my-image
```

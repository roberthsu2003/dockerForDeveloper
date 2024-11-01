# docker build指令常用的參數

## 1. 基本docker build參數

```bash
docker build -t <image-name>:<tag> <path>
```

- -t:指定image的名稱,也可以加上:<版本名稱>(eg. my-image:latest)
- <paht>:指定Dockerfile的位置一般使用 **.** ,代表是目前目錄

**Example:**

```bash
docker build -t my-app:latest .
```

## 2. --file 指定自訂的Dockerfile名稱

```bash
docker build -f <dockerfile_name> .
```

**Example**

```bash
docker build -f Dockerfile.dev -t my-app:dev .
```

> 指定特定名稱Dockerfile.dev

## 3. 使用--build-arg來傳遞引數值

```
docker build --build-arg <arg_name>=<value> -t my-app .
```


**Example**

```bash
docker build --build-arg NODE_ENV=production -t my-app:latest .
```


## 4. --no-cache 指定不要儲存每一層安裝時下載的資料

```bash
docker build --no-cache -t my-app .
```

- --no-cache:強制 Docker 在不使用任何快取的情況下建立映像，確保每一層都會重新執行。

**Example**

```bash
docker build --no-cache -t my-app:latest .
```

## 5. --quiet 減少多餘的輸出

```bash
docker build --quiet -t my-app .
```

**Example**

```bash
docker build --quiet -t my-app:latest .
```

## 6.使用遠端的DockerFile(Git)

```bash
docker build <url>
```

**Example**

```bash
docker build https://github.com/user/repo.git#branch
```



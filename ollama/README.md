# 建立ollama
- [ollama官網安裝說明](https://github.com/ollama/ollama)

## 1. 下載ollama官方image

```bash
docker pull ollama/ollama
```

**確認已經下載image**

```bash
docker images ls
```

## 2. 啟動容器
- 啟動容器
- 建立本地端的ollam資料夾(要和容器的/root/.ollama)同步
- ollama下載的模型預設全部會下載至/root/.ollama
- ollama預設的port為11434

```bash
mkdir $HOME/Documents/ollama
docker run -itd -v $HOME/Documents/ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

## 3. 透過本機終端機下載模型

**3.1 下載模型**

- 下載的模型會在容器的/root/.ollama,本機的$HOME/Documents/ollama


```bash
docker exec -it ollama ollama pull llama3.2:3b
```

**3.2 執行模型**

```bash
docker exec -it ollama ollama run llama3.2:3b
```

**3.3 檢查所有模型**

```bash
docker exec -it ollama ollama list
```

**3.4 刪除模型**

```bash
docker exec -it ollama ollama delete llama3.2:3b
```

**3.5 更新模型**

```bash
docker exec -it ollama ollama update llama3.2:3b
```

## 4.0 Docker Container網路有關的設定
- 在container內,可以直接請求host.docker.internal:port,以操作本機端的http服務

```
--add-host=host.docker.internal:host-gateway
```






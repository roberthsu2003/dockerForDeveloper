# 常用的docker指令

- **檢查目前所有的image**
- Prompt:`如何列出我擁有的所有 Docker 映像？`
	<details>
	How do I list all the Docker images that I have?
	</details>

```bash
docker images
```
---
- **刪除image**
- Prompt:`如何刪除特定的 Docker 映像？ `
	<details>
	How do I delete specific Docker images that I have?
	</details>

```bash
docker rmi <image_name>
```
---
- **檢查目前正在執行的容器**
- Prompt:`如何檢查 Docker 容器是否仍在執行中 `
<details>
How do I check if a Docker container is still running
</details>

```bash
docker ps
```
---
- **檢查目前所有的容器**
- prompt:`如何列出我擁有的所有 Docker 容器？`
	<details>
	How do I list all the Docker containers that I have?
	</details>

```bash
docker ps -a
```
---

- **停止目前執行中的容器**
- Prompt:`如何停止正在執行的 Docker 容器？`
	<details>
	How do I stop a Docker container that is running?
	</details>

```bash
docker stop <container_name>
```

- **重新啟動容器**
- Prompt:`如何重新啟動已停止運作的 Docker 容器？ `
	<details>
	How do I restart a Docker container that has stopped working?
	</details>
	
```bash
docker restart <container_name>
```

- **刪除目前的容器**
- Prompt:`如何刪除我擁有的 Docker 容器？`
	<details>
	How do I delete Docker containers that I have?
	</details>

```bash
docker rm <container_name>
```

- **刪除所有未使用的docker cache**
- prompt: 如何刪除我擁有的所有 Docker 容器和映像？
	<details>
	How do I delete all of the Docker containers and images that I have?
	</details>

```
#1停止目前所有的容器`-q`代表只要顯示id
docker stop $(docker ps -q)

#2移除目前所有的docker container
docker rm $(docker ps -a -q)

#3移除目前所有的image
docker rmi $(docker images -q)

#4移除目前所有的積卷 -f 不用提醒
docker volume prune -f

#移除目前所有的network `-f` 不要提醒
docker network prune -f

#移除所有沒有使用使用的data(包含images,containers,volumne,and networks還有下載的build cache
#`-a`移除所有未使用的images,'--volumes`移除所有未使用的volumes
docker system prune -a --volumes
```
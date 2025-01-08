# 常用的docker指令

- **檢查目前所有的image**

```bash
docker images
```
---
- **刪除image**

```bash
docker rmi <image_name>
```
---
- **檢查目前正在執行的容器**

```bash
docker ps
```
---
- **檢查目前所有的容器**

```bash
docker ps -a
```
---

- **停止目前執行中的容器**

```bash
docker stop <container_name>
```

- **刪除目前的容器**

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
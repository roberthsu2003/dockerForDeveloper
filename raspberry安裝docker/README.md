# 樹莓派安裝 Docker 完整指南

## 📋 目錄
- [系統需求](#系統需求)
- [前置準備](#前置準備)
- [安裝步驟](#安裝步驟)
- [驗證安裝](#驗證安裝)
- [常見問題排除](#常見問題排除)
- [基本使用範例](#基本使用範例)

---

## 🖥️ 系統需求

### 硬體需求
- **Raspberry Pi 4** (推薦) 或 Raspberry Pi 3B+
- **記憶體**: 至少 4GB RAM (Docker 需要足夠記憶體)
- **儲存空間**: 至少 32GB microSD 卡
- **網路連線**: 穩定的網際網路連線

### 軟體需求
- **作業系統**: Raspberry Pi OS (64-bit) 或 Ubuntu 20.04+
- **架構**: ARM64 (aarch64) 或 ARMv7

---

## 🔧 前置準備

### 1. 更新系統套件
```bash
# 更新套件清單
sudo apt update

# 升級系統套件
sudo apt upgrade -y

# 安裝必要的工具
sudo apt install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

### 2. 檢查系統架構

請先確認您的作業系統與架構，這樣才能在 Docker Hub 上找到相容且正確的映像檔。

> aarch64 代表 "ARM Architecture 64-bit"。
> aarch64 是 ARM 公司推出的 ARMv8-A 指令集架構 中 64 位元執行狀態的名稱。

```bash
# 檢查系統架構
uname -m #aarch64

# 檢查作業系統版本
lsb_release -a
```

---

## 📦 安裝步驟

### 方法：使用官方安裝腳本 (推薦)

#### 1. 下載並執行 Docker 官方安裝腳本
```bash
# 下載安裝腳本
curl -fsSL https://get.docker.com -o get-docker.sh

# 執行安裝腳本
sudo sh get-docker.sh
```

#### 2. 將使用者加入 docker 群組
```bash
# 將目前使用者加入 docker 群組
sudo usermod -aG docker $USER

# 重新載入群組設定 (需要重新登入)
newgrp docker
```


## ✅ 驗證安裝

### 1. 檢查 Docker 版本
```bash
# 檢查 Docker 版本
docker --version

# 檢查 Docker Compose 版本
docker-compose --version
```

### 2. 測試 Docker 是否正常運作
```bash

# 檢查 Docker 系統資訊
docker system info
```

### 3. 檢查 Docker 服務狀態
```bash
# 檢查 Docker 服務狀態
sudo systemctl status docker

# 檢查 Docker 是否正在執行
sudo systemctl is-active docker
```

---

## 🔍 常見問題排除

### 問題 1: 權限不足錯誤
**錯誤訊息**: `permission denied while trying to connect to the Docker daemon socket`

**解決方案**:
```bash
# 確認使用者已加入 docker 群組
groups $USER

# 如果沒有看到 docker 群組，重新加入
sudo usermod -aG docker $USER

# 重新登入或重新載入群組
newgrp docker
```

### 問題 2: 記憶體不足
**錯誤訊息**: `no space left on device` 或容器無法啟動

**解決方案**:
```bash
# 清理 Docker 系統
docker system prune -a

# 檢查磁碟使用量
df -h

# 清理未使用的映像檔
docker image prune -a
```

### 問題 3: 網路連線問題
**錯誤訊息**: 無法拉取映像檔

**解決方案**:
```bash
# 檢查網路連線
ping google.com

# 檢查 Docker 網路設定
docker network ls

# 重設 Docker 網路
sudo systemctl restart docker
```

### 問題 4: ARM 架構相容性
**解決方案**:
```bash
# 搜尋 ARM 相容的映像檔
docker search --filter is-official=true nginx

# 使用多平台映像檔
docker pull --platform linux/arm64 nginx:latest
```

---

## 🚀 基本使用範例

### 1. 執行簡單的 Web 伺服器
```bash
# 使用 Nginx
docker run -d -p 8080:80 --name my-nginx nginx:alpine

# 檢查容器狀態
docker ps

# 測試網頁
curl http://localhost:8080
```

### 2. 建立並執行 Python 應用程式
```bash
# 建立 Python 應用程式目錄
mkdir ~/python-app
cd ~/python-app

# 建立 app.py
cat > app.py << EOF
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Raspberry Pi Docker!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
EOF

# 建立 Dockerfile
cat > Dockerfile << EOF
FROM python:3.9-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
EOF

# 建立 requirements.txt
echo "Flask==2.0.1" > requirements.txt

# 建構映像檔
docker build -t my-python-app .

# 執行容器
docker run -d -p 5000:5000 --name my-app my-python-app
```

### 3. 使用 Docker Compose
```bash
# 建立 docker-compose.yml
cat > docker-compose.yml << EOF
version: '3.8'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - .:/app
    environment:
      - FLASK_ENV=development
EOF

# 啟動服務
docker compose up -d

# 停止服務
docker compose down
```

---

## 📊 效能優化建議

### 1. 記憶體管理
```bash
# 設定 Docker 記憶體限制
echo 'GRUB_CMDLINE_LINUX="cgroup_enable=memory cgroup_memory=1"' | sudo tee -a /etc/default/grub
sudo update-grub
```

### 2. 儲存空間優化
```bash
# 定期清理 Docker 系統
docker system prune -a --volumes

# 設定自動清理 (建立 cron 工作)
echo "0 2 * * * docker system prune -f" | sudo crontab -
```

### 3. 網路優化
```bash
# 使用本地映像檔快取
docker pull hello-world
```

---

## 🔗 相關資源

- [Docker 官方文件](https://docs.docker.com/)
- [Raspberry Pi 官方文件](https://www.raspberrypi.org/documentation/)
- [Docker Hub](https://hub.docker.com/)
- [ARM 映像檔清單](https://github.com/docker-library/official-images)

---

## 📝 注意事項

1. **記憶體限制**: Raspberry Pi 的記憶體有限，建議只執行必要的容器
2. **ARM 架構**: 確保使用的映像檔支援 ARM 架構
3. **效能考量**: Docker 在樹莓派上的效能會比在 x86 系統上慢
4. **儲存空間**: 定期清理未使用的映像檔和容器以節省空間
5. **安全性**: 避免在生產環境中執行有安全風險的容器

---

**🎉 恭喜！您已成功在 Raspberry Pi 上安裝並設定 Docker！**

如有任何問題，請參考上述的常見問題排除章節，或查閱 Docker 官方文件。

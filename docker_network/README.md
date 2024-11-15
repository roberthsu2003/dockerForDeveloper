# Docker network

## 什麼是Docker network?

Docker Network 允許容器彼此、主機和外部系統進行通訊。透過使用 Docker 網路，您可以控制容器之間的互動方式、隔離應用程式，並加強容器化環境的安全性。

## Docker network主要功能
- **容器到容器通訊**：同一網路上的容器可以使用容器名稱作為主機名稱輕鬆地相互通訊。

- **容器到主機通訊**：容器可以與主機系統的網路交互，反之亦然。

- **隔離**：網路提供隔離以防止容器互相干擾。

- **自訂配置**：可自訂網路以滿足特定的應用要求。

## Docker network 類型

### 1. Bride Network(default)
### 2. Host Network
### 3. Overlay Network
### 4. None Network
### 5. Custom Network
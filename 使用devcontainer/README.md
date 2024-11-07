# VS Code 擴充套件(deccontainer)

## 使麼是devcontainer
Visual Studio Code (VS Code) 中的 Dev Containers 提供了一種強大的方式，可使用 Docker 容器建立隔離且可重複的開發環境。

這表示您可以在不同的機器上擁有一致的開發設定，並輕鬆地與您的團隊分享。

### 主要優點:
- **隔離**： Dev Containers 可為每個專案建立獨立的環境，防止不同工具和版本之間發生衝突。  
- **可重複性**： 您可以定義專案所需的確切環境，確保每個人都使用相同的設定。  
- **可攜性**： Dev Containers 可以輕鬆共用，並在不同的機器上執行，讓協作和加入的新團隊成員更快容易參與協作。  
- **效率**： 您可以在不同的開發環境之間快速切換，而無需在本機上安裝或設定多種工具。

### 實際案例
1. [**單獨使用devcontainer**](./1.單獨使用devcontainer)
2. [**和Dockerfile整合**](2.devcontainer和Dockerfile)
3. [**和docker-compose整合**](3.devcontainer和docker-compose)
4. [**postgres server**](4.建立devcontainer和postgres)
5. [**mysql server**](5.建立devcontainer和mysql工作環境)

### devcontainer.json架構

#### 基本配置：
- **name**：VS Code 中的顯示名稱
- **image或build**：指定預先建置映像或自訂 Dockerfile

#### 容器設定:

- **runArgs** ：Docker 運行參數
- **mounts**：配置卷掛載
- **RemoteUser**：指定容器中的用戶

#### VS 程式碼整合：
- **customizations.vscode.extensions**：要安裝的 VS Code 擴充
- **customizations.vscode.settings**：要套用的 VS Code 設定

#### 開發特點：

- **features**：需要安裝的附加工具和功能
- **forwardPorts**：從容器轉送的端口
- **RemoteEnv**：環境變數

#### 容器建立流程腳本：

- **postCreateCommand**：建立容器後執行
- **initializeCommand**：在建立容器之前執行
- **onCreateCommand**：建立容器時執行
- **updateContentCommand**：更新容器時執行
- **postStartCommand**：容器啟動時運行

```
{
    // 1. initializeCommand (First)
    // Runs on host machine before container creation
    "initializeCommand": "./setup-host.sh",

    // 2. onCreateCommand (Second)
    // Runs inside container after creation but before VS Code connects
    "onCreateCommand": "echo 'Container created' && ./initial-setup.sh",

    // 3. updateContentCommand (Third)
    // Runs inside container when content changes or repository is cloned/updated
    "updateContentCommand": "if [ -f 'package.json' ]; then npm install; fi",

    // 4. postCreateCommand (Fourth)
    // Runs inside container after updateContentCommand
    "postCreateCommand": "npm install && npm run build",

    // 5. postStartCommand (Fifth)
    // Runs every time the container starts
    "postStartCommand": "npm run dev",

    // 6. postAttachCommand (Last)
    // Runs every time VS Code attaches to the container
    "postAttachCommand": "echo 'VS Code attached'",

    // Example of using compound commands
    "postCreateCommand": {
        "install": "npm install",
        "build": "npm run build",
        "setup": "chmod +x ./scripts/*.sh"
    }
}
```


```devcontainer.json
{
    // Name of the dev container displayed in VS Code
    "name": "Project Development Environment",

    // Base Docker image or Dockerfile configuration
    "image": "mcr.microsoft.com/devcontainers/base:ubuntu",  // Use pre-built image
    // Alternative: Use custom Dockerfile
    "build": {
        "dockerfile": "Dockerfile",
        "context": "..",
        "args": {
            "VARIANT": "16"
        }
    },

    // Container-specific settings
    "runArgs": [
        "--cap-add=SYS_PTRACE",
        "--security-opt", "seccomp=unconfined"
    ],

    // Mount points and volumes
    "mounts": [
        "source=${localEnv:HOME}/.ssh,target=/home/vscode/.ssh,type=bind,consistency=cached"
    ],

    // Container user settings
    "remoteUser": "vscode",

    // VS Code settings and extensions
    "customizations": {
        "vscode": {
            "extensions": [
                "dbaeumer.vscode-eslint",
                "esbenp.prettier-vscode"
            ],
            "settings": {
                "terminal.integrated.defaultProfile.linux": "bash",
                "editor.formatOnSave": true
            }
        }
    },

    // Features to install
    "features": {
        "docker-in-docker": "latest",
        "git": "latest",
        "github-cli": "latest"
    },

    // Commands to run after container is created
    "postCreateCommand": "npm install",

    // Port forwarding configuration
    "forwardPorts": [3000, 5432],

    // Environment variables
    "remoteEnv": {
        "NODE_ENV": "development"
    },

    // Lifecycle scripts
    "initializeCommand": "./setup.sh",
    "onCreateCommand": "echo 'Container created!'",
    "updateContentCommand": "npm install",
    "postStartCommand": "npm run dev"
}
```


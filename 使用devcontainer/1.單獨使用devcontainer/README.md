# 建立一般python開發環境

- debian bookworm作業系統
- python3.11
- 安裝git
- 容器名稱改為"python_chilhlee_api"
- 更新pip
- 安裝requirements.txt
- git初始化設定

以下是devcontainer.json內容說明

```json
// For format details, see https://aka.ms/devcontainer.json. For config options, see the
// README at: https://github.com/devcontainers/templates/tree/main/src/python
{
	"name": "Python 3",
	// Or use a Dockerfile or Docker Compose file. More info: https://containers.dev/guide/dockerfile
	"image": "mcr.microsoft.com/devcontainers/python:1-3.11-bookworm",
	"features": {
		"ghcr.io/devcontainers/features/git:1": {}
	},
	"runArgs":["--name","python_chilhlee_api"],

	// Features to add to the dev container. More info: https://containers.dev/features.
	// "features": {},

	// Use 'forwardPorts' to make a list of ports inside the container available locally.
	// "forwardPorts": [],

	// Use 'postCreateCommand' to run commands after the container is created.
	"postCreateCommand": "pip install --upgrade pip && pip3 install --user -r requirements.txt && git config --global user.name \"roberthsu2003\" && git config --global user.email \"roberthsu2003@gmail.com\"",

		
	

	// Configure tool-specific properties.
	"customizations": {
		"vscode": {
			"extensions": [
				"MS-CEINTL.vscode-language-pack-zh-hant",
				"ms-toolsai.jupyter",
				"ms-python.python"
			]
		}
	},

	// Uncomment to connect as root instead. More info: https://aka.ms/dev-containers-non-root.
	"remoteUser": "root"
}

```
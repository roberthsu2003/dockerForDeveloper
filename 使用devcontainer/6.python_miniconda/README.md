# python和minicoda環境

## 專案檔案架構

```
專案
	|requirements.txt------>optional
	|.devcontainer
		|devcontainer.json
		|Dockerfile
		|noop.txt				
```
  


## devcontainer建立的container有以下的設定
- 安裝miniconda(使用預設,不然conda行容易Permition Deny)
- 安裝git,github cli
- 容器名稱改為"python_langchain"
- 安裝vscode的套件-繁體中文套件,python開發套件,jupyter notebook開發套件

**devcontainer.json的內容**

```
// For format details, see https://aka.ms/devcontainer.json. For config options, see the
// README at: https://github.com/devcontainers/templates/tree/main/src/miniconda
{
	"name": "Miniconda (Python 3)",
	"build": { 
		"context": "..",
		"dockerfile": "Dockerfile"
	},
	"features": {
		"ghcr.io/devcontainers/features/git:1": {},
		"ghcr.io/devcontainers/features/github-cli:1":{}
	},
	//使用--newwork=host,代表直接使用host的網路
	"runArgs": ["--network=host","--name","python_langchain"],

	// Features to add to the dev container. More info: https://containers.dev/features.
	// "features": {},

	// Use 'forwardPorts' to make a list of ports inside the container available locally.
	// "forwardPorts": [],

	// Use 'postCreateCommand' to run commands after the container is created.
	// "postCreateCommand": "python --version",

	//安裝vscode的擴充套件,繁體中文,jupyter,python開發套件
	"customizations": {
		"vscode": {
			"extensions": [
				"MS-CEINTL.vscode-language-pack-zh-hant",
				"ms-toolsai.jupyter",
				"ms-python.python"
			]
		}
	}


	// Uncomment to connect as root instead. More info: https://aka.ms/dev-containers-non-root.
	// "remoteUser": "root"
}

```

**Dockerfile**

```
FROM mcr.microsoft.com/devcontainers/miniconda:1-3
```

**noop.txt**
```
可以是空的或任何內容
```
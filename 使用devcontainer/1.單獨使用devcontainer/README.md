# 建立一般python開發環境

## 執行devcontainer.json前的需求
- git init(從github下載後就已經有git init)
- 必需建立一個requirements.txt

## devcontainer建立的container有以下的設定
- debian bookworm作業系統
- python3.11
- 安裝git
- 容器名稱改為"python_chilhlee_api"
- 更新pip
- 安裝requirements.txt
- git初始化設定
- 安裝vscode的套件-繁體中文套件,python開發套件,jupyter notebook開發套件
- 使用者名稱改為root

以下是devcontainer.json內容說明

```json
//格式的詳細資訊，請參閱 https://aka.ms/devcontainer.json。有關設定選項，請參閱
// README，網址為：https://github.com/devcontainers/templates/tree/main/src/python
{
	//name是這個devcontainer.json的名字,不重要
	"name": "Python 3",
	//安裝debain bookworm,python3.11
	"image": "mcr.microsoft.com/devcontainers/python:1-3.11-bookworm",
	"features": {
		//系統要安裝git
		"ghcr.io/devcontainers/features/git:1": {}
	},
	//設定container名稱為python_chilhlee_api
	"runArgs":["--name","python_chilhlee_api"],
	
	//使用「forwardPorts」可使容器內的連接埠清單在本機可用。 
	// "forwardPorts": [],

	//使用「postCreateCommand」可在容器建立後執行指令。
	"postCreateCommand": "pip install --upgrade pip && pip3 install --user -r requirements.txt && git config --global user.name \"roberthsu2003\" && git config --global user.email \"roberthsu2003@gmail.com\"",


		
	

	//安裝VSCode套件
	"customizations": {
		"vscode": {
			"extensions": [
				"MS-CEINTL.vscode-language-pack-zh-hant",
				"ms-toolsai.jupyter",
				"ms-python.python"
			]
		}
	},

	//設定使用者為root,系統建議不要設為root,可以註解,使用內建的方式設定
	"remoteUser": "root"
}

```
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
- 安裝miniconda和自訂pythonp版本
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

# Copy environment.yml (if found) to a temp location so we update the environment. Also
# copy "noop.txt" so the COPY instruction does not fail if no environment.yml exists.
#COPY environment.yml* .devcontainer/noop.txt /tmp/conda-tmp/
#RUN if [ -f "/tmp/conda-tmp/environment.yml" ]; then umask 0002 && /opt/conda/bin/conda env update -n base -f /tmp/conda-tmp/environment.yml; fi \
#   && rm -rf /tmp/conda-tmp

#預設conda安裝的版本,安裝pipx,並把先前安裝的版本移除
RUN conda install -y python=3.11 \
    && pip install --no-cache-dir pipx \
    && pipx reinstall-all


#copy ../requirements.txt* 的所有檔案至容器的/tmp/pip-tmp/資料夾內,如果沒有../requirements.txt,就copy noop.txt至/tmp/pip-tmp 
COPY ../requirements.txt* .devcontainer/noop.txt /tmp/pip-tmp/

#if的語法是bash 語法:如果有這個檔,就安裝/tmp/pip-tmp/requirements.txt內的檔案,安裝完成後刪除/tmp/pip-tmp
RUN if [ -f "/tmp/pip-tmp/requirements.txt" ]; then \
        pip install -r /tmp/pip-tmp/requirements.txt; \
    fi \
    && rm -rf /tmp/pip-tmp

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

```

**noop.txt**
```
可以是空的或任何內容
```
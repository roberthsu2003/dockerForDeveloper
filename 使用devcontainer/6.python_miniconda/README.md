# python和minicoda環境

## 執行devcontainer.json前的需求
- git init(從github下載後就已經有git init)


## devcontainer建立的container有以下的設定
- 安裝miniconda和自訂pythonp版本
- 安裝git
- 容器名稱改為"python_chilhlee_api"
- 安裝vscode的套件-繁體中文套件,python開發套件,jupyter notebook開發套件

**devcontainer.json**

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
		"ghcr.io/devcontainers/features/git:1": {}
	},
	
	"runArgs":["--name","python_chilhlee_api"],
	
	// Use 'postCreateCommand' to run commands after the container is created.
	 "postCreateCommand": "pip install --upgrade pip && pip3 install --user -r requirements.txt",
	
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
COPY environment.yml* .devcontainer/noop.txt /tmp/conda-tmp/
RUN if [ -f "/tmp/conda-tmp/environment.yml" ]; then umask 0002 && /opt/conda/bin/conda env update -n base -f /tmp/conda-tmp/environment.yml; fi \
    && rm -rf /tmp/conda-tmp

# [Optional] Uncomment to install a different version of Python than the default
RUN conda install -y python=3.11

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

```

**noop.txt**
```
This file is copied into the container along with environment.yml* from the
parent folder. This is done to prevent the Dockerfile COPY instruction from 
failing if no environment.yml is found.
```
## miniconda_mongodb

**Dockerfile**

```
FROM mcr.microsoft.com/devcontainers/miniconda:1-3
```

**docker-compose.yml**

```
version: '3.8'

services:
  app:
    build:
      context: ..
      dockerfile: .devcontainer/Dockerfile
    
    volumes:
      - ../..:/workspaces:cached
    command: sleep infinity
    network_mode: service:mongo

  mongo:
    image: mongo
    restart: always
    volumes:
      - mongodb-data:/data/db
    ports:
      - 27017:27017


volumes:
  mongodb-data:

```

**devcontainer.json**

```
// For format details, see https://aka.ms/devcontainer.json. For config options, see the
// README at: https://github.com/devcontainers/templates/tree/main/src/miniconda
{
	"name": "Miniconda (Python 3)",
	"dockerComposeFile": "docker-compose.yml",
	"service": "app",
	"workspaceFolder": "/workspaces/${localWorkspaceFolderBasename}",
	"features": {
		"ghcr.io/devcontainers/features/git:1": {},
		"ghcr.io/devcontainers/features/github-cli:1":{}
	},
	
	"customizations": {
		"vscode": {
			"extensions": [
				"MS-CEINTL.vscode-language-pack-zh-hant",
				"ms-toolsai.jupyter",
				"ms-python.python"
			]
		}
	}	
}

```
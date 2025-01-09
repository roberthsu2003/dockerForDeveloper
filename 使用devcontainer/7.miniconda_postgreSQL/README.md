## miniconda_postgreSQL

### 先使用VSCode精靈建立
- 修改docker-compose.yml
- 增加posts:5432,如下範例的格式


```
version: '3.8'

services:
  app:
    build:
      context: ..
      dockerfile: .devcontainer/Dockerfile
    env_file:
        - .env

    volumes:
      - ../..:/workspaces:cached

    # Overrides default command so things don't shut down after the process ends.
    command: sleep infinity

    # Runs app on the same network as the database container, allows "forwardPorts" in devcontainer.json function.
    network_mode: service:db

    # Use "forwardPorts" in **devcontainer.json** to forward an app port locally.
    # (Adding the "ports" property to this file will not forward from a Codespace.)

  db:
    image: postgres:latest
    restart: unless-stopped
    volumes:
      - postgres-data:/var/lib/postgresql/data
    env_file:
      - .env
    ports:
      - 5432:5432

    # Add "forwardPorts": ["5432"] to **devcontainer.json** to forward PostgreSQL locally.
    # (Adding the "ports" property to this file will not forward from a Codespace.)

volumes:
  postgres-data:

```

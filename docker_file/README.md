# Dockerfile 介紹（Python 版）

Dockerfile 是一個用來自動建立 Docker 容器映像的文字檔。對於 Python 開發者來說，Dockerfile 可以幫助你快速建立一個乾淨、一致的 Python 執行環境，讓你的程式在任何電腦上都能順利執行。

## 為什麼要用 Dockerfile？

- 讓你的 Python 程式不會因為每台電腦環境不同而出錯。
- 可以快速分享、部署你的應用程式。
- 學會 Dockerfile，未來在團隊合作或上雲端都很有幫助。

## Dockerfile 的基本結構

Dockerfile 由一行一行的「指令」組成，每一行都在描述如何建立你的環境。

```dockerfile
# 這是註解
INSTRUCTION 參數
```

常見的指令有：

- **`FROM`**
  - **說明**：這是每個 Dockerfile 的第一行指令，用來指定你的新映像要基於哪個「基礎映像」來建立。你可以把它想像成蓋房子的地基。
  - **範例**：
    ```dockerfile
    # 使用官方 Python 3.11 的輕量版 (slim) 作為基礎
    FROM python:3.11-slim
    ```

- **`WORKDIR`**
  - **說明**：設定容器內的工作目錄。之後的 `RUN`、`CMD`、`COPY` 等指令都會在這個目錄下執行。如果目錄不存在，它會自動被建立。
  - **範例**：
    ```dockerfile
    # 設定容器內的工作目錄為 /app
    WORKDIR /app
    ```

- **`COPY`**
  - **說明**：將你電腦本機的檔案或資料夾，複製到容器的檔案系統裡面。
  - **範例**：
    ```dockerfile
    # 將本機的 requirements.txt 複製到容器的 /app 目錄下
    COPY requirements.txt .

    # 將本機的 src 資料夾內所有東西，複製到容器的 /app/src 目錄下
    COPY src/ ./src
    ```

- **`RUN`**
  - **說明**：在映像建立過程中執行指令，通常用來安裝套件或軟體。每執行一次 `RUN` 都會建立一個新的映像層 (layer)。
  - **範例**：
    ```dockerfile
    # 更新套件庫並安裝 git
    RUN apt-get update && apt-get install -y git

    # 使用 pip 安裝 Python 套件
    RUN pip install -r requirements.txt
    ```

- **`CMD`**
  - **說明**：設定當容器啟動時，預設要執行的指令。一個 Dockerfile 只能有一個 `CMD`。如果在 `docker run` 時指定了其他指令，`CMD` 的設定會被覆蓋。
  - **範例**：
    ```dockerfile
    # 設定容器啟動時，執行 python app.py
    CMD ["python", "app.py"]
    ```

- **`EXPOSE`**
  - **說明**：這是一個「聲明」或「文件」，告訴別人這個容器內的應用程式會使用哪個 port。它本身不會真的把 port 開放給外部存取，你還是需要在 `docker run` 時使用 `-p` 參數來對應 port。
  - **範例**：
    ```dockerfile
    # 聲明容器會使用 5000 port
    EXPOSE 5000
    ```

- **`ENV`**
  - **說明**：用來設定容器內的環境變數。這個變數可以在後續的指令（如 `RUN`）中使用，也可以被容器中執行的應用程式讀取。
  - **範例**：
    ```dockerfile
    # 設定一個名為 APP_VERSION 的環境變數
    ENV APP_VERSION=1.0
    ```

## Python Dockerfile 範例

假設你有一個簡單的 Python 程式 `hello.py`：

```python
print("Hello, Docker!")
```

你還有一個 `requirements.txt`（如果有用到第三方套件，這裡可以先放空）：

```
# 這裡可以列出你要安裝的 Python 套件，例如：
# requests
```

### 對應的 Dockerfile

```dockerfile
# 1. 選擇官方 Python 映像作為基礎
FROM python:3.11-slim

# 2. 設定工作目錄
WORKDIR /app

# 3. 複製需求檔與程式碼到映像中
COPY requirements.txt ./
COPY hello.py ./

# 4. 安裝 Python 套件（如果 requirements.txt 有內容）
RUN pip install --no-cache-dir -r requirements.txt

# 5. 設定容器啟動時執行的指令
CMD ["python", "hello.py"]
```

### 建立與執行步驟

1. 把上面的 `hello.py`、`requirements.txt` 和 `Dockerfile` 放在同一個資料夾。
2. 在該資料夾下打開終端機，執行：
   ```sh
   docker build -t my-python-app .
   ```
   這會建立一個名為 `my-python-app` 的映像。
3. 執行容器：
   ```sh
   docker run --rm my-python-app
   ```
   你會看到畫面輸出：
   ```
   Hello, Docker!
   ```

---

這樣就完成了最基本的 Python Dockerfile 教學！你可以把 `hello.py` 換成自己的 Python 程式，或在 `requirements.txt` 加上需要的套件。

---

## 更多實用範例

### 範例 1：基礎 Flask 網頁應用程式

假設你有一個簡單的 Flask 應用程式 `app.py`：

```python
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    # 這裡之後會接 LLM API
    response = f"你說：{user_message}，我收到了！"
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

建立 `templates/index.html`：
```html
<!DOCTYPE html>
<html>
<head>
    <title>我的 AI 聊天機器人</title>
    <meta charset="UTF-8">
</head>
<body>
    <h1>AI 聊天機器人</h1>
    <div id="chat-container">
        <div id="messages"></div>
        <input type="text" id="user-input" placeholder="輸入訊息...">
        <button onclick="sendMessage()">送出</button>
    </div>
    
    <script>
        function sendMessage() {
            const input = document.getElementById('user-input');
            const message = input.value;
            if (!message) return;
            
            fetch('/api/chat', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({message: message})
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('messages').innerHTML += 
                    `<p><strong>你：</strong>${message}</p>
                     <p><strong>AI：</strong>${data.response}</p>`;
                input.value = '';
            });
        }
    </script>
</body>
</html>
```

對應的 `requirements.txt`：
```
Flask==2.3.3
```

**Dockerfile：**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# 先複製 requirements.txt 並安裝套件（利用 Docker 快取機制）
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製應用程式碼和模板
COPY app.py .
COPY templates/ ./templates/

# 聲明使用的 port
EXPOSE 5000

# 啟動 Flask 應用程式
CMD ["python", "app.py"]
```

**執行方式：**
```sh
docker build -t my-chatbot .
docker run -p 5000:5000 my-chatbot
```
然後在瀏覽器開啟 `http://localhost:5000`

### 範例 2：整合 OpenAI API 的聊天機器人

假設你要建立一個真正能與 AI 對話的聊天機器人：

```python
# ai_chatbot.py
import os
import openai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 設定 OpenAI API Key（從環境變數讀取）
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/api/chat', methods=['POST'])
def chat_with_ai():
    try:
        user_message = request.json.get('message', '')
        
        if not user_message:
            return jsonify({'error': '請輸入訊息'}), 400
        
        # 呼叫 OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "你是一個友善的助手，請用繁體中文回答。"},
                {"role": "user", "content": user_message}
            ],
            max_tokens=150,
            temperature=0.7
        )
        
        ai_response = response.choices[0].message.content
        return jsonify({'response': ai_response})
        
    except Exception as e:
        return jsonify({'error': f'發生錯誤：{str(e)}'}), 500

@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy', 'service': 'AI Chatbot'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

建立 `templates/chat.html`：
```html
<!DOCTYPE html>
<html>
<head>
    <title>AI 聊天機器人</title>
    <meta charset="UTF-8">
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        #messages { height: 400px; border: 1px solid #ccc; padding: 10px; overflow-y: scroll; margin-bottom: 10px; }
        #user-input { width: 70%; padding: 10px; }
        button { padding: 10px 20px; }
        .user-msg { color: blue; }
        .ai-msg { color: green; }
        .error-msg { color: red; }
    </style>
</head>
<body>
    <h1>🤖 AI 聊天機器人</h1>
    <div id="messages"></div>
    <div>
        <input type="text" id="user-input" placeholder="輸入你的問題..." onkeypress="handleEnter(event)">
        <button onclick="sendMessage()">送出</button>
    </div>
    
    <script>
        function handleEnter(event) {
            if (event.key === 'Enter') {
                sendMessage();
            }
        }
        
        function sendMessage() {
            const input = document.getElementById('user-input');
            const message = input.value.trim();
            if (!message) return;
            
            // 顯示使用者訊息
            addMessage('你', message, 'user-msg');
            input.value = '';
            
            // 顯示載入中
            addMessage('AI', '思考中...', 'ai-msg');
            
            fetch('/api/chat', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({message: message})
            })
            .then(response => response.json())
            .then(data => {
                // 移除載入中訊息
                const messages = document.getElementById('messages');
                messages.removeChild(messages.lastChild);
                
                if (data.error) {
                    addMessage('系統', data.error, 'error-msg');
                } else {
                    addMessage('AI', data.response, 'ai-msg');
                }
            })
            .catch(error => {
                addMessage('系統', '連線錯誤，請稍後再試', 'error-msg');
            });
        }
        
        function addMessage(sender, message, className) {
            const messages = document.getElementById('messages');
            const messageDiv = document.createElement('div');
            messageDiv.innerHTML = `<strong class="${className}">${sender}：</strong>${message}`;
            messages.appendChild(messageDiv);
            messages.scrollTop = messages.scrollHeight;
        }
    </script>
</body>
</html>
```

`requirements.txt`：
```
Flask==2.3.3
openai==0.28.1
python-dotenv==1.0.0
```

**Dockerfile：**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# 複製需求檔案並安裝套件
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製應用程式碼
COPY ai_chatbot.py .
COPY templates/ ./templates/

# 設定環境變數（實際使用時請設定真實的 API Key）
ENV OPENAI_API_KEY=your_openai_api_key_here

EXPOSE 5000

CMD ["python", "ai_chatbot.py"]
```

**執行方式：**
```sh
# 建置映像
docker build -t ai-chatbot .

# 執行容器（記得替換成你的真實 API Key）
docker run -p 5000:5000 -e OPENAI_API_KEY=your_real_api_key ai-chatbot
```

### 範例 3：使用多種 LLM API 的智能助手

這個範例展示如何整合多個 LLM 服務（OpenAI、Anthropic Claude 等）：

```python
# smart_assistant.py
import os
import openai
import anthropic
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 設定 API Keys
openai.api_key = os.getenv('OPENAI_API_KEY')
claude_client = anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

@app.route('/')
def home():
    return render_template('assistant.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        model_choice = data.get('model', 'gpt-3.5-turbo')
        
        if not user_message:
            return jsonify({'error': '請輸入訊息'}), 400
        
        if model_choice.startswith('gpt'):
            response = call_openai(user_message, model_choice)
        elif model_choice.startswith('claude'):
            response = call_claude(user_message)
        else:
            return jsonify({'error': '不支援的模型'}), 400
            
        return jsonify({'response': response, 'model': model_choice})
        
    except Exception as e:
        return jsonify({'error': f'發生錯誤：{str(e)}'}), 500

def call_openai(message, model):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "你是一個專業的程式設計助手，請用繁體中文回答。"},
            {"role": "user", "content": message}
        ],
        max_tokens=300,
        temperature=0.7
    )
    return response.choices[0].message.content

def call_claude(message):
    response = claude_client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=300,
        messages=[
            {"role": "user", "content": f"請用繁體中文回答：{message}"}
        ]
    )
    return response.content[0].text

@app.route('/api/models')
def get_models():
    return jsonify({
        'models': [
            {'id': 'gpt-3.5-turbo', 'name': 'GPT-3.5 Turbo'},
            {'id': 'gpt-4', 'name': 'GPT-4'},
            {'id': 'claude-3-sonnet', 'name': 'Claude 3 Sonnet'}
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

建立 `templates/assistant.html`：
```html
<!DOCTYPE html>
<html>
<head>
    <title>智能程式設計助手</title>
    <meta charset="UTF-8">
    <style>
        body { font-family: Arial, sans-serif; max-width: 1000px; margin: 0 auto; padding: 20px; }
        .header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
        #model-select { padding: 8px; }
        #messages { height: 500px; border: 1px solid #ccc; padding: 15px; overflow-y: scroll; margin-bottom: 15px; background-color: #f9f9f9; }
        .input-area { display: flex; gap: 10px; }
        #user-input { flex: 1; padding: 12px; border: 1px solid #ccc; border-radius: 4px; }
        button { padding: 12px 20px; background-color: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background-color: #0056b3; }
        .message { margin-bottom: 15px; padding: 10px; border-radius: 8px; }
        .user-message { background-color: #e3f2fd; border-left: 4px solid #2196f3; }
        .ai-message { background-color: #f1f8e9; border-left: 4px solid #4caf50; }
        .error-message { background-color: #ffebee; border-left: 4px solid #f44336; }
        .model-tag { font-size: 12px; color: #666; margin-left: 10px; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🤖 智能程式設計助手</h1>
        <select id="model-select">
            <option value="gpt-3.5-turbo">GPT-3.5 Turbo</option>
            <option value="gpt-4">GPT-4</option>
            <option value="claude-3-sonnet">Claude 3 Sonnet</option>
        </select>
    </div>
    
    <div id="messages"></div>
    
    <div class="input-area">
        <input type="text" id="user-input" placeholder="詢問程式設計問題..." onkeypress="handleEnter(event)">
        <button onclick="sendMessage()">送出</button>
    </div>
    
    <script>
        function handleEnter(event) {
            if (event.key === 'Enter') {
                sendMessage();
            }
        }
        
        function sendMessage() {
            const input = document.getElementById('user-input');
            const modelSelect = document.getElementById('model-select');
            const message = input.value.trim();
            const selectedModel = modelSelect.value;
            
            if (!message) return;
            
            // 顯示使用者訊息
            addMessage('你', message, 'user-message');
            input.value = '';
            
            // 顯示載入中
            addMessage('AI', '思考中...', 'ai-message');
            
            fetch('/api/chat', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    message: message,
                    model: selectedModel
                })
            })
            .then(response => response.json())
            .then(data => {
                // 移除載入中訊息
                const messages = document.getElementById('messages');
                messages.removeChild(messages.lastChild);
                
                if (data.error) {
                    addMessage('系統', data.error, 'error-message');
                } else {
                    addMessage('AI', data.response, 'ai-message', data.model);
                }
            })
            .catch(error => {
                const messages = document.getElementById('messages');
                messages.removeChild(messages.lastChild);
                addMessage('系統', '連線錯誤，請稍後再試', 'error-message');
            });
        }
        
        function addMessage(sender, message, className, model = '') {
            const messages = document.getElementById('messages');
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${className}`;
            
            const modelTag = model ? `<span class="model-tag">[${model}]</span>` : '';
            messageDiv.innerHTML = `<strong>${sender}${modelTag}：</strong><br>${message.replace(/\n/g, '<br>')}`;
            
            messages.appendChild(messageDiv);
            messages.scrollTop = messages.scrollHeight;
        }
    </script>
</body>
</html>
```

`requirements.txt`：
```
Flask==2.3.3
openai==0.28.1
anthropic==0.3.11
python-dotenv==1.0.0
gunicorn==21.2.0
```

**Dockerfile：**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# 複製需求檔案並安裝套件
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製應用程式碼
COPY smart_assistant.py .
COPY templates/ ./templates/

# 設定環境變數
ENV OPENAI_API_KEY=your_openai_api_key
ENV ANTHROPIC_API_KEY=your_anthropic_api_key

EXPOSE 5000

# 生產環境使用 gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "smart_assistant:app"]
```

**執行方式：**
```sh
# 建置映像
docker build -t smart-assistant .

# 執行容器
docker run -p 5000:5000 \
  -e OPENAI_API_KEY=your_real_openai_key \
  -e ANTHROPIC_API_KEY=your_real_anthropic_key \
  smart-assistant
```

### 範例 4：開發環境 Dockerfile

適合開發時使用，包含開發工具：

**Dockerfile.dev：**
```dockerfile
# /Users/roberthsu2003/Documents/GitHub/dockerForDeveloper/docker_file/README.md

# 使用完整的 Python 3.11 映像。
# 相較於 -slim 版本，完整版包含更多編譯工具，
# 在安裝某些需要編譯的 Python 套件時比較不會出錯，適合開發。
FROM python:3.11

# 設定容器內的工作目錄為 /app。
# 後續的指令都會在這個目錄下執行。
WORKDIR /app

# 安裝開發時會用到的工具
# --upgrade pip 是好習慣，確保 pip 是最新版
RUN pip install --upgrade pip
# 安裝測試(pytest)、程式碼格式化(black)、程式碼風格檢查(flake8)、
# 型別檢查(mypy)、互動式筆記本(jupyter)等開發工具。
RUN pip install pytest black flake8 mypy jupyter

# 複製相依套件需求檔到容器中
# 這裡把 requirements.txt (正式環境) 和 requirements-dev.txt (開發環境) 都複製進去
COPY requirements.txt requirements-dev.txt ./
# 一次性安裝所有正式和開發用的套件
RUN pip install -r requirements.txt -r requirements-dev.txt

# 設定環境變數，讓 Flask 知道現在是開發模式
# FLASK_ENV=development 在較新版 Flask 已棄用，但 FLASK_DEBUG=1 仍有效，
# 會啟用除錯模式和自動重載功能。
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

# 聲明 /app 目錄為一個掛載點 (Volume)。
# 這是一個提示，告訴使用者這個目錄預期會從外部掛載進來。
# 在 `docker run` 指令中，我們用 `-v $(pwd):/app` 實現了這一點，
# 將本機的程式碼目錄直接對應到容器內的 /app 目錄。
# 這樣你在本機修改程式碼，容器內會立刻同步，非常方便。
VOLUME ["/app"]

# 聲明容器會用到的 port。
# 5000 通常給 Flask 應用程式，8888 給 Jupyter Notebook。
# 這只是一個文件聲明，實際的 port 映射還是要靠 `docker run -p`。
EXPOSE 5000 8888

# 設定容器啟動時的預設指令。
# 如上所述，啟動一個 bash shell，等待開發者進行互動操作。
CMD ["/bin/bash"]

```

**使用方式：**
```sh
# 建置開發映像
docker build -f Dockerfile.dev -t my-app-dev .

# 執行開發容器
docker run -it -v $(pwd):/app -p 5000:5000 -p 8888:8888 my-app-dev
```

---

## 最佳實踐建議

1. **利用快取機制**：先複製 `requirements.txt` 並安裝套件，再複製程式碼
2. **使用 .dockerignore**：排除不需要的檔案，減少建置時間
3. **多階段建置**：分離建置和執行環境，減少最終映像大小
4. **非 root 使用者**：提高安全性
5. **環境變數**：讓容器更有彈性
6. **健康檢查**：確保應用程式正常運作

**範例 .dockerignore：**
```
.git
.gitignore
README.md
Dockerfile
.dockerignore
node_modules
npm-debug.log
.coverage
.pytest_cache
__pycache__
*.pyc
*.pyo
*.pyd
.env
.venv
```

---

> 💡 **小提示**：選擇適合的基礎映像很重要！`python:3.11-slim` 比 `python:3.11` 小很多，但如果需要編譯套件，可能需要完整版本。

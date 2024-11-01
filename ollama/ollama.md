# 使用python操控ollama提供的api

```
import requests
import json

class OllamaAPI:
    def __init__(self, base_url="http://localhost:11434"):
        self.base_url = base_url

    def generate(self, model: str, prompt: str, options: dict = None) -> dict:
        """
        Generate a response using the specified model
        """
        url = f"{self.base_url}/api/generate"
        
        payload = {
            "model": model,
            "prompt": prompt
        }
        if options:
            payload.update(options)
            
        response = requests.post(url, json=payload, stream=True)
        
        for line in response.iter_lines():
            if line:
                yield json.loads(line)

    def chat(self, model: str, messages: list, options: dict = None) -> dict:
        """
        Have a conversation with the model
        """
        url = f"{self.base_url}/api/chat"
        
        payload = {
            "model": model,
            "messages": messages
        }
        if options:
            payload.update(options)
            
        response = requests.post(url, json=payload, stream=True)
        
        for line in response.iter_lines():
            if line:
                yield json.loads(line)

    def list_models(self) -> dict:
        """
        List all available models
        """
        url = f"{self.base_url}/api/tags"
        response = requests.get(url)
        return response.json()

# Example usage
if __name__ == "__main__":
    # Initialize the client
    client = OllamaAPI()
    
    # List available models
    models = client.list_models()
    print("Available models:", models)
    
    # Example of generating text
    prompt = "請使用python程式碼輸出一個hollo world的程式?"
    for response in client.generate("llama3.2:3b", prompt):
        if 'response' in response:
            print(response['response'], end='')
    print("\n")
    
    # Example of chat conversation
    messages = [
        {
            "role": "user",
            "content": "台灣目前的總統是?"
        }
    ]
    
    for response in client.chat("llama3.2:3b", messages):
        if 'message' in response:
            print(response['message']['content'], end='')
```
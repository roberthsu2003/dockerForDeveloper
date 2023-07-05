from fastapi import FastAPI
import redis

app = FastAPI()

r = redis.Redis(host='redis', port=6379)


@app.get("/")
def read_root():
    return {"Hello": "World123"}

@app.get("/hits")
def read_root1():
    r.incr('hits')
    return {"number of hits": r.get('hits')}


@app.get("/items/{item_id}")
def read_item(item_id:int, q:str | None = None):
    return {"item_id": item_id, "q": q}
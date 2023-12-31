from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {"Hello":"World"}

@app.get('/item/{item_id}')
def read_item(item_id: int , message: Union[str,None] = None):
    return {"item_id": item_id , "message":message}

if __name__ == "__main__":
    print("Application is up and running in container")
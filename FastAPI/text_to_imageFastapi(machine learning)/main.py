from fastapi import FastAPI
from pydantic import BaseModel
from ml import obtain_image
from fastapi.responses import FileResponse
app = FastAPI()


@app.get('/test')
def read_root():
    return {"hello":"test"}



@app.get('test/{item}')
def test_item(item:int):
    return {"item":item}


class Item(BaseModel):
    name:str
    price: float
    tags: list[str] = []

@app.post("/item")
def read_item(item:Item):
    return {"item":item}

@app.get('/generate/{prompt}')
def create_iamge(prompt:str):
    image = obtain_image(prompt)
    image.save('test.png')
    return FileResponse('test.png')

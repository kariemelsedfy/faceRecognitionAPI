from typing import Union

from fastapi import FastAPI

from api import register, recognize, stream, compareTwoImages

app = FastAPI()


app.include_router(register.router)
app.include_router(recognize.router)
app.include_router(stream.router)
app.include_router(compareTwoImages.router)
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
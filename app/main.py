from fastapi import FastAPI
import model
from config import engine
import router

model.Base.metadata.create_all(bind = engine)


app = FastAPI()

@app.get('/')
def home():
    return('Home')

app.include_router(router.router, prefix='/book', tags=['book'])

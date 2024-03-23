from fastapi import FastAPI

app=FastAPI()

@app.get('/')
async def root():
    return {'message': "FastAPI loyxamiz ishga tushdi"}
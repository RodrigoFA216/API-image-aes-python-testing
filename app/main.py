from fastapi import FastAPI
from app.routes.router import router

app = FastAPI()
app.include_router(router)


@app.get('/', status_code=200, response_description="Petición válida", tags=['Get', 'Hello world'])
def helloWorld():
    return {"message": "Hello"}

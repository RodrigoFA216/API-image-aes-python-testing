# Esta rama es backup para desplegar en multiples instancias
from fastapi import FastAPI
from app.routes.router import router

app = FastAPI()
app.include_router(router)
app.title = "API REST para Esteganografia y Cifrado"
app.version = "1.0.0"


@app.get('/', status_code=200, response_description="Petición válida", tags=['Get', 'Hello world'])
def helloWorld():
    return {"message": "Hello"}

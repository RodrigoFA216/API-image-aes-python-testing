from fastapi import FastAPI

app = FastAPI()


@app.get('/', status_code=200, response_description="Petición válida", tags=['Get', 'Hello world'])
def helloWorld():
    return {"message": "Hello"}

from fastapi import FastAPI
from src.example.main import hello
from src.lab import router as lab_router

app = FastAPI()
app.include_router(lab_router)


@app.get("/hello/{name}")
def read_hello(name: str):
    return {"message": hello(name)}


@app.get("/")
def root():
    return {"message": "Welcome to the Python Practice API!"}

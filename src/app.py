from fastapi import FastAPI
import gradio as gr

from src.example.main import hello
from src.lab.gradio_app import build_lab

app = FastAPI()


demo = build_lab()
app = gr.mount_gradio_app(app, demo, path="/lab")


@app.get("/hello/{name}")
def read_hello(name: str):
    return {"message": hello(name)}


@app.get("/")
def root():
    return {"message": "Welcome to the Python Practice API! Visit /lab for the UI."}

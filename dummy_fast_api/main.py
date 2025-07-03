from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from iss import get_router

class MainApp:
    def __init__(self):
        self.app = FastAPI()
        self.app.add_api_route("/", self.read_root, methods=["GET"], response_class=PlainTextResponse)
        self.app.include_router(get_router())

    def read_root(self):
        return "Hello World"

app = MainApp().app 
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.gzip import GZipMiddleware

app=FastAPI()
app.mount("/static",StaticFiles(directory="static"),name="static")
app.add_middleware(GZipMiddleware)

templates=Jinja2Templates(directory="templates")

@app.get("/")
async def index(request:Request):
    return templates.TemplateResponse("base.html",{"request":request})
from fastui import prebuilt_html
from flask import Flask

app = Flask(__name__)


@app.get("/robots.txt")
async def robots_txt() -> str:
    return "User-agent: *\nAllow: /"


@app.get("/favicon.ico")
async def favicon_ico() -> str:
    return "page not found"


@app.get("/<path:path>")
async def html_landing():
    return prebuilt_html(title="FastUI Demo")

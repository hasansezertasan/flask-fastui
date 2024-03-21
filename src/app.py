# Copyright 2024 Hasan Sezer Taşan <hasansezertasan@gmail.com>
# Copyright (C) 2024 <hasansezertasan@gmail.com>
from typing import List

from fastui import AnyComponent, prebuilt_html
from fastui.components import Heading, Navbar, Page, PageTitle, Paragraph
from fastui.events import GoToEvent
from flask import Flask

from src.render_response import render_response

app = Flask(__name__)


@app.get("/robots.txt")
def robots_txt() -> str:
    return "User-agent: *\nAllow: /"


@app.get("/favicon.ico")
def favicon_ico() -> str:
    return "page not found"


@app.get("/api/")
def page() -> List[AnyComponent]:
    response = [
        PageTitle(text="Title: Hello World!"),
        Navbar(
            title="Navbar Title: Hello World!",
            title_event=GoToEvent(url="/"),
        ),
        Page(
            components=[
                Heading(text="H1 Header: Hello World"),
                Paragraph(text="Paragraph: This is a simple demo of FastUI."),
            ],
        ),
    ]
    return render_response(response)


@app.get("/")
def html_landing() -> str:
    return prebuilt_html(title="FastUI Demo")

from fastui import AnyComponent, prebuilt_html
from fastui import components as c
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
def page() -> list[AnyComponent]:
	response = [
		c.PageTitle(text="Title: Hello World!"),
		c.Navbar(
			title="Navbar Title: Hello World!",
			title_event=GoToEvent(url="/"),
		),
		c.Page(
			components=[
				c.Heading(text="H1 Header: Hello World"),
				c.Paragraph(text="Paragraph: This is a simple demo of FastUI."),
			],
		),
	]
	return render_response(response)


@app.get("/")
def html_landing():
	return prebuilt_html(title="FastUI Demo")

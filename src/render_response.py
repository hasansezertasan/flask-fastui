from fastui import FastUI
from flask import jsonify


def render_response(response: list) -> str:
	return jsonify(FastUI(root=response).model_dump())

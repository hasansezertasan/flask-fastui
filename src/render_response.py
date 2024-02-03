from typing import List

from fastui import AnyComponent, FastUI
from flask import jsonify


def render_response(response: List[AnyComponent]) -> str:
	return jsonify(FastUI(root=response).model_dump())

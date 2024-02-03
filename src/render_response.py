from flask import jsonify
from fastui import FastUI

def render_response(response: list) -> str:
    return jsonify(FastUI(root=response).model_dump())

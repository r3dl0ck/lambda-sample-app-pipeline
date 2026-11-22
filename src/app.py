"""Prosta funkcja Lambda wdrazana przez pipeline z cwiczenia 4.4."""

import json
import os

VERSION = os.environ.get("APP_VERSION", "1.0.0")


def handler(event, context):
    path = event.get("rawPath", "/")
    if path == "/health":
        return _response(200, {"status": "ok", "version": VERSION})
    if path == "/":
        return _response(200, {"message": "Witaj z CodePipeline!", "version": VERSION})
    return _response(404, {"error": "Not found"})


def _response(status, body):
    return {
        "statusCode": status,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body),
    }

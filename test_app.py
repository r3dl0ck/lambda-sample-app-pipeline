"""Testy jednostkowe uruchamiane w fazie pre_build (buildspec.yml)."""

import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from app import handler  # noqa: E402


def _event(path):
    return {"rawPath": path}


def test_root_returns_200():
    response = handler(_event("/"), None)
    assert response["statusCode"] == 200
    assert "message" in json.loads(response["body"])


def test_health_returns_ok():
    response = handler(_event("/health"), None)
    assert response["statusCode"] == 200
    assert json.loads(response["body"])["status"] == "ok"


def test_unknown_path_returns_404():
    assert handler(_event("/nie-ma"), None)["statusCode"] == 404

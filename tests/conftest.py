from __future__ import annotations

import pytest

from wta.config import load_config
from wta.models import Item


@pytest.fixture
def config(tmp_path):
    """只有默认值的配置。"""
    return load_config(tmp_path / "missing.yaml")


@pytest.fixture
def make_item():
    def _make(title="Hello LLM", url="https://example.com/a", section="news", **kwargs) -> Item:
        kwargs.setdefault("source", "fake")
        kwargs.setdefault("via", "Fake")
        return Item(title=title, url=url, section=section, **kwargs)

    return _make

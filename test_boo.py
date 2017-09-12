"""Test Boo plugin."""

import pytest

from swak.plugin import DummyOutput
from swak.event_router import EventRouter


@pytest.fixture()
def def_output():
    """Create default output and returns it."""
    return DummyOutput()


def test_boo_basic(def_output):
    """Test basic features of Boo plugin."""
    pass
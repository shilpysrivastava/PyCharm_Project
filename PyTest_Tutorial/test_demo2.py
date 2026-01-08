import pytest


@pytest.mark.xfail(reason="this is a xfail test case")
def test_add():
    assert 5+2==10
import pytest


def test_compare():
    assert 5==5

@pytest.mark.smoke
def test_string():
    assert "hello" in "hello I m selenium"

def test_list():
    assert [1,2,3]==[1,2,3]
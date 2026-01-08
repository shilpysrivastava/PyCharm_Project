'''Markers basically used to add tags or catgories test case
markers as tags/labels attach to test case so that we can select, skip, or control how they run.
'''
import pytest

@pytest.mark.smoke
def test_login():
    print("This is login test case")

@pytest.mark.regression
def test_logout():
    print("This is logout test case")

def test_addtocart():
    print("This is addtocart test case")

'''Multiple markers on one test'''

@pytest.mark.smoke
@pytest.mark.regression
def test_payment():
    print("This is payment test case")

'''build-in markers'''

@pytest.mark.skip(reason="this is a skip test case")
def test_build():
    print("This is build test case")


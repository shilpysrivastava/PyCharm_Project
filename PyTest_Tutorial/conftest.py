'''declare fixture here when we want to share fixture globally'''
''''
| Scope                | Runs              |
| -------------------- | ----------------- |
| `function` (default) | Every test        |
| `class`              | Once per class    |
| `module`             | Once per file     |
| package              | Once per package  |
| `session`            | Once per test run | '''''


import pytest


@pytest.fixture(scope="class")
def setup():
    print("This is setup fixture, I will run first")
    yield
    print("This is teardown  fixture, I will run at the end ")


@pytest.fixture(scope="module")
def setup_module():
    print("\nSetup module")
    yield
    print("Teardown module")


#Parametrized fixtures
@pytest.fixture(params=["function", "class", "module", "package", "session"])
def data_load(request):
    return request.param

#Multiple Values
@pytest.fixture(params=[(2,3,5),(20,6,7),(9,8,6)])
def add(request):
    return request.param

@pytest.fixture(params=[("jose","jose@1"),"admin","password",("guest : guest123")])
def load_data(request):
    return request.param
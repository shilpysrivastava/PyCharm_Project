''''
| Scope                | Runs              |
| -------------------- | ----------------- |
| `function` (default) | Every test        |
| `class`              | Once per class    |
| `module`             | Once per file     |
| `session`            | Once per test run | '''''
import pytest

@pytest.mark.usefixtures("setup")
class Test_Scope:

    def test_db(self):
        print("This is db test case")

    def test_session(self):
        print("This is session test case")

    def test_function(self):
        print("This is function test case")

    def test_class(self):
        print("This is class test case")
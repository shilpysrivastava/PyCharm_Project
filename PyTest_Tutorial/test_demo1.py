'''Different command for running test cases from terminal
pytest -> for running all test cases
pytest -v`-> verbose output  shows meta data
pytest -q`-> quiet mode  Don't shows extra details like directory , plugins
pytest -x`->  stop on first failure
pytest --maxfail=2 -> stop after 2 failures
pytest -k -> run testcase with the matching test case name
'''
def test_example():
    print("This the test example of Pytest")
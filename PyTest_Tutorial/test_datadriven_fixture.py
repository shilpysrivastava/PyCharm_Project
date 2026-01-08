''''Run the same test multiple times with different input data.
Pytest fixtures support a params argument that lets you pass multiple data sets.
'''''

#Simple Data-Driven Fixture
def test_edit_profile(data_load):
    print(data_load)

#Multiple Values (Tuple Data)
def test_load_multipleValue(add):
    a,b,c = add
    sum = a+b+c
    print(sum)

def test_load_multipleValue2(load_data):
    print(load_data[0])
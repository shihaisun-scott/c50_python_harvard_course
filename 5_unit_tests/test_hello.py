from hello import hello

def test_hello():
    assert hello("Appa") == "hello, Appa"

def test_default():
    assert hello() == "hello, world"

# can also make a test of folders
# create folder mkdir test
# create test script code test\test_hello.py
# code test\__init__.py 
# this treats the folder as a package
# pytest test will search through the whole folder and do tests
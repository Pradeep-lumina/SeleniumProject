import pytest

@pytest.fixture()
def setup():
    print("Once every test method")

def testMethod1(setup):
    print("This is method1")


def testMethod2(setup):
    print("This is method2")
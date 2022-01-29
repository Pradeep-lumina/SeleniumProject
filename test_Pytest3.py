import pytest

@pytest.fixture()
def setup():
    print("Once every before test method")
    yield
    print("Once every after test method")

def testMethod1(setup):
    print("This is method1")


def testMethod2(setup):
    print("This is method2")
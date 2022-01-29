import pytest

@pytest.fixture()
def setup():
    print("Once every before test method")
    yield
    print("Once every after test method")

def testMethod3(setup):
    print("This is method3")


def testMethod4(setup):
    print("This is method4")
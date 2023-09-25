import pytest

@pytest.fixture()
def setup():
    print("Inside Setup Field")
    print("BEFORE THE EXECUTION OF TEST CASES")
    yield
    print("**************************")
    print("Inside Function but after Yield")

def test_addition(setup):
    print("Inside Addition Function")


def test_substraction(setup):
    print("Inside Substraction Method")




from Src import arithmetic_functions as AF
import pytest
import platform


# @pytest.mark.Akshay
# def test_addition():
#     assert AF.addition(2, 5) == 7
#
# @pytest.mark.Akshay
# @pytest.mark.Nawale
# def test_substraction():
#     assert AF.substraction(5, 1)==4
#
# @pytest.mark.Ajay
# @pytest.mark.Jannat
# def test_division():
#     assert AF.division(4,2)==2
#
#
# @pytest.mark.Akshay
# @pytest.mark.kapil
# def test_multiplication():
#     assert AF.multiplication(4,2)==8


@pytest.mark.One
@pytest.mark.Sanity
def test_addition():
    assert AF.addition(2, 3) == 5


@pytest.mark.One
@pytest.mark.Sanity
def test_subtraction():
    assert AF.subtraction(3, 2) == 1


@pytest.mark.One
@pytest.mark.Sanity
def test_multiplication():
    assert AF.multiplication(3, 2) == 6


@pytest.mark.One
@pytest.mark.Sanity
def test_division():
    assert AF.division(4, 2) == 2


@pytest.mark.skip
def test_square():
    assert AF.square(3) == 9





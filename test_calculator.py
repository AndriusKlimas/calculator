from calculator import add
from calculator import subtract
from calculator import devide
import pytest

def test_devide():
    assert 2 == devide(6,3)
    assert 5 == devide(25,5)
    assert 1 == devide(2,2)
    assert 10 == devide(10,1)
    assert 3 == devide(9,3)
    assert -1 == devide(0,0)
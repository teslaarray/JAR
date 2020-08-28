from calculator import *
import math as mt
import pytest



@pytest.mark.parametrize ("a, b, c", [ [1, 2, 3], [3, 5, 8],
    [7, 6, 13]])
def test_add(a, b, c):
    assert add(a, b)==c

@pytest.mark.parametrize ("a, b, c", [ [.1, .2, .3], [.3, .5, .8],
    [.7, .6, 1.3]])
def test_addfloat(a, b, c):
    assert abs(add(a, b)-c)<1e-12

@pytest.mark.parametrize ("a, b, c", [
    ["One", "Two", "OneTwo"],
    ["Three", "Four", "ThreeFour"]
])
def test_addstr(a, b, c):
    assert add(a, b)==c

@pytest.mark.parametrize ("a, b", [
    [3, 6],
    [4, 24],
    [5, 120]
])
def test_factorial(a, b):
    assert factorial(a) == b

@pytest.mark.parametrize ("a, b", [
    [0, 0],
    [mt.pi/2, 1],
    [mt.pi, 0]
])
def test_sin(a, b):
    assert abs(sin(a, 40)-b) < 1e-5

@pytest.mark.parametrize ("a, b", [
    [0, 1],
    [mt.pi/2, 0],
    [mt.pi, -1]
])
def test_cos(a, b):
    assert abs(cos(a, 40)-b) < 1e-5

@pytest.mark.parametrize ("a, b", [
    [0, 0],
    [mt.pi/4, 1],
])
def test_tan(a, b):
    assert abs(tan(a, 40)-b) < 1e-5

@pytest.mark.parametrize ("a, b, c", [
    [6, 2, 3],
    [18, 3, 6],
    [1, 1, 1]
])
def test_divide(a, b, c):
    assert divide(a, b)==c

import pytest

def test_addTypeError():
    with pytest.raises(TypeError):
        add("LELEL", 5)

def test_zeroDiv():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

import sys
from pathlib import Path 
import math
import pytest

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import (
    add, subtract, multiply, divide, sqrt, square, logarithm, sin, cosine, percentage, power
)

def test_add1():
    assert add(5 , 6) == 11

def test_add2():
    assert add(5, 6) != 10

def test_add3():
    assert add(5, -3) == 2

def test_add4():
    assert add(-5, -3) == -8
    
def test_add5():
    assert add(5, -3) == 2
    
def test_add6():
    assert add(5, 0) == 5
    
def test_add7():
    assert add(2.5, 3.5) == 6.0
    
def test_subtract1():
    assert subtract(10, 3) == 7
    
def test_subtract2():
    assert subtract(-5, -3) == -2
    
def test_subtract3():
    assert subtract(5, -3) == 8
    
def test_subtract4():
    assert subtract(5, 0) == 5
    
def test_subtract5():
    assert subtract(5.5, 2.5) == 3.0
    
def test_multiply1():
    assert multiply(4, 5) == 20
    
def test_multiply2():
    assert multiply(-4, -5) == 20
    
def test_multiply3():
    assert multiply(4, -5) == -20
    
def test_multiply4():
    assert multiply(5, 0) == 0
    
def test_multiply5():
    assert multiply(2.5, 4.0) == 10.0
    
def test_divide1():
    assert divide(10, 2) == 5.0
    
def test_divide2():
    assert divide(-10, -2) == 5.0
    
def test_divide3():
    assert divide(10, -2) == -5.0
    
def test_divide4():
    assert divide(10.0, 2.5) == 4.0
    
def test_divide5():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)
    
def test_divide6():
    assert divide(0, 5) == 0.0

def test_square1():
    assert square(5) == 25
    
def test_square2():
    assert square(-5) == 25
    
def test_square3():
    assert square(0) == 0
    
def test_square4():
    assert square(2.5) == 6.25
    
def test_square_root1():
    assert square_root(16) == 4.0
    
def test_square_root2():
    assert square_root(0) == 0.0
    
def test_square_root3():
    assert abs(square_root(2) - math.sqrt(2)) < 1e-9
    
def test_square_root4():
    assert square_root(1) == 1.0
    
def test_square_root5():
    with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
            square_root(-5)
    
def test_logarithm1():
    assert logarithm(100, 10) == 2.0
    
def test_logarithm2():
    assert abs(logarithm(math.e, math.e) - 1.0) < 1e-9
    
def test_logarithm3():
    assert logarithm(8, 2) == 3.0
    
def test_logarithm4():
    assert logarithm(1, 10) == 0.0
    
def test_logarithm5():
    with pytest.raises(ValueError, match="Logarithm argument must be positive"):
            logarithm(-5, 10)
    
def test_logarithm6():
    with pytest.raises(ValueError, match="Logarithm argument must be positive"):
            logarithm(0, 10)
    
def test_logarithm7():
    with pytest.raises(ValueError, match="Logarithm base must be positive"):
            logarithm(10, -2)
    
def test_logarithm8():
    with pytest.raises(ValueError, match="Logarithm base must be positive"):
            logarithm(10, 0)
    
def test_logarithm9():
    with pytest.raises(ValueError, match="Logarithm base cannot be 1"):
            logarithm(10, 1)
    
def test_sine1():
    assert sine(0) == 0.0
    
def test_sine2():
    assert abs(sine(math.pi / 2) - 1.0) < 1e-9
    
def test_sine3():
    assert abs(sine(math.pi)) < 1e-9
    
def test_sine4():
    assert abs(sine(-math.pi / 2) - (-1.0)) < 1e-9
    
def test_cosine1():
    assert cosine(0) == 1.0
    
def test_cosine2():
    assert abs(cosine(math.pi / 2)) < 1e-9
    
def test_cosine3():
    assert abs(cosine(math.pi) - (-1.0)) < 1e-9
    
def test_cosine4():
    assert abs(cosine(-math.pi) - (-1.0)) < 1e-9
    
def test_percentage1():
    assert percentage(100, 50) == 50.0
    
def test_percentage2():
    assert percentage(0, 50) == 0.0
    
def test_percentage3():
    assert percentage(100, 0) == 0.0
    
def test_percentage4():
    assert percentage(-100, 50) == -50.0
    
def test_percentage5():
    assert percentage(100, -25) == -25.0
    
def test_percentage6():
    assert abs(percentage(50.5, 20) - 10.1) < 1e-9
    
def test_power1():
    assert power(2, 3) == 8
    
def test_power2():
    assert power(5, 0) == 1
    
def test_power3():
    assert power(2, -2) == 0.25
    
def test_power4():
    assert abs(power(4, 0.5) - 2.0) < 1e-9
    
def test_power5():
    assert power(0, 5) == 0
    
def test_power6():
    assert power(-2, 3) == -8

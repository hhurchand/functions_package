"""Module to test quadratics

"""

import sys
import os

# Get the current directory (where this script is located)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Append the parent directory (project root) to sys.path
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


from src.quadratics import Quadratics #Pylint : disable=C0413
import pytest #Pylint:disable:C0413

@pytest.fixture
def data_negative():
    """Test data

    Returns:
        Tuple : Coefficients for a negative discriminant
    """
    return (1,5,8)

@pytest.fixture
def data_positive():
    """Test data

    Returns:
       tuple which leads to a positive discriminant
    """
    yield (1,5,-8)

def test_discriminant_zero() -> float:
    """Test zero discriminant
    """
    quad = Quadratics(1,-2,1)
    assert quad.discriminant() == 0

def test_discriminant_negative(data_negative) -> float:
    """Test negative discriminant
    """

    quad = Quadratics(*data_negative)
    assert quad.discriminant() < 0

def test_discriminant_positive(data_positive) -> float:
    """Test positive discriminant
    """
    quad = Quadratics(*data_positive)
    assert quad.discriminant() > 0
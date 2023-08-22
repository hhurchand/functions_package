"""This module provides a class for quadratic expressions and functions

Classes:
    Quadratics: Represents a quadratic, with coefficients

Example usage:
    # Create a quadratic object
    quadratic = Quadratics(5,7,8)
"""


class Quadratics:
    """Calculate property indicators of a quadratic expression.

    Given the coefficients of a quadratic expression, this class perform
    key caulculations, which are indicative of properties of the quadratic
    eg. discriminant, nature of roots


    Attributes:
    coeff_x2 (float): coeffiecient of x^2
    coeff_x1 (float): coefficient of x
    constant: constant term

    Methods:
    discriminant: Returns the discriminant of the quadratic expression
    """
    def __init__(self, coeff_x2: float, coeff_x: float, constant: float):
        self.coeff_x2 = coeff_x2
        self.coeff_x = coeff_x
        self.constant = constant

    def __repr__(self):
        return f"Class {self.__class__.__name__}\
                    calcuates discriminant of a quadratic"

    def discriminant(self) -> float:
        """Calculate discriminant of quadratic.

        Returns:
        Discriminant (float): Calculates the discriminat of the quadratic

        """
        return self.coeff_x2*self.coeff_x2 - 4*self.coeff_x2*self.constant

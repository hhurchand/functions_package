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
        self.a = coeff_x2
        self.b = coeff_x
        self.c = constant

    def __repr__(self):
        return f"Class {self.__class__.__name__}\
                    calcuates discriminant of a quadratic"

    def discriminant(self) -> float:
        """Calculate discriminant of quadratic.

        Returns:
        Discriminant (float): Calculates the discriminat of the quadratic

        """
        return self.b*self.b - 4*self.a*self.c

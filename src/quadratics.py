class Quadratics:
    def __init__(self,coeff_x2: float,coeff_x:float,constant:float):
        self.a = coeff_x2
        self.b = coeff_x
        self.c = constant
    
    def __repr__(self):
        return f"Class {self.__class__.__name__} calcuates discriminant of a quadratic"

    def discriminant(self)-> float:
        """Calculate discriminant of quadratic
        
        Returns:
        Discriminant : Float

        """
        return self.b*self.b - 4*self.a*self.c
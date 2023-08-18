class Quadratics:
    def __init__(self,coeff_x2: float,coeff_x:float,constant:float):
        self.a = coeff_x2
        self.b = coeff_x
        self.c = constant
    
    def discriminant(self)-> float:
        """Calculate discriminant of quadratic
        
        Returns:
        Discrimant : Float

        """
        return self.b*self.b - 4*self.a*self.c
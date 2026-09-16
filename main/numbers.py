class Number:
    def __init__(self, sign, magnitude):
        self.magnitude = str(magnitude)
        self.iszero = self.magnitude == "0"
        self.isone = self.magnitude == "1"
        self.isneg = sign == "-"

    def neg(self):
        return Number("-" if not self.isneg else "+", self.magnitude)

    def copy(self):
        return Number("-" if self.isneg else "+", self.magnitude)

    def add(self, other):
        if other.iszero:
            return self.copy()
        elif self.iszero:
            return other.copy()
        elif other.isneg:
            return self.sub(other.neg())
        elif self.isneg:
            return other.sub(self.neg())
        else:
            pass # TODO: make it actually add.

    def sub(self, other):
        if other.iszero:
            return self.copy
        elif self.iszero:
            return other.copy
        elif other.isneg:
            return self.add(other.neg())
        elif self.isneg:
            return (self.add(other)).neg()
        else:
            pass # TODO: make it subtract

    def mul(self, other):
        pass # TODO: Multiplication

    def div(self, other):
        pass # TODO: Division


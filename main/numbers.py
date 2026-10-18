class Number:
    '''This class defines a single number. 
    whole and fractional are strings, the '.' in a number or any radix point is ommited.
    sign is Either True for positive or False for negative.'''
    def __init__(self, whole, fractional, sign=True):
        self.whole = whole
        self.fractional = fractional
        self.sign = sign

    # TODO: Add logic for numbers

    def __add__(self, other):
        pass

    def __sub__(self,other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __neg__(self):
        return Number(self.whole, self.fractional, not self.sign)


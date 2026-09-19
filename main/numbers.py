class Number:
    def __init__(self, magnitude, sign=False):
        self.magnitude = str(magnitude)
        self.iszero = self.magnitude == "0"
        self.isone = self.magnitude == "1"
        if isinstance(sign, bool):
            self.isneg = sign
        else:
            self.isneg = sign == "-"

    def neg(self):
        return Number(self.magnitude, self.isneg) 

    def copy(self):
        return Number(self.magnitude, self.isneg)

    def gt(self, other):
        if self.isneg and not other.isneg:
            return False
        elif not self.isneg and other.isneg:
            return True
        else:
            if self.isneg:
                if len(self.magnitude) > len(other.magnitude):
                    return False
                elif len(self.magnitude) < len(other.magnitude):
                    return True
                else:
                    pass # TODO: make this work

    def lt(self, other):
        return not self.gt(other)

    def add(self, other):
        table = [[x + y for x in range(10)] for y in range(10)]
        if other.iszero:
            return self.copy()
        elif self.iszero:
            return other.copy()
        elif other.isneg:
            return self.sub(other.neg())
        elif self.isneg:
            return other.sub(self.neg())
        else:
            a = self.magnitude
            b = self.magnitude
            digs_in_out = max(len(a), len(b)) + 1
            o = " " * digs_in_out
            c = " " * digs_in_out
            a = "0" * (digs_in_out - len(a)) + a
            a.reverse()
            b = "0" * (digs_in_out - len(b)) + b
            b.reverse()
            for didx in range(digs_in_out):
                da = a[didx]
                db = b[didx]
                do, dc = list(str(table[int(da)][int(db])))
                o[didx] = do
                c[didx] = dc
            o.reverse()
            c.reverse()
            if c == "0" * digs_in_out:
                return Number(o)
            else:
                c = Number(c)
                o = Number(o)
                return o.add(c)

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


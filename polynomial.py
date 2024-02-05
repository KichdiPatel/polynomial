class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

    def evaluate(self, x):
        return x


class Int:
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return str(self.i)

    def evaluate(self, x):
        return self.i


class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

    def evaluate(self, x):
        return self.p1.evaluate(x) + self.p2.evaluate(x)


class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, (Add, Div, Sub)):
            if isinstance(self.p2, (Add, Div, Sub)):
                return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, (Add, Div, Sub)):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)

    def evaluate(self, x):
        return self.p1.evaluate(x) * self.p2.evaluate(x)


class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, (Add, Mul, Sub, Div)):
            if isinstance(self.p2, (Add, Mul, Sub, Div)):
                return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) / " + repr(self.p2)
        if isinstance(self.p2, (Add, Mul, Sub, Div)):
            return repr(self.p1) + " / ( " + repr(self.p2) + " )"
        return repr(self.p1) + " / " + repr(self.p2)

    def evaluate(self, x):
        return self.p1.evaluate(x) / self.p2.evaluate(x)


class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " - " + repr(self.p2)

    def evaluate(self, x):
        return self.p1.evaluate(x) - self.p2.evaluate(x)


# 4 + 3 + X + 1 * ( X * X + 1 )
poly = Add(Add(Int(4), Int(3)), Add(X(), Mul(Int(1), Add(Mul(X(), X()), Int(1)))))

# ( 4 + X ) / ( ( 3 + X ) * 2 - 1 / X )
poly2 = Div(Add(Int(4), X()), Sub(Mul(Add(3, X()), Int(2)), Div(Int(1), X())))


print(poly)
print(poly.evaluate(-1))

def size(e):
    if type(e) is binary_expr:
        return 1 + size(e.lhs) + size(e.rhs)
    if type(e) is not_expr:
        return 1 + size(e.expr)
    if type(e) is val:
        return 1

def height(e):
    if type(e) is binary_expr:
        lhs = height(e.lhs)
        rhs = height(e.rhs)
        if lhs > rhs:
            return 1 + lhs
        return 1 + rhs
    if type(e) is not_expr:
        return 1 + height(e.expr)
    if type(e) is val:
        return 1

def same():
    pass

def value():
    pass

def step():
    pass

def step_reduce():
    pass

class expr():
    def __init__(self):
        pass

class binary_expr(expr):
    def __init__(self, lhs, rhs):
        assert(isinstance(lhs, expr))
        assert(isinstance(rhs, expr))
        self.lhs = lhs
        self.rhs = rhs

class not_expr(expr):
    def __init__(self, e):
        assert(isinstance(e, expr))
        self.expr = e

class val(expr):
    def __init__(self, val):
        assert(val is True or val is False)
        self.val = val

if __name__ == '__main__':
    print('Running, boss!')
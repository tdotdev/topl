def size(e):
    if type(e) == binary_expr:
        return 1 + size(e.lhs) + size(e.rhs)
    if type(e) == not_expr:
        return 1 + size(e.expr)
    if type(e) == val:
        return 1

def height(e):
    if type(e) == binary_expr:
        lhs = height(e.lhs)
        rhs = height(e.rhs)
        if lhs > rhs:
            return 1 + lhs
        return 1 + rhs
    if type(e) == not_expr:
        return 1 + height(e.expr)
    if type(e) == val:
        return 1

def same():
    pass

def value(e):
    if type(e) == binary_expr:
        return value(e.lhs) and value(e.rhs)
    if type(e) == not_expr:
        return not value(e.expr)
    if type(e) == val:
        return e.val

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
        assert(val == True or val == False)
        self.val = val

if __name__ == '__main__':
    print('Running, boss!')
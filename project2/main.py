
def size():
    pass

def height():
    pass

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

class val(expr):
    def __init(self, val):
        assert(val is True or val is False)
        self.val = val

if __name__ == '__main__':
    print('Running, boss!')
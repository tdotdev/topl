from enum import Enum, auto


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
        if e.op == logical_op._or:
            return value(e.lhs) or value(e.rhs)
        elif e.op == logical_op._and:
            return value(e.lhs) and value(e.rhs)
    if type(e) == not_expr:
        return not value(e.expr)
    if type(e) == val:
        return e.val

def get_children(e):
    if type(e) is binary_expr:
        return [e.lhs, e.rhs]
    if type(e) is not_expr:
        return [e.expr]
    if type(e) is value:
        return [e.val]
    return []
    ## for serialize tree

def serialize_tree(tree):
    children = get_children(tree)
    for node in children:  
        print(serialize_tree(node))
    print([tree])

def step(expr):
    z = serialize_tree(expr)
    print(z)
    return 2
    """
    e = expr
    stack = Stack()
    children = list_iterator(get_children(e))

    while children.current() != None or stack.empty() != False:
        while children.current() != None:
            stack.push(children.current())
            children.next()

        children = list_iterator(get_children(stack.top()))

        print(children.current())
        children.next()
    
    return e
    """



def step_reduce():
    pass

class list_iterator():
    def __init__(self, vals):
        if type(vals) is not list:
            vals = [vals]
        self._list = vals + [None]
        self._current = self._list[0]
        self.index = 0

    def current(self):
        assert(self.index <= len(self._list))
        return self._current

    def next(self):
        self.index += 1
        self._current = self._list[self.index]

    def list(self):
        return self._list[:-1]

class Queue():
    def __init__(self, vals=[]):
        self._list = list(vals)

    def queue(self, val):
        val = list(val)
        for v in val:
            self._list.append(v)
    
    def dequeue(self, val):
        return self._list.pop(0)

class Stack():
    def __init__(self, vals=[]):
        self._list = list(vals)
        self._top = None

    def push(self, val):
        self._list.append(val)
        self._top = self._list[-1]

    def pop(self):
        assert(len(self._list) != 0)
        return self._list.pop()

    def top(self):
        assert(len(self._list) > 0)
        return self._top

    def empty(self):
        if len(self._list) == 0:
            return True
        return False
    
class logical_op(Enum):
    _or = auto()
    _and = auto()
    @classmethod
    def to_string(cls, val):
        if val == logical_op._or:
            return 'OR'
        elif val == logical_op._and:
            return 'AND'
        raise ValueError

class expr():
    def __init__(self):
        pass
    def to_string(self):
        raise NotImplementedError

class binary_expr(expr):
    # op given default argument of logical and so I don't have to 
    # retroactively add an operator to all of my test cases :D
    def __init__(self, lhs, rhs, op=logical_op._and):
        assert(isinstance(lhs, expr))
        assert(isinstance(rhs, expr))
        self.lhs = lhs
        self.rhs = rhs
        self.op = op

    def to_string(self):
        return f"{self.lhs.to_string()} {logical_op.to_string(self.op)} {self.rhs.to_string()}"

class not_expr(expr):
    def __init__(self, e):
        assert(isinstance(e, expr))
        self.expr = e
    
    def to_string(self):
        return f"NOT {self.expr.to_string()}"

class val(expr):
    def __init__(self, val):
        assert(val == True or val == False)
        self.val = val

    def to_string(self):
        return f"{self.val}"

if __name__ == '__main__':

    
    e = binary_expr(
        not_expr(val(False)),
        binary_expr(
            val(False),
            val(True)
        )
    )

    print(e.to_string())
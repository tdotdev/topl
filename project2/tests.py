from expr import *

expr1 = not_expr(not_expr(not_expr(val(False))))
assert(value(expr1) is True)

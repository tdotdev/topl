from expr import *

expr0 = binary_expr(
    not_expr(
        not_expr(
            not_expr(
                not_expr(
                    val(False)
                )
            )
        )
    ), 
    not_expr(
        not_expr(
            not_expr(
                not_expr(
                    not_expr(
                        val(False)
                    )
                )
            )
        )
    )
)
assert(height(expr0) == 7)
assert(value(expr0) == False)
assert(step_reduce(expr0).val == False)

expr1 = binary_expr(
    binary_expr(
        not_expr(
            not_expr(
                val(True)
            )
        ),
        not_expr(
            not_expr(
                val(True)
            )
        )
    ),
    binary_expr(
        val(True),
        val(False),
        logical_op._or
    )
)
assert(size(expr1) == 11)
assert(value(expr1) == True)
assert(step_reduce(expr1).val == True)

expr2 = not_expr(
    not_expr(
        val(False)
    )
)
assert(size(expr2) == 3)
assert(value(expr2) == False)
assert(step_reduce(expr2).val == False)

expr3 = binary_expr(
    val(True),
    not_expr(
        val(False)
    )
)
assert(height(expr3) == 3)
assert(value(expr3) == True)
assert(step_reduce(expr3).val == True)
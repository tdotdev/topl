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
assert(height(expr0) is 7)
assert(value(expr0) is False)

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
        val(False)
    )
)
assert(size(expr1) == 11)

expr2 = not_expr(
    not_expr(
        val(False)
    )
)
assert(size(expr2) == 3)
assert(value(expr2) is False)

expr3 = binary_expr(
    val(True),
    not_expr(
        val(False)
    )
)
assert(height(expr3) == 3)
assert(value(expr3) is True)



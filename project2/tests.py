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

expr3 = binary_expr(
    val(True),
    not_expr(
        val(False)
    )
)
assert(size(expr3) == 4)



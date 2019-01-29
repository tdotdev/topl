Tim Snyder - Theory of Programming Languages - Project 2

---

Due: Feb 5

Implement the AST for the following language:

e ::= true | false | not e1 | e1 and e2 | e1 or e2

Implement the following operations on the abstract syntax tree:

- size -- compute the size of an expression
- height -- compute the height of an expression
- same -- Return true if two expressions are identical
- value -- compute the value of an expression
- step -- Return an expression representing a single step of evaluation
- reduce -- Calls step repeatedly until the expression is non-reducible


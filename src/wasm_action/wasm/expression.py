"""
Expression evaluator.

Expressions are evaluated against a WebAssembly module instance.
Expressions allow to combine zero or more function invocations into one go.
An expression may consist of the following constituents:
 * Literals
    Simple types that can be represented in WA types.
    1, 0x23, true, false, 3.14
 * Function invocations
    Refer to functions that must be present in the exports section (what about allowing to call imports?).
    sum(2, 3)
 * Tuples for structure and multiple instructions.
    Tuples - allow multiple invocations in one.


Example:
Suppose the file calculator.wasm provides the following exports:
 - sum, mul
Then the following expressions can be constructed:
sum(2, 3)
sum(2, mul(3, 5))
sum(1, sum(2, sum(3, sum(4, 5))))
(1, sum(2, 3))  -> (1, 5)

Implementation takes a shortcut by using Python's ast module.
"""

import ast

ALLOWED_SYNTAX = {
    ast.Module,
    ast.Expr,
    ast.Constant,
    ast.Tuple,
    ast.Call,
    ast.Name,
}


def parse(value: str) -> ast.AST:
    """Parse an expression into an ast syntax tree."""
    node = ast.parse(value)
    for x in ast.walk(node):
        if isinstance(x, ast.Load):
            # ignored
            continue
        if x.__class__ not in ALLOWED_SYNTAX:
            raise SyntaxError("{} not allowed in expression".format(x.__class__.__name__))
    return node


def evaluate(expression, obj):
    node = parse(expression)
    return Evaluator(obj).evaluate(node)


class Evaluator:

    def __init__(self, obj):
        self.obj= obj

    def evaluate(self, node: ast.AST) -> object:
        if isinstance(node, ast.Module):
            for sub in node.body:
                yield from self.evaluate(sub)

        elif isinstance(node, ast.Expr):
            yield self.compute(node)

        else:
            raise Exception("value not allowed: {}".format(node))

    def compute(self, node):
        """Evaluate a single expression"""
        if isinstance(node, ast.Expr):
            return self.compute(node.value)

        elif isinstance(node, ast.Tuple):
            return tuple(self.compute(x) for x in node.elts)

        elif isinstance(node, ast.Constant):
            return node.value

        elif isinstance(node, ast.Call):
            assert isinstance(node.func, ast.Name)
            name = node.func.id
            func = getattr(self.obj, name)
            args = [self.compute(x) for x in node.args]
            return func(*args)

        elif isinstance(node, ast.Name):
            return getattr(self.obj, node.id)

        else:
            raise Exception("value not allowed: {}".format(node))

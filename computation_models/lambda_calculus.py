# lambda_calculus.py
"""
Simple Lambda Calculus Interpreter
"""

class Lambda:
    def __init__(self, var, body):
        self.var = var
        self.body = body

    def __call__(self, arg):
        return substitute(self.body, self.var, arg)

def substitute(expr, var, val):
    if isinstance(expr, str):
        return val if expr == var else expr
    elif isinstance(expr, Lambda):
        if expr.var == var:
            return expr
        return Lambda(expr.var, substitute(expr.body, var, val))
    elif isinstance(expr, tuple):
        return (substitute(expr[0], var, val), substitute(expr[1], var, val))
    return expr

def evaluate(expr):
    if isinstance(expr, tuple):
        func, arg = expr
        func = evaluate(func)
        arg = evaluate(arg)
        if isinstance(func, Lambda):
            return evaluate(func(arg))
        return (func, arg)
    return expr


if __name__ == "__main__":
    identity = Lambda("x", "x")
    expr = (identity, "y")
    print(evaluate(expr))  # 'y'

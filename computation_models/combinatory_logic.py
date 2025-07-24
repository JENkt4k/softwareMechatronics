# combinatory_logic.py
"""
SKI Combinatory Logic Interpreter
"""

class S:
    def __call__(self, x):
        return lambda y: lambda z: x(z)(y(z))

class K:
    def __call__(self, x):
        return lambda y: x

class I:
    def __call__(self, x):
        return x


if __name__ == "__main__":
    s = S()
    k = K()
    i = I()

    identity = s(k)(k)
    print(identity("Hello"))  # 'Hello'

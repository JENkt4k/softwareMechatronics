import os

# Path to computation_models directory
cm_dir = r"E:\git_slow\SoftwareMechatronics\computation_models"

computation_models_files = {
    "finite_state_machine.py": '''# finite_state_machine.py
"""
Finite State Machine (FSM) Implementation
"""

class FSM:
    def __init__(self, states, alphabet, transition, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition = transition  # dict of dicts: {state: {symbol: next_state}}
        self.start_state = start_state
        self.accept_states = accept_states

    def accepts(self, string):
        current_state = self.start_state
        for symbol in string:
            if symbol not in self.alphabet or symbol not in self.transition[current_state]:
                return False
            current_state = self.transition[current_state][symbol]
        return current_state in self.accept_states


if __name__ == "__main__":
    states = {"q0", "q1"}
    alphabet = {"0", "1"}
    transition = {
        "q0": {"0": "q0", "1": "q1"},
        "q1": {"0": "q0", "1": "q1"}
    }
    fsm = FSM(states, alphabet, transition, "q0", {"q1"})
    print(fsm.accepts("0101"))  # True
''',

    "pushdown_automaton.py": '''# pushdown_automaton.py
"""
Pushdown Automaton (PDA) Implementation
"""

class PDA:
    def __init__(self, states, input_alphabet, stack_alphabet, transition, start_state, accept_states):
        self.states = states
        self.input_alphabet = input_alphabet
        self.stack_alphabet = stack_alphabet
        self.transition = transition  # dict: (state, symbol, stack_top) -> [(new_state, stack_ops)]
        self.start_state = start_state
        self.accept_states = accept_states

    def accepts(self, input_str):
        return self._accepts_helper(self.start_state, input_str, ["$"])

    def _accepts_helper(self, state, remaining_input, stack):
        if not remaining_input and state in self.accept_states:
            return True
        if not remaining_input:
            symbol = ""
        else:
            symbol = remaining_input[0]

        stack_top = stack[-1] if stack else "$"

        key = (state, symbol, stack_top)
        if key in self.transition:
            for new_state, stack_ops in self.transition[key]:
                new_stack = stack[:-1] + stack_ops[::-1]
                if self._accepts_helper(new_state, remaining_input[1:], new_stack):
                    return True
        return False


if __name__ == "__main__":
    # Example PDA that accepts balanced parentheses
    states = {"q0"}
    input_alphabet = {"(", ")"}
    stack_alphabet = {"$", "("}
    transition = {
        ("q0", "(", "$"): [("q0", ["$", "("])],
        ("q0", "(", "("): [("q0", ["(", "("])],
        ("q0", ")", "("): [("q0", [])],
        ("q0", "", "$"): [("q0", ["$"])]
    }
    pda = PDA(states, input_alphabet, stack_alphabet, transition, "q0", {"q0"})
    print(pda.accepts("(()())"))  # True
''',

    "turing_machine.py": '''# turing_machine.py
"""
Turing Machine Implementation
"""

class TuringMachine:
    def __init__(self, tape, transition, start_state, accept_state, reject_state, blank="_"):
        self.tape = list(tape)
        self.transition = transition  # dict: (state, symbol) -> (new_state, new_symbol, move)
        self.state = start_state
        self.head = 0
        self.accept_state = accept_state
        self.reject_state = reject_state
        self.blank = blank

    def step(self):
        symbol = self.tape[self.head] if self.head < len(self.tape) else self.blank
        if (self.state, symbol) not in self.transition:
            self.state = self.reject_state
            return False

        new_state, new_symbol, move = self.transition[(self.state, symbol)]
        if self.head >= len(self.tape):
            self.tape.append(self.blank)
        self.tape[self.head] = new_symbol
        self.state = new_state
        self.head += 1 if move == "R" else -1 if move == "L" else 0
        if self.head < 0:
            self.tape.insert(0, self.blank)
            self.head = 0
        return True

    def run(self):
        while self.state not in (self.accept_state, self.reject_state):
            if not self.step():
                break
        return self.state == self.accept_state


if __name__ == "__main__":
    # TM that accepts "1"
    tape = list("1")
    transition = {
        ("q0", "1"): ("q_accept", "1", "R")
    }
    tm = TuringMachine(tape, transition, "q0", "q_accept", "q_reject")
    print(tm.run())  # True
''',

    "lambda_calculus.py": '''# lambda_calculus.py
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
''',

    "combinatory_logic.py": '''# combinatory_logic.py
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
'''
}

os.makedirs(cm_dir, exist_ok=True)

# Write files
for filename, content in computation_models_files.items():
    file_path = os.path.join(cm_dir, filename)
    with open(file_path, "w") as f:
        f.write(content)

print(f"Computation models filled in {cm_dir}")

# turing_machine.py
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

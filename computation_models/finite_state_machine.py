# finite_state_machine.py
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

# pushdown_automaton.py
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

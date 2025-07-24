"""
Computation models: FSM, PDA, Turing Machine, Lambda Calculus, Combinatory Logic.
"""

from .finite_state_machine import FSM
from .pushdown_automaton import PDA
from .turing_machine import TuringMachine
from .lambda_calculus import Lambda, evaluate
from .combinatory_logic import S, K, I

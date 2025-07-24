# test_models.py
import unittest
from computation_models.finite_state_machine import FSM
from computation_models.lambda_calculus import Lambda, evaluate
from computation_models.combinatory_logic import S, K, I

class TestComputationModels(unittest.TestCase):

    def test_fsm(self):
        states = {"q0", "q1"}
        alphabet = {"0", "1"}
        transition = {"q0": {"0": "q0", "1": "q1"}, "q1": {"0": "q0", "1": "q1"}}
        fsm = FSM(states, alphabet, transition, "q0", {"q1"})
        self.assertTrue(fsm.accepts("01"))
        self.assertFalse(fsm.accepts("00"))

    def test_lambda_calculus(self):
        identity = Lambda("x", "x")
        expr = (identity, "y")
        self.assertEqual(evaluate(expr), "y")

    def test_combinatory_logic(self):
        s, k, i = S(), K(), I()
        self.assertEqual(i("Hello"), "Hello")
        self.assertEqual(k("X")("Y"), "X")
        self.assertEqual(s(k)(k)("Z"), "Z")

if __name__ == '__main__':
    unittest.main()

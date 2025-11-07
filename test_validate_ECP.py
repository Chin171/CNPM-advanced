import unittest
from student_score import is_valid_float, calculate_final_score

class TestEquivalencePartition(unittest.TestCase):
    # ---- is_valid_float() ----
    def test_invalid_non_number(self):
        self.assertFalse(is_valid_float("abc")[0])

    def test_invalid_negative(self):
        self.assertFalse(is_valid_float(-0.25)[0])

    def test_invalid_over_10(self):
        self.assertFalse(is_valid_float(10.25)[0])

    def test_valid_normal(self):
        self.assertTrue(is_valid_float(7.5)[0])

    def test_invalid_not_multiple_025(self):
        self.assertFalse(is_valid_float(5.1)[0])

    def test_invalid_too_many_decimals(self):
        self.assertFalse(is_valid_float(6.123)[0])

    # ---- calculate_final_score() ----
    def test_total_sessions_zero(self):
        self.assertFalse(calculate_final_score(0, 0, 5, 5, 5)['pass'])

    def test_absent_over_20_percent(self):
        self.assertFalse(calculate_final_score(10, 3, 5, 5, 5)['pass'])

    def test_valid_no_violation(self):
        self.assertTrue(calculate_final_score(10, 2, 5, 5, 5)['pass'])

    def test_cc_zero(self):
        self.assertFalse(calculate_final_score(10, 0, 0, 5, 5)['pass'])

    def test_gk_zero(self):
        self.assertFalse(calculate_final_score(10, 0, 5, 0, 5)['pass'])

    def test_ck_less_than_4(self):
        self.assertFalse(calculate_final_score(10, 0, 5, 5, 3.9)['pass'])

    def test_tb_less_than_4(self):
        self.assertFalse(calculate_final_score(10, 0, 3, 3, 4)['pass'])

    def test_rule_violation(self):
        self.assertFalse(calculate_final_score(10, 0, 5, 5, 5, "yes")['pass'])

    def test_all_valid(self):
        self.assertTrue(calculate_final_score(10, 0, 5, 5, 5, "no")['pass'])



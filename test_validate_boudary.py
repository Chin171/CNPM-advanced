import unittest
from math import isclose
# ====== UNIT TESTS ======
class TestStudentScore(unittest.TestCase):

    # --- 1. total_sessions > 0 ---
    def test_total_sessions_boundary(self):
        r = calculate_final_score(0, 0, 5, 5, 5, "no")
        self.assertFalse(r['pass'])
        self.assertIn("Tổng số buổi học phải > 0", " ".join(r['reasons']))

        r = calculate_final_score(1, 0, 5, 5, 5, "no")
        self.assertTrue(r['pass'])

        r = calculate_final_score(2, 0, 5, 5, 5, "no")
        self.assertTrue(r['pass'])

    # --- 2. absent_sessions <= 20% total_sessions ---
    def test_absent_boundary(self):
        r = calculate_final_score(10, 1.9, 5, 5, 5, "no")
        self.assertTrue(r['pass'])

        r = calculate_final_score(10, 2.0, 5, 5, 5, "no")
        self.assertTrue(r['pass'])

        r = calculate_final_score(10, 2.1, 5, 5, 5, "no")
        self.assertFalse(r['pass'])
        self.assertIn("Số buổi nghỉ > 20%", " ".join(r['reasons']))

    # --- 3. cc > 0 ---
    def test_cc_boundary(self):
        r = calculate_final_score(10, 0, 0, 5, 5, "no")
        self.assertFalse(r['pass'])
        self.assertIn("CC", " ".join(r['reasons']))

        r = calculate_final_score(10, 0, 0.1, 5, 5, "no")
        self.assertTrue(r['pass'])

    # --- 4. gk > 0 ---
    def test_gk_boundary(self):
        r = calculate_final_score(10, 0, 5, 0, 5, "no")
        self.assertFalse(r['pass'])
        self.assertIn("GK", " ".join(r['reasons']))

        r = calculate_final_score(10, 0, 5, 0.1, 5, "no")
        self.assertTrue(r['pass'])

    # --- 5. ck >= 4 ---
    def test_ck_boundary(self):
        r = calculate_final_score(10, 0, 5, 5, 3.9, "no")
        self.assertFalse(r['pass'])
        self.assertIn("CK", " ".join(r['reasons']))

        r = calculate_final_score(10, 0, 5, 5, 4.0, "no")
        self.assertTrue(r['pass'])

        r = calculate_final_score(10, 0, 5, 5, 4.1, "no")
        self.assertTrue(r['pass'])

    # --- 6. TB >= 4 ---
    def test_tb_boundary(self):
        # TB = 3.9
        r = calculate_final_score(10, 0, 3, 3, 5, "no")
        self.assertFalse(r['pass'])
        self.assertIn("TB", " ".join(r['reasons']))

        # TB = 4.0
        r = calculate_final_score(10, 0, 4, 4, 4, "no")
        self.assertTrue(r['pass'])

        # TB = 4.1
        r = calculate_final_score(10, 0, 4.5, 4.5, 4.2, "no")
        self.assertTrue(r['pass'])

    # --- 7. violated_rules ---
    def test_violated_rules_boundary(self):
        r = calculate_final_score(10, 0, 5, 5, 5, "yes")
        self.assertFalse(r['pass'])
        self.assertIn("quy chế", " ".join(r['reasons']))

        r = calculate_final_score(10, 0, 5, 5, 5, "no")
        self.assertTrue(r['pass'])

        r = calculate_final_score(10, 0, 5, 5, 5, " No ")
        self.assertTrue(r['pass'])

    # --- 8. is_valid_float boundary tests ---
    def test_is_valid_float_boundary(self):
        # Biên dưới 0
        valid, _ = is_valid_float("-0.25")
        self.assertFalse(valid)

        # Biên trên 10
        valid, _ = is_valid_float("10")
        self.assertTrue(valid)
        valid, _ = is_valid_float("10.25")
        self.assertFalse(valid)

        # Quá 2 chữ số thập phân
        valid, msg = is_valid_float("5.123")
        self.assertFalse(valid)
        self.assertIn("2 chữ số", msg)

        # Không phải bội của 0.25
        valid, msg = is_valid_float("6.1")
        self.assertFalse(valid)
        self.assertIn("0.25", msg)

        # Giá trị hợp lệ
        valid, val = is_valid_float("7.5")
        self.assertTrue(valid)
        self.assertTrue(isclose(val, 7.5))

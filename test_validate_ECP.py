class TestValidateEquivalence(unittest.TestCase):

    def test_valid_all_conditions(self):
        """Lớp hợp lệ: tất cả điều kiện đạt"""
        passed, total, reasons = validate(10, 1, 6, 6, "no")
        self.assertTrue(passed)
        self.assertTrue(isclose(total, 6.0))

    def test_invalid_total_sessions(self):
        """Lớp không hợp lệ: total_sessions <= 0"""
        with self.assertRaises(ValueError):
            validate(0, 0, 5, 5, "no")

    def test_invalid_absent_sessions(self):
        """Lớp không hợp lệ: absent_sessions >= 20%"""
        passed, total, reasons = validate(10, 2, 6, 6, "no")
        self.assertFalse(passed)
        self.assertIn("Too many absences", reasons)

    def test_invalid_coursework_zero(self):
        """Lớp không hợp lệ: coursework_score = 0"""
        passed, total, reasons = validate(10, 1, 0, 6, "no")
        self.assertFalse(passed)
        self.assertIn("Coursework score is zero", reasons)

    def test_invalid_final_exam_below_4(self):
        """Lớp không hợp lệ: final_exam_score < 4"""
        passed, total, reasons = validate(10, 1, 6, 3, "no")
        self.assertFalse(passed)
        self.assertIn("Final exam score below 4", reasons)

    def test_invalid_total_score_below_5(self):
        """Lớp không hợp lệ: tổng điểm < 5"""
        passed, total, reasons = validate(10, 1, 4, 4, "no")
        self.assertFalse(passed)
        self.assertIn("Total score", " ".join(reasons))

    def test_invalid_violated_rules(self):
        """Lớp không hợp lệ: violated_rules != 'no'"""
        passed, total, reasons = validate(10, 1, 6, 6, "yes")
        self.assertFalse(passed)
        self.assertIn("Violated rules", reasons)

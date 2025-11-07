class TestValidateBoundary(unittest.TestCase):

    def test_total_sessions_zero(self):
        with self.assertRaises(ValueError):
            validate(0, 0, 5, 5, "no")

    def test_total_sessions_min_valid(self):
        passed, total, reasons = validate(1, 0, 5, 5, "no")
        self.assertTrue(passed)
        self.assertTrue(isclose(total, 5.0))

    def test_absent_below_threshold(self):
        passed, total, reasons = validate(10, 1, 5, 5, "no")
        self.assertTrue(passed)

    def test_absent_equal_threshold(self):
        passed, total, reasons = validate(10, 2, 5, 5, "no")
        self.assertFalse(passed)
        self.assertIn("Too many absences", reasons)

    def test_absent_just_below_threshold(self):
        passed, total, reasons = validate(10, 1.9, 5, 5, "no")
        self.assertTrue(passed)

    def test_coursework_zero(self):
        passed, total, reasons = validate(10, 0, 0, 5, "no")
        self.assertFalse(passed)
        self.assertIn("Coursework score is zero", reasons)

    def test_coursework_above_zero(self):
        passed, total, reasons = validate(10, 0, 0.1, 5, "no")
        self.assertTrue(passed)

    def test_final_exam_below_4(self):
        passed, total, reasons = validate(10, 0, 5, 3.9, "no")
        self.assertFalse(passed)
        self.assertIn("Final exam score below 4", reasons)

    def test_final_exam_equal_4(self):
        passed, total, reasons = validate(10, 0, 5, 4.0, "no")
        # total_score = 0.4*5 + 0.6*4 = 4.4 < 5, nên fail
        self.assertFalse(passed)
        self.assertIn("Total score", " ".join(reasons))

    def test_total_score_below_5(self):
        passed, total, reasons = validate(10, 0, 5, 4.83, "no")
        self.assertFalse(passed)
        self.assertIn("Total score", " ".join(reasons))

    def test_total_score_equal_5(self):
        passed, total, reasons = validate(10, 0, 5, 5, "no")
        self.assertTrue(passed)

    def test_violated_rules_no(self):
        passed, total, reasons = validate(10, 0, 5, 5, "no")
        self.assertTrue(passed)

    def test_violated_rules_No_case_insensitive(self):
        passed, total, reasons = validate(10, 0, 5, 5, "No")
        self.assertTrue(passed)

    def test_violated_rules_yes(self):
        passed, total, reasons = validate(10, 0, 5, 5, " yes ")
        self.assertFalse(passed)
        self.assertIn("Violated rules", reasons)

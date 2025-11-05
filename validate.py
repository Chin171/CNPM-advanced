def validate(total_sessions, absent_sessions, coursework_score, final_exam_score, violated_rules):
    """
    Returns (passed: bool, total_score: float, reasons: list).
    Pass conditions:
      - absent_sessions < 20% of total_sessions
      - coursework_score != 0
      - final_exam_score >= 4
      - total_score = 0.4*coursework_score + 0.6*final_exam_score >= 5
      - violated_rules == "no" (case-insensitive)
    """
    if total_sessions <= 0:
        raise ValueError("total_sessions must be > 0")

    reasons = []
    if absent_sessions >= 0.2 * total_sessions:
        reasons.append("Too many absences")
    if coursework_score == 0:
        reasons.append("Coursework score is zero")
    if final_exam_score < 4:
        reasons.append("Final exam score below 4")

    total_score = 0.4 * coursework_score + 0.6 * final_exam_score
    if total_score < 5:
        reasons.append(f"Total score {total_score:.2f} below 5")

    if str(violated_rules).strip().lower() != "no":
        reasons.append("Violated rules")

    passed = len(reasons) == 0
    return passed, total_score, reasons


if __name__ == "__main__":
    try:
        total_sessions = int(input("total_sessions: ").strip())
        absent_sessions = int(input("absent_sessions: ").strip())
        coursework_score = float(input("coursework_score: ").strip())
        final_exam_score = float(input("final_exam_score: ").strip())
        violated_rules = input("violated_rules (yes/no): ").strip()
    except Exception as e:
        print("Invalid input:", e)
        raise SystemExit(1)

    passed, total_score, reasons = validate(
        total_sessions, absent_sessions, coursework_score, final_exam_score, violated_rules
    )

    if passed:
        print(f"PASSED (total_score={total_score:.2f})")
    else:
        print(f"FAILED (total_score={total_score:.2f}) Reasons: {', '.join(reasons)}")

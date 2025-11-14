from typing import Tuple, Optional, List
from xmlrpc.client import boolean

def validate_and_score(
    attendance_score: float,
    midterm_score: float,
    final_score: float,
    is_violated_rule: bool,
) -> Tuple[Optional[float], Optional[str], bool, List[str]]:
    """
    Validate inputs and compute weighted final_grade.

    Returns:
      (score_float or None, score_str or None, is_rule_violated, errors_list)
    """
    errors: List[str] = []
    results : bool
    if is_violated_rule == True:
        results = False
        errors.append("Rule violation detected.")
        print("Validation failed due to rule violation.")
        return None, None, True, errors
    else:
        if attendance_score <=0:
            results = False
            errors.append("Attendance score must be greater than 0.")
        if midterm_score <=0:
            results = False
            errors.append("Midterm score must be greater than 0.")
            print("Validation failed with errors:", errors)
            return None, None, False, errors
        if final_score <4:
            results = False
            errors.append("Final score must be at least 4.")
            print("Validation failed with errors:", errors)
            return None, None, False, errors
        else:
            final_grade = 0.1*attendance_score + 0.3*midterm_score + 0.6*final_score
            final_grade_str = f"{final_grade:.2f}"
            if final_grade < 5:
                results = False
                errors.append("Final grade is below passing threshold.")
                print("Validation failed with errors:", errors) 
                return None, None, False, errors
            else:
                results = True
                print("Is passed:", results)
                print(f"Validation succeeded. Final grade: {final_grade_str}")
                return final_grade, results,errors
            
if __name__ == "__main__":
    try:
        attendance_score = float(input("Enter attendance_score (0 < attendance_score <= 10): ").strip())
        midterm_score = float(input("Enter midterm_score (0 < midterm_score <= 10): ").strip())
        final_score = float(input("Enter final_score (4 <= final_score <= 10): ").strip())
        is_violated_input = input("Có vi phạm quy chế không? (yes/true/y/no/false/n): ").strip().lower()
        is_violated_rule = is_violated_input in ["yes", "true", "y"]
    except ValueError:
        print("Invalid input: all scores must be numeric floats.")
    else:
       validate_and_score(attendance_score, midterm_score, final_score, is_violated_rule)   

def is_valid_float(value):
    """Kiểm tra xem input có hợp lệ (float, <=10, 2 chữ số thập phân, bước 0.25)"""
    try:
        f = float(value)
    except ValueError:
        return False, "Giá trị không phải số thực"
    
    if f < 0 or f > 10:
        return False, "Giá trị phải nằm trong khoảng 0–10"
    
    # Kiểm tra số chữ số thập phân (tối đa 2)
    s = str(value)
    if '.' in s and len(s.split('.')[1]) > 2:
        return False, "Chỉ được nhập tối đa 2 chữ số thập phân"
    
    # Kiểm tra bước nhảy 0.25
    if round(f * 100) % 25 != 0:
        return False, "Giá trị phải là bội số của 0.25 (ví dụ: 6.25, 7.5, 8.75)"
    
    return True, f


def calculate_final_score(total_sessions, absent_sessions, cc, gk, ck, violated_rules):
    """
    Tính điểm trung bình và xét Pass/Fail dựa trên yêu cầu:
    - absent_sessions <= 20% tổng số buổi
    - cc > 0
    - gk > 0
    - ck >= 4
    - TB >= 4.0
    - Không vi phạm quy chế
    """
    reasons = []

    # Kiểm tra số buổi học
    if total_sessions <= 0:
        reasons.append("Tổng số buổi học phải > 0")
    elif absent_sessions > 0.2 * total_sessions:
        reasons.append("Số buổi nghỉ > 20% tổng số buổi học")

    # Kiểm tra điểm
    if cc <= 0:
        reasons.append("Điểm chuyên cần (CC) phải > 0")
    if gk <= 0:
        reasons.append("Điểm giữa kỳ (GK) phải > 0")
    if ck < 4:
        reasons.append("Điểm cuối kỳ (CK) phải >= 4")

    # Tính điểm trung bình
    tb = round(0.1 * cc + 0.3 * gk + 0.6 * ck, 1)
    if tb < 4.0:
        reasons.append(f"Điểm trung bình (TB={tb}) < 4.0")

    # Kiểm tra vi phạm
    if violated_rules.strip().lower() != "no":
        reasons.append("Vi phạm quy chế thi")

    passed = len(reasons) == 0
    return passed, tb, reasons


if __name__ == "__main__":
    print("=== ĐÁNH GIÁ HỌC PHẦN SINH VIÊN ===")

    try:
        total_sessions = int(input("Tổng số buổi học: ").strip())
        absent_sessions = int(input("Số buổi nghỉ: ").strip())
        
        # Validate điểm thành phần
        for label in ["Điểm chuyên cần (CC)", "Điểm giữa kỳ (GK)", "Điểm cuối kỳ (CK)"]:
            while True:
                value = input(f"{label}: ").strip()
                valid, result = is_valid_float(value)
                if valid:
                    if label.startswith("Điểm chuyên cần"):
                        cc = result
                    elif label.startswith("Điểm giữa"):
                        gk = result
                    else:
                        ck = result
                    break
                else:
                    print(f"Lỗi: {result}. Vui lòng nhập lại.")

        violated_rules = input("Có vi phạm quy chế thi? (yes/no): ").strip()
        
        passed, tb, reasons = calculate_final_score(total_sessions, absent_sessions, cc, gk, ck, violated_rules)
        
        print("\n=== KẾT QUẢ ===")
        if passed:
            print(f"PASS – Điểm trung bình: {tb}")
        else:
            print(f"FAIL – Điểm trung bình: {tb}")
            print("Lý do:")
            for r in reasons:
                print(f"- {r}")
                
    except Exception as e:
        print("Lỗi nhập dữ liệu:", e)

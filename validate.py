class HocPhan:
    def __init__(self, so_buoi_hoc, so_buoi_nghi, diem_thanh_phan, diem_cuoi_ky, vi_pham_quy_che=False):
        self.so_buoi_hoc = so_buoi_hoc
        self.so_buoi_nghi = so_buoi_nghi
        self.diem_thanh_phan = diem_thanh_phan
        self.diem_cuoi_ky = diem_cuoi_ky
        self.vi_pham_quy_che = vi_pham_quy_che

    def tinh_diem_trung_binh(self):
        """Ví dụ: điểm trung bình = 40% điểm thành phần + 60% điểm cuối kỳ"""
        return round(self.diem_thanh_phan * 0.4 + self.diem_cuoi_ky * 0.6, 2)

    def kiem_tra_dat_mon(self):
        ly_do = []

        # Kiểm tra số buổi nghỉ học
        if self.so_buoi_nghi > 0.2 * self.so_buoi_hoc:
            ly_do.append("Số buổi nghỉ vượt quá 20% tổng số buổi học")

        # Điểm thành phần phải > 0
        if self.diem_thanh_phan <= 0:
            ly_do.append("Điểm thành phần phải lớn hơn 0")

        # Điểm cuối kỳ >= 4
        if self.diem_cuoi_ky < 4:
            ly_do.append("Điểm cuối kỳ phải >= 4")

        # Không vi phạm quy chế thi
        if self.vi_pham_quy_che:
            ly_do.append("Sinh viên vi phạm quy chế thi")

        # Điểm trung bình >= 5
        diem_tb = self.tinh_diem_trung_binh()
        if diem_tb < 5:
            ly_do.append(f"Điểm trung bình {diem_tb} < 5")

        # Kết luận
        if ly_do:
            return {
                "dat_mon": False,
                "diem_trung_binh": diem_tb,
                "ly_do": ly_do
            }
        else:
            return {
                "dat_mon": True,
                "diem_trung_binh": diem_tb,
                "ly_do": ["Đạt học phần"]
            }

# Ví dụ sử dụng
if __name__ == "__main__":
    sv = HocPhan(
        so_buoi_hoc=30,
        so_buoi_nghi=5,
        diem_thanh_phan=6.0,
        diem_cuoi_ky=5.5,
        vi_pham_quy_che=False
    )

    ket_qua = sv.kiem_tra_dat_mon()
    print("Kết quả:", "ĐẠT" if ket_qua["dat_mon"] else "KHÔNG ĐẠT")
    print("Điểm trung bình:", ket_qua["diem_trung_binh"])
    print("Chi tiết:", "; ".join(ket_qua["ly_do"]))

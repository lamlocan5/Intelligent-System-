def diem_sang_chu(x):
    if x >= 8.5: return "A"
    elif x >= 7.0: return "B"
    elif x >= 5.5: return "C"
    elif x >= 4.0: return "D"
    else: return "F"
def du_doan_thanh_phan_chu(d1, d2, d3, d4, d5):
    # Tính mean
    mean_x = (d1 + d2 + d3 + d4 + d5) / 5.0
    # Tạo độ lệch dựa trên 10%, 20%, 30%, 40%
    factors = [0.85, 0.95, 1.05, 1.15]
    # Tạo điểm thành phần
    comps = [round(max(1.0, min(10.0, mean_x * f)), 2) for f in factors]
    # Chuyển sang chữ
    chu = [diem_sang_chu(c) for c in comps]
    return comps, chu
# ======================
#     INPUT USER
# ======================
d1 = float(input("Nhập điểm 1: "))
d2 = float(input("Nhập điểm 2: "))
d3 = float(input("Nhập điểm 3: "))
d4 = float(input("Nhập điểm 4: "))
d5 = float(input("Nhập điểm 5: "))
comps, chu = du_doan_thanh_phan_chu(d1, d2, d3, d4, d5)
print("\n=== KẾT QUẢ DỰ ĐOÁN ===")
print("4 điểm thành phần:", comps)
print("4 thành phần chữ :", chu)
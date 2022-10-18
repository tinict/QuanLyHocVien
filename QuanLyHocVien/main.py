#Quản lý học viên
#1. Thêm học viên
#2. Hiển thị học viên
#3. Sửa thông tin học viên
#4. Xóa thông tin học viên
from QuanLyHocVien import QuanLyHocVien

QLHV = QuanLyHocVien(2);  # type: ignore
QLHV.ThemSinhVien();
QLHV.SuaHocVien(1);
QLHV.XoaHocVien(1);
QLHV.HienThiHocVien();
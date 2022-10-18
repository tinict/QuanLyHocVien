#id, name, age, city, diemtin, diemtienganh
from Reman import Student
  
class QuanLyHocVien(Student):
    def __init__(self, sluong, ListSV = []):
        self.sluong = sluong;
        self.ListSV = ListSV;
    def ThemSinhVien(self):
        i = 0;
        while(i < self.sluong):
            id = int(input('Id:'));
            name = str(input('Name: '));
            age = int(input('Age: '));
            city = str(input('City: '));
            diemtin = float(input('Diemtin: '));
            diemtienganh = float(input('Diemtienganh: '));
            Study = Student(id, name, age, city, diemtin, diemtienganh);
            self.ListSV.append(Study);
            i += 1;
    def HienThiHocVien(self):
        for i in self.ListSV:
            i.show();
    def SuaHocVien(self, id_Edit):
        for i in self.ListSV:
            if(i.id == id_Edit):
                idEdit = int(input('Id:'));
                nameEdit = str(input('Name: '));
                ageEdit = int(input('Age: '));
                cityEdit = str(input('City: '));
                diemtinEdit = float(input('Diemtin: '));
                dTAEdit = float(input('Diemtienganh: '));
                i.setStudent(idEdit, nameEdit, ageEdit, cityEdit, diemtinEdit, dTAEdit);
                break;
    def XoaHocVien(self, id_delete):
        for i in self.ListSV:
            if (i.id == id_delete):
                self.ListSV.remove(i);

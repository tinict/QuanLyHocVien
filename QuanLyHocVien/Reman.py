class Student:
    def __init__(self, id, name, age, city, diemtin, diemtienganh):
        self.id = id;
        self.name = name;
        self.age = age;
        self.city = city;
        self.diemtin = diemtin;
        self.diemtienganh = diemtienganh;
    def show(self):
        print(str(self.id) + ' ' + str(self.name) + ' ' + str(self.age) + " " + str(self.city) + " " + str(self.diemtin) + " " + str(self.diemtienganh));
    def setStudent(self, id_Edit, name_Edit, age_Edit, city_Edit, diemtin_Edit, diemtienganh_Edit):
        self.id = id_Edit;
        self.name = name_Edit;
        self.age = age_Edit;
        self.city = city_Edit;
        self.diemtin = diemtin_Edit;
        self.diemtienganh = diemtienganh_Edit;
class student:
    grade=0
    name=""
    gpa=0
    age=0
    def __init__(self, grade_p, name_p, gpa_p, age_p):
        self.grade=grade_p
        self.name=name_p
        self.gpa=gpa_p
        self.age=age_p
    def study(self, hours):
        print(self.name, "is studying for", hours, "hours.")


student1=student(grade_p=8, name_p="Bobby", gpa_p=3.6, age_p=14)
student1.study(2)

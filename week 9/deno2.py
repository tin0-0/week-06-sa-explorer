class student: 
    def __init__(self,name, student_number,course_code,province):
        self.name = name
        self.student_number = student_number
        self.course_code = course_code
        self.province = province
    def greet(self):
        return f"Molo! I am {self.name} from {self.province},studying {self.course_code}"

thabo = student("Thabo Mkize", "GP206001", "ITPROG26/FT", "Gauteng")
paul = student("Paul Jobs", "WC206002", "ITPROG26/FT", "Western Cape")
lerato = student("Lerato Doe", "KZ2026003", "ITPROG26/FT", "kwazulu Natal")
sarah = student("sarah johnson","EC2026004", "ITPROG/FT", "Eastern Cape")

students = [thabo, paul, lerato, sarah]

for student in students:
    print(f"{student.name} from {student.province}")
print()
for student in students:
    print(student.greet())
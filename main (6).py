class Student:

    def __init__(self, name, roll_number, cgpa):
     self.name = name
     self.roll_number = roll_number
     self.cgpa = cgpa


def sorted_students (student_list):
  #sort the list of students in descending order of CGPA

 sorted_students =sorted(student_list,
                     keylambdastudent:
Student.cgpa,  
                        reverse=True)
 #syntax-Lambda arg:exp
 return sorted_students


   
students = [
  Student("John Doe", "A101", 3.8),
  Student("Jane Doe", "8202", 3.9),

  Student("Jim Smith", "C303", 3.7),
Student("Jill  Johnson", "D404", 4.0)
]


sorted_students = sorted_students(students)
 #print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA:{}".format(student.name, student.roll_number, student.cgpa))
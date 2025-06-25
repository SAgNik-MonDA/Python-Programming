class Student:
    name = "sagnik"
    def __init__(self , fullname):
        self.name = fullname
        print("adding new student in clg database :")
   

# creating object (object is a instance of class)
s1=Student("karan")
print(s1.name)


s2=Student("sagnik")
print(s2.name)

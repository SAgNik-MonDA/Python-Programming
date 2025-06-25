class Student:
    def __init__(self , name ,marks):
        self.name=name
        self.marks=marks
    
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum +=val
        print("hi",self.name,"your avg score is :",sum/3)


s1=Student("sagnik",[99,98,97])
s1.get_avg()


s1.name = "tirtha"
s1.marks = [89,58,96]
s1.get_avg()
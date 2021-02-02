class Students:
    def set_stud(self,roll,name,course):
        self.roll=roll
        self.name=name
        self.course=course
    def print_stud(self):
        print(self.roll,",",self.name,",",self.course)

stud1=Students()
stud1.set_stud(62,"Hanna","CSE")
stud1.print_stud()

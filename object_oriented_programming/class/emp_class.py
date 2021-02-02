class Employee:
    def set_emp(self,e_id,e_name,desig,salary):
        self.e_id=e_id
        self.e_name=e_name
        self.desig=desig
        self.salary=salary

    def print_emp(self):
        print(self.e_id,",",self.e_name,",",self.desig,",",self.salary)


emp1=Employee()
emp2=Employee()
emp3=Employee()

emp1.set_emp(101,"Hari","Manager",25000)
emp2.set_emp(102,"Holmes","Manager",50000)
emp3.set_emp(103,"Gayatri","Snr Manager",35000)

emp1.print_emp()
emp2.print_emp()
emp3.print_emp()

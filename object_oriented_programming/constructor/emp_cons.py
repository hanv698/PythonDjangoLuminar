class Employee:
    def __init__(self,e_id,e_name,desig,salary):
        self.e_id=e_id
        self.e_name=e_name
        self.desig=desig
        self.salary=salary

    def print_emp(self):
        print(self.e_id,",",self.e_name,",",self.desig,",",self.salary)


emp=Employee(101,"Hari","Manager",25000)

emp.print_emp()


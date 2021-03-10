class Employee{
    constructor(eid,ename,sal,desig){
        this.eid=eid;
        this.ename=ename;
        this.sal=sal;
        this.desig=desig;
    }
    printDet=()=>{
        console.log(this.eid,",",this.ename,",",this.sal,",",this.desig);
    }
}

var employee=[];
var obj=new Employee(100,"varun",25000,"developer");
var obj1=new Employee(101,"arun",22000,"developer");
var obj2=new Employee(102,"ravi",25000,"qa");
var obj3=new Employee(103,"ram",27000,"qa");

employee.push(obj);
employee.push(obj1);
employee.push(obj2);
employee.push(obj3);

employee.forEach(emp=>console.log(emp.desig));
employee.map(emp=>emp.sal+2000).forEach(sal=>console.log(sal));

employee.map(emp=>emp.ename.toUpperCase()).forEach(name=>console.log(name))

employee.filter(emp=>emp.desig=="developer").forEach(emp=>console.log(emp))

employee.sort(o1,o2=>o1.sal>o2.sal?-1:1).forEach(emp=>console.log(emp))

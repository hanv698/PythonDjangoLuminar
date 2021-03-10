class Parent{
    m1(){
        console.log("Inside Parent class");
    }
}

class Child extends Parent{
    m2(){
        console.log("Inside Child class");
    }
}

var child=new Child();
child.m2();
child.m1();
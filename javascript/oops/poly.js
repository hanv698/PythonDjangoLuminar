class Calc{
    add(){
        console.log("No arg method");
    }
    add(num){
        console.log("one arg method");
    }
    add(num1,num2){
        console.log("two arg method");
    }
}

var cal=new Calc();
cal.add(10,20); //recently implemented method only works
cal.add(10);
cal.add();
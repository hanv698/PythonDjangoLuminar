var num=17;
flag=0;

for(let i=2;i<num;i++){
    flag=0
    if(num%i==0){
        flag++;
        break;
    }
    else{
        flag=0;
    }
}
if(flag==0)
    console.log("Prime");
else
    console.log("not prime");

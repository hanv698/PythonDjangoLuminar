var arr1=[10,20,30,40];
var arr2=[21,22,30,31,40];

i=0;
j=0;
for(e1 of arr1){
    for(e2 of arr2){
        if(e1==e2){
            console.log(e1,e2);
            arr1[i]+1;
            arr2[j]+1;
        }
        else if(e1>e2){
            arr2[e2]+1;
        }
        else{
            arr2[e1]+1;
        }
    }
}
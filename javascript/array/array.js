var data=[10,"hai",10.5,true];
console.log(data);
console.log(data[2]);

for(let num of data){
    console.log(num);
}

data.push(20);
console.log(data);

data.pop();
console.log(data);
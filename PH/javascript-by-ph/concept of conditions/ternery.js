/**
 * ternery - three parts
 * 
 *  ? : 
 * 
 * condition ? do something when true: do something when false 
 */


//const age = 20;
//if(age >=18){
    //console.log('you can vote');
//}
//else{
    //console.log('you can not vote');
//}


//age >=18 ? console.log('you can vote') : console.log('you can not vote');


let price = 500;
const isLeader = true;

if(isLeader){
    price = 0;
}
else{
    price = price + 100;
}
//console.log(price);

price = isLeader == true ? 0 : price + 100;



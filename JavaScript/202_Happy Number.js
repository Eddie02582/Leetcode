
var isHappy = function(n) {
    var map = new Map();
    while (n != 1){
        n =   getSum(n);
        if (map.has(n)) {
               
            return false;  
        }            
        map.set(n, n);                 
    }      
    return true;
    
}

function getSum(n){
    var s = n.toString();
    var sum = 0;
    for (var i = 0 ; i < s.length ; i++){
            sum = sum + parseInt(s[i])*parseInt(s[i]);
    }   
    return sum;
    
}



// var isHappy = function(n) {
//     var sum = 0;
//     var map = new Map();
  
//     while(true) {
//       if (n === 1) {
//         return true;
//       }
//       if (map.has(n)) {
//         return false;
//       }
//       else {
//         map.set(n, n);
//       }
  
//       sum = 0;
//       while(n !== 0) {
//         sum += Math.floor(n % 10) * Math.floor(n % 10);
//         n = Math.floor(n / 10);
//       }
  
//       n = sum;
//     }
//   };



console.log(isHappy(19))
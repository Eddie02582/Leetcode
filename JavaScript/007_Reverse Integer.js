
var reverse = function(x) {
  
    var reverse = 0;    
    while(x)
    {
        reverse = reverse*10 + x%10;
        x = parseInt(x/10);
    }
    
    //return flag == true ? reverse : reverse*-1;
    if (reverse > 2**31 - 1 || reverse < -1*2**31)
        return 0
    return reverse 
};


console.log(reverse(-123))
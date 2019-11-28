
var isPalindrome = function(x) {
    if (x < 0 )
        return false;
    x = x.toString();
    length = Math.floor(x.length/2);
    for (var i = 0 ; i <length ;i++)
    {
        if (x[i] != x[x.length - 1 - i])
            return false;
        
    }
    return true;
    
    
};


var isPalindrome_reverse_Intger = function(x) {
    if (x < 0 )
        return false;
    var reverse = 0 ;
    var n = x 
    while(n)
    {
        reverse = reverse*10 + n%10;
        n = Math.floor(n/10);
    }
    return x == reverse;
    
};


var isPalindrome_reverse = function(x) {
    return x == x.toString().split('').reverse().join('');
};

isPalindrome(10);


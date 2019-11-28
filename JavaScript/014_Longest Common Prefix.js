var longestCommonPrefix = function(strs) {
    if (strs.length == 0)
        return "";
    else if (strs.length == 1 )
        return strs[0];
    
    
    strs.sort();
    var minlength =    strs[0].length > strs[strs.length - 1].length ?  strs[strs.length - 1].length: strs[0].length ;
    var result = ""
    for (var i = 0; i < minlength;i++){
        if (strs[0][i] != strs[strs.length - 1][i])
            break
        result += strs[0][i];
        
    }    
    return result;
};


longestCommonPrefix([])
var longestCommonPrefix = function(strs) {
    if (strs.length == 0)
        return "";
    else if (strs.length == 1 )
        return strs[0];    
    
    strs.sort();
    var p = 0 , lastindex = strs.length - 1
    var s = ""  
    while (p < strs[0].length && p < strs[lastindex].length){
        if (strs[0][p] != strs[lastindex][p]){
            break
        }
        s += strs[0][p++]     
    }   
    
  
    return s;
};




longestCommonPrefix([])
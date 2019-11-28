var isValid = function(s) {
    var match = {  ")":"(",
                   "]":"[",
                   "}":"{",
                };
    var result = [];
    for (var i = 0 ; i< s.length ; i++){
        //if (!(s[i] in match)){
        if (! match.hasOwnProperty(s[i])){  
            result.push(s[i]);
        }
        else if ( result.pop() != match[s[i]])
            return false;          
  
            
        
    }
    return result.length == 0;
    
};


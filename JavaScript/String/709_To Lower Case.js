var toLowerCase_inbuid = function(str) {
    return str.toLowerCase()
};


var toLowerCase = function(str) {
    var lower = "";
    for (var i = 0 ; i< str.length;i++){
        var n = str[i].charCodeAt();
        if (n >= 65 && n <=90) n += 32;                                 
        lower += String.fromCharCode(n);    
    }
    return lower
};

toLowerCase("Hellow")
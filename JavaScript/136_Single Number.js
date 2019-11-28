
/* var singleNumber = function(nums) {
    var output = 0 ; 
    
    for (var i = 0 ; i<nums.length ;i++)    
        output = output^nums[i]; 
    return output;
    
};
 */

var singleNumber = function(nums) {
    var output = 0 ; 
    nums.forEach(n => {
        
        output ^= n
    }); 
    return output;
    
};

console.log(singleNumber([2,2,1]))
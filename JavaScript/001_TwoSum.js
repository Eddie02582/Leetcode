
 var twoSum = function(nums, target) {
    var data = {};
    for(var i = 0 ; i < nums.length ; i++)
    {
        if( data[target- nums[i]] >= 0)
        {
            return [data[target - nums[i]],i];
        }
        data[nums[i]] = i
        
    }   
    
    
};


console.log(twoSum([2, 7, 11, 15],9))
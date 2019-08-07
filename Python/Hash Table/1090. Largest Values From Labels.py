'''

We have a set of items: the i-th item has value values[i] and label labels[i].

Then, we choose a subset S of these items, such that:

|S| <= num_wanted
For every label L, the number of items in S with label L is <= use_limit.
Return the largest possible sum of the subset S.

 

Example 1:

    Input: values = [5,4,3,2,1], labels = [1,1,2,2,3], num_wanted = 3, use_limit = 1
    Output: 9
    Explanation: The subset chosen is the first, third, and fifth item.
Example 2:

    Input: values = [5,4,3,2,1], labels = [1,3,3,3,2], num_wanted = 3, use_limit = 2
    Output: 12
    Explanation: The subset chosen is the first, second, and third item.

'''


class Solution(object):
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type num_wanted: int
        :type use_limit: int
        :rtype: int
        """
        score = {}
        for v,l in zip(values,labels):
            if l not in score:
                score[l] = [v,]
            else:
                score[l].append(v)
            
        limit,count,total = 0,0,0,        
        for key in score.keys():
            limit = 0            
            for value in score[key]:                             
                if limit < use_limit and count < num_wanted:
                    total += value
                    print (value)
                    count += 1
                    limit += 1
            if count == num_wanted:
                break
        return total
 
sol = Solution()
 
#assert sol.largestValsFromLabels([5,4,3,2,1],[1,1,2,2,3],3,1) ==9
 
assert sol.largestValsFromLabels([5,4,3,2,1],[1,3,3,3,2],3,2) == 12 
 
#assert sol.largestValsFromLabels([9,8,8,7,6],[0,0,0,1,1],3,1) ==16
 
#assert sol.largestValsFromLabels([9,8,8,7,6],[0,0,0,1,1],3,2) == 24
 
 
 
 
 
 
 
 
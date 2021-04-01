# Combination Sum

## 原題目:
```
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

    Input: candidates = [2,3,6,7], target = 7,
    A solution set is:
    [
      [7],
      [2,2,3]
    ]
Example 2:

    Input: candidates = [2,3,5], target = 8,
    A solution set is:
    [
      [2,2,2,2],
      [2,3,3],
      [3,5]
    ]


```



## 思路backtracking


#### Python


``` python
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtracking(array,start,total):
            if total == 0 :
                res.append(array[:])
                return
            elif total < 0 :
                return
            for i in range (start,len(candidates)): 
                n = candidates[i]              
                backtracking(array + [n],i,total - n)

        res = []    
        backtracking([],0,target)    
        return res     
           
``` 

#### C#

```csharp
public class Solution {
    public IList<IList<int>> CombinationSum(int[] candidates, int target) {
        IList<IList<int>> ans = new List<IList<int>>();
        backtracking(candidates,0,new List<int>(),target,ans);
        return ans;
    }
    public void backtracking(int[] candidates,int index,IList<int>path,int path_res,IList<IList<int>> ans){
        if (path_res < 0)
            return;        
        else if (path_res == 0){
            ans.Add(path);
            return;
        }        
        for (int i = index; i < candidates.Length; i ++ )
        {
            path.Add(candidates[i]);
            backtracking(candidates,i,new List<int>(path),path_res - candidates[i],ans);
            path.RemoveAt(path.Count() - 1);
        }   
    }
}
```









## 思路DP
#### python
``` python
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        dp = defaultdict(set)        
        dp[0].add(())
        for n in candidates:
            for i in range(n, target + 1):                
                for seq in dp[i - n]:
                    dp[i].add(seq+(n,))
        return dp[target]            
           
``` 



#### C#

```csharp
public class Solution {
    public IList<IList<int>> CombinationSum(int[] candidates, int target)
    {

        //   0	 1	 2	 3	  4	      5	       6	              7
        //2	 []		[2]		[2,2]		    [2,2,2]	
        //3	 []		[2]	[3]	[2,2]	[2,3]	[3,3],[2,2,2]	    [2,2,3]
        //6	 []		[2]	[3]	[2,2]	[2,3]	[3,3],[2,2,2],[6]	[2,2,3]
        //7								                        [2,2,3],[7] 

        IList<IList<int>> ans = new List<IList<int>>(); 
        List<IList<IList<int>>> dp = new List<IList<IList<int>>>();
           //initial
        for (int j = 0; j <= target ; j++)
        {
            dp.Add(new List<IList<int>>());
        }

        foreach (int candidate in candidates)
        {
            for (int j = candidate; j <= target; j++)
            {
                if (candidate == j)
                {
                    List<int> d = new List<int>();
                    d.Add(candidate);
                    dp[j].Add(d);
                }
                foreach (List<int> q in dp[j - candidate])
                {                        
                    var add = new List<int>(q);
                    add.Add(candidate);
                   dp[j].Add(add);
                }
            }
        }
        return dp[target];

    }
}
```










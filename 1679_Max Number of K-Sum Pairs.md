# Max Number of K-Sum Pairs

## 原題目:
```
You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

Example 1:
	Input: nums = [1,2,3,4], k = 5
	Output: 2
	Explanation: Starting with nums = [1,2,3,4]:
	- Remove numbers 1 and 4, then nums = [2,3]
	- Remove numbers 2 and 3, then nums = []
	There are no more pairs that sum up to 5, hence a total of 2 operations.
	
	
Example 2:
	Input: nums = [3,1,3,4,3], k = 6
	Output: 1
	Explanation: Starting with nums = [3,1,3,4,3]:
	- Remove the first two 3's, then nums = [1,4,3]
	There are no more pairs that sum up to 6, hence a total of 1 operation.

Constraints:
	1 <= nums.length <= 105
	1 <= nums[i] <= 109
	1 <= k <= 109


```

## 雙指針法

我們可以使用雙指針法來解決這個問題，首先需要對數組進行排序。然後，我們設置兩個指針，分別指向數組的起始和結束位置，根據當前指針的元素之和與 k 的關係來調整指針。

步驟：
<ol>
	<li>排序數組：將數組按升序排序，這樣就可以使用雙指針技術。</li>
	<li>使用雙指針：設置一個指向數組開頭的指針 left 和一個指向數組末尾的指針 right。</li>
	<li>根據當前和判斷指針移動
		<ul>
			<li>如果 nums[left] + nums[right] == k，則這是一個有效的配對，增加結果計數，並移動兩個指針，分別向內移動。</li>
			<li>如果 nums[left] + nums[right] < k，則需要增大總和，將 left 指針向右移動。</li>
			<li>如果 nums[left] + nums[right] > k，則需要減小總和，將 right 指針向左移動。</li>
		</ul>
	</li>
	<li>終止條件：當 left 超過或等於 right 時，停止循環。</li>
</ol>



``` c++
class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        sorted(nums.begin(),nums,end());
		int left = 0,right = nums.size() - 1;
		int count = 0;
		while(left < right){
			int sum = nums[left] + nums[right];
			if(sum == k){
				count++;
				left++;
				right--;
			}
			else if(sum > k){
				right--;
			}
			else if(sum < k){
				left++;
			}			
		}
		
		return count;
		
    }
};
```

## 使用map


``` c++
class Solution {
public:
   int maxOperations(vector<int>& nums, int k) {
    unordered_map<int, int> count;
    int operations = 0;

    for (int num : nums) {
        int complement = k - num;
        
        // 如果 complement 在哈希表中，并且它的计数大于 0
        if (count[complement] > 0) {
            operations++;
            count[complement]--;
        } else {
            count[num]++;
        }
    }

    return operations;
}
};

```










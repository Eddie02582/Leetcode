class NumArray:

    def __init__(self, nums: List[int]):
        self.nums =nums
        self.sum = [0]
        for index,n in enumerate(self.nums):
            if index == 0 :
                self.sum.append(n)
            else:
                self.sum.append(n + self.sum[-1])
        
        

    def sumRange(self, i: int, j: int) -> int:
        return  self.sum [j+1] - self.sum[i]
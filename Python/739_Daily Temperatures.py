'''
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

'''


class Solution(object):
    #timeout
    def dailyTemperatures_(self, T):
        array = [0]*len(T)
        for i in range(0,len(T)):
            for j in range(i+1,len(T)):
                if T[j] > T[i]:
                    array[i] = j - i
                    break
        return array
                
    def dailyTemperatures_statck(self, T):
        N = len(T)
        stack = []
        res = [0] * N
        for i, t in enumerate(T):
            while stack and stack[-1][0] < t:
                oi = stack.pop()[1]
                res[oi] = i - oi
            stack.append((t, i))
        return res

    def dailyTemperatures(self, T):
        ans = [0] * len(T)
        stack = [] 
        for i in range(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans


sol = Solution()

assert sol.dailyTemperatures( [73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
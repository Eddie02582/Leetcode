class Solution:
    def removeKdigits_(self,num,k):
        if k > len(num):
            return "0"

        count = 0        
        while count < k and num:      
            isFind = False
            for i in range(len(num) - 1):
                if int(num[i]) > int(num[i + 1]):
                    isFind = True
                    num = num[0 : i] + num[i + 1:]
                    count += 1
                    break
            if not isFind:
                break
        while  count < k and num:         
            num = num[0:-1]
            count += 1   
        if not num:
            return "0"

        return str(int(num))

    def removeKdigits(self,num,k):
        if k > len(num) or not num:
            return "0"

        stack,count = [],0        
 
        for s in num:           
            n = int(s)
            while stack and int(stack[-1]) > n and count < k:
                stack.pop()
                count += 1                  
            stack.append(s) 

        while stack and stack[0] == "0":
            stack.pop(0)

        while stack and count < k:
            count += 1
            stack.pop()
    
        return "".join(stack) if stack else "0"

    def removeKdigits(self, num: str, k: int) -> str:  
        newLength = len(num) - k
        stack = [0] * len(num)
        top = 0
        for i in range(len(num)):
            c = int (num[i])
            while top > 0 and int (stack[top - 1]) > int (num[i]) and k >0:
                top -= 1
                k -= 1

            stack[top] = num[i]
            top += 1

        offset = 0

        while offset < newLength and stack[offset] == '0':
            offset += 1
    
        return "0" if offset == newLength else "".join(stack[offset: newLength])


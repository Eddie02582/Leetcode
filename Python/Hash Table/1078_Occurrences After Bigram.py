class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        arr = text.split()
        data = [first,second]
        result = []
        for i in range(len(arr) - 2):
            if arr[i:i+2] == data:
                result.append(arr[i+2])
            
        return result
            
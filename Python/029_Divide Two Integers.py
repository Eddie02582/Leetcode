class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        if not divisor or (dividend == -2**31 and divisor == - 1) or (dividend == 2**31 and divisor == 1):
            return 2**31 - 1
        
        result = 0
        sign =  dividend * divisor < 0 
        dividendabs  = abs(dividend)
        divisorabs  = abs (divisor)
        while divisorabs <= dividendabs:
            temp ,doubles = divisorabs ,1   
            while (temp << 1) <= dividendabs:
                temp <<= 1
                doubles <<= 1            
            dividendabs -= temp;
            result += doubles;
        return  - 1 * result  if sign  else result
        
    def divide__shift(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        if not divisor or (dividend == -2**31 and divisor == - 1) or (dividend == 2**31 and divisor == 1):
            return 2**31 - 1

        dividendabs  = abs(dividend)
        divisorabs  = abs (divisor)        
        maxShiftDigit = 0
        while  divisorabs << maxShiftDigit <= dividendabs:
            maxShiftDigit += 1

        sign,result  =  dividend * divisor < 0,0

        for i in range(maxShiftDigit - 1 , - 1 ,-1):
            shiftValue = divisorabs << i
            if shiftValue <= dividendabs:
                result += (1 << i);
                dividendabs -= shiftValue;

        return  - 1 * result  if sign  else result        
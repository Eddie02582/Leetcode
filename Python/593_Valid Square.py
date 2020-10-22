class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """

        l1,l2,l3,l4 = sorted([p1,p2,p3,p4])       
        
        #4 sides are equal and Diagonal equal and length != 0
        return self.getDistance(l1,l2) == self.getDistance(l2,l4) == self.getDistance(l3,l1) == self.getDistance(l3,l4) and self.getDistance(l1,l4) == self.getDistance(l2,l3) and self.getDistance(l1,l2) != 0
    
    def getDistance(self,p1,p2):   
        return (p1[0]- p2[0])**2 + (p1[1]- p2[1])**2

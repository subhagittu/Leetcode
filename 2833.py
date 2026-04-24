class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        x, r=0, 0
        for c in moves:
            x+=(c=='R')-(c=='L')
            r+=c=='_'
        return abs(x)+r
        

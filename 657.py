class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if len(moves) & 1: return False
        x = y = 0

        for c in moves:
            y += (c == 'U') - (c == 'D')
            x += (c == 'R') - (c == 'L')

        return not x and not y
        

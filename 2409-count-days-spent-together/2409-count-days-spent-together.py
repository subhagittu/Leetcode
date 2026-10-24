class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        return max(0, self.getDate(min(leaveAlice, leaveBob)) - self.getDate(max(arriveAlice, arriveBob)) + 1)
    
    def getDate(self, date):
        monthList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        month = int(date[:2])
        days = int(date[3:])
        return sum(monthList[: month - 1]) + days
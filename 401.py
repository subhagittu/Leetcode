class Solution(object):
    def readBinaryWatch(self, turnedOn):
        if turnedOn > 8:
            return []

        ans = []

        for hour in range(0,12):
            for minute in range(0,60):
                if bin(hour).count('1') + bin(minute).count('1') == turnedOn:
                    ans.append(str(hour)+ ":" + str(minute).zfill(2))

        return ans
        

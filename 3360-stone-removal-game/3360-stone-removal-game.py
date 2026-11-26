class Solution:
    def canAliceWin(self, n: int) -> bool:
        t, pile = 0, 10

        while n >= pile:
            n -= pile
            pile -= 1
            t ^= 1

        return bool(t & 1)
#translated using AI
class Fancy:

    def __init__(self):
        self.arr = []
        self.mul = 1
        self.add = 0
        self.MOD = 10**9 + 7

    def power(self, a, b):
        res = 1
        a %= self.MOD
        while b > 0:
            if b & 1:
                res = (res * a) % self.MOD
            a = (a * a) % self.MOD
            b >>= 1
        return res

    def modInverse(self, x):
        return self.power(x, self.MOD - 2)

    def append(self, val: int) -> None:
        stored = ((val - self.add + self.MOD) % self.MOD * self.modInverse(self.mul)) % self.MOD
        self.arr.append(stored)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % self.MOD
        self.add = (self.add * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.arr):
            return -1
        ans = (self.arr[idx] * self.mul) % self.MOD
        ans = (ans + self.add) % self.MOD
        return ans

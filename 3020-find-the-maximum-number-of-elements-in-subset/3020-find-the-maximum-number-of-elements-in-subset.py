class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mp = {}

        for x in nums:
            mp[x] = mp.get(x, 0) + 1

        ans = 1

        for x in nums:
            if x == 1:
                if mp[x] % 2:
                    ans = max(ans, mp[x])
                else:
                    ans = max(ans, mp[x] - 1)
            else:
                ct = 0

                if mp[x] >= 2:
                    curr = x

                    while curr <= 2**31 - 1 and curr in mp:
                        if mp[curr] == 1:
                            ct += 1
                            break

                        ct += 1

                        if curr > (2**63 - 1) // curr:
                            break

                        curr *= curr

                ans = max(ans, ct * 2 - 1)

        return ans
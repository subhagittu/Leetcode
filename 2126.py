class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        xmax = max(asteroids)
        freq = [0]*(xmax+1)
        for x in asteroids:
            freq[x] += 1

        planet = mass
        for x,f in enumerate(freq):
            if f == 0:
                continue
            if x > planet:
                return False

            planet += x*f

        return True

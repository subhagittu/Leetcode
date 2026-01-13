class Solution(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """
        total_area = 0
        events = []

        for _, y, l in squares:
            total_area += l * l
            events.append((y, l, 1))
            events.append((y + l, l, -1))

        events.sort(key=lambda x: x[0])

        covered_width = 0.0
        curr_area = 0.0
        prev_height = events[0][0]

        for y, l, delta in events:
            diff = y - prev_height
            area = covered_width * diff

            if covered_width > 0 and 2 * (curr_area + area) >= total_area:
                return prev_height + (total_area - 2 * curr_area) / (2 * covered_width)

            covered_width += delta * l
            curr_area += area
            prev_height = y

        return prev_height
        

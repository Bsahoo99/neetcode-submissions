class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(k):
            total_hours = 0 

            for p in piles: 
                hours = (p + k - 1)//k
                total_hours += hours

            return total_hours <= h

        l = 1
        r = max(piles)

        while l < r:
            m = (l + r) // 2

            if can_finish(m):
                r = m 
            else:
                l = m + 1
        return l                   
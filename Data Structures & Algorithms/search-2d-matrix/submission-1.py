class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        r = len(matrix)
        c = len(matrix[0])

        l = 0 
        r = r * c - 1

        while l <= r:
            m = (l + r) // 2
            rows = m // c
            cols = m % c

            value = matrix[rows][cols]

            if value == target:
                return True 
            elif value < target:
                l = m + 1
            else:
                r = m - 1
        return False                
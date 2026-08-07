class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # n = len(temperatures)
        # l = 0 
        # r = l + 1 
        # ans = []
        # while l :
        #     if l > r: 
        #         r += 1
        #         ans.add(0)
        #     else:
        #         ans.add(r-l)
        #         l += 1
        # return ans      

        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack [-1][0]:
                stackT,stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t,i])
        return res                   
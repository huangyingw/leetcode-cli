class Solution(object):
    def permute(self, nums):
        def dfs():
            if len(current) == len(nums):
                result.append(list(current))
            for index in range(len(nums)):
                if not visited[index]:
                    visited[index] = True
                    current.append(nums[index])
                    dfs()
                    current.pop()
                    visited[index] = False
        nums.sort()
        visited = [False for _ in range(len(nums))]
        current = []
        result = []
        dfs()
        return result


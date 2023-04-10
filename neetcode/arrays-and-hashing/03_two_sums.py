class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for i, num in enumerate(nums):
            if num in ans:
                return [ans[num], i]
            else:
                ans[target - num] = i

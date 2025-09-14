class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in num_map:
                return [num_map[need], i]
            num_map[num] = i
        return []

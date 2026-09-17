class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp_dict = dict()
        for pos, val in enumerate(nums):
            comp = target - val
            if val in comp_dict:
                return [comp_dict[val], pos]
            comp_dict[comp] = pos

        
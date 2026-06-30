class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in num_dict: return [num_dict[diff], idx]
            num_dict[num] = idx
            
        

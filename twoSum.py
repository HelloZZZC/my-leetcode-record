class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data_dict = {}
        for index in range(len(nums)):
            data_dict[nums[index]] = index

        for index in range(len(nums)):
            key = target - nums[index]
            if key in data_dict.keys() and data_dict[key] != index:
                return [index, data_dict[key]]

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 1
        previous_value = nums[0]
        max_count = 0
        for i in range(len(nums)-1):
            if (previous_value == nums[i+1]):
                count += 1
            else:
                if (max_count < count):
                    max_count = count
                    count = 0
            previous_value = nums[i+1]
        return max_count

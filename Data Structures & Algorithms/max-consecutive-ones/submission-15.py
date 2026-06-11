class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = max_count = 0
        for num in nums:
            if num:
                count += 1
                if max_count < count:
                    max_count = count
            else:
                count = 0
        return max_count
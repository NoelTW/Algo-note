class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        xor = 0
        for x in range(len(nums) + 1):
            xor ^= x 
        
        for y in nums:
            xor ^= y 

        return xor
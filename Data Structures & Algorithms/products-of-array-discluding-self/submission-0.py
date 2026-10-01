class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        # Store product of everything to the left
        left_product = 1
        for i in range(n):
            output[i] = left_product
            left_product *= nums[i]

        # Multiply by product of everything to the right
        right_product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]

        return output
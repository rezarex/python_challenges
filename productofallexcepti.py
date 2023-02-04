class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        productArr = [1 for i in range(len(nums))]
        product = 1

        for i in range(len(nums)):
            productArr[i] = productArr[i] * product
            product = product * nums[i]
        
        product = 1

        for j in reversed(range(len(nums))):
            productArr[j] = productArr[j] * product
            product = product * nums[j]

        return productArr
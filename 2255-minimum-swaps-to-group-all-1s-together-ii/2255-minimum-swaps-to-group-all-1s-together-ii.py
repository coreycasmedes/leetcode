class Solution:

    def circular_slice(self, nums, start, length):
        return [nums[(start + i) % len(nums)] if start + i >= len(nums) else nums[start+i] for i in range(length)]

    def minSwaps(self, nums: List[int]) -> int:
        ones_count = sum(nums)
        i = 0
        j = ones_count
        
        window_sum = sum(nums[:ones_count])
        largestc = window_sum

        for i in range(len(nums)):
            end_indx = (i + ones_count) % len(nums) if i + ones_count >= len(nums) else i + ones_count
            window_sum = window_sum + nums[end_indx] - nums[i]
            largestc = max(largestc, window_sum)
            i+=1
        return ones_count-largestc
        

        # while i < len(nums):
        #     j = (i + ones_count)
        #     if j >= len(nums):
        #         j %= ones_count
        #     # find largest concentration of ones
        #     largestc = max(largestc, sum(self.circular_slice(nums, i, ones_count)))
        #     i += 1
        # return ones_count - largestc

            




          
        
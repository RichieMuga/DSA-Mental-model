# Implement sliding window technique
class SlidingWindow:
    def __init__(self, target, nums):
        self.target = target
        self.nums = nums

    def sliding_window(self):
        # counter rep the largest possible value
        # l rep the left counter
        counter, l = float('inf'), 0
        
        # rep the total subarray
        total = 0

        # starting from the right counter
        for r in range(len(self.nums)):
            # add the total values when we increase the right value and store it
            total += self.nums[r]
            # while we have not exceeded the target with our total
            while self.target < total:
                # we check the minimum continous subarray
                counter = min(counter, r-l+1)
                # we then remove the left most value
                total -= self.nums[l]
                # then increase the pointer
                l+=1
        return counter
         



# Goal: to implement a dynamic sliding window technique
# What the question? or specifics?
# You are given an array nums with a target
# find the highest number of sub array that is not more than the target
# return the longest continiuos sub array

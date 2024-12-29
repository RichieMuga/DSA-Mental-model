class SlidingWIndow:
    def __init__(self, nums, targetSum):
        self.nums = nums
        self.targetSum = targetSum

    def sliding_window(self):
        l = 0
        # allocate the biggest number posiible
        leastSubArray = float('inf')
        total = 0

        for r in range(len(self.nums)):
            # increase the right pointer
            total += self.nums[r]

            # while the totat is greater than the target sum, if its long enough, we move the left pointer
            while total >= self.targetSum:
                # get the minimum subArray between the current one and the one being checked
                leastSubArray = min(leastSubArray, r - l + 1)
                # remove the the left part
                total -= self.nums[l]
                # add the left pointer
                l += 1

        return leastSubArray

        # check the loop and try to add the first index to the following indexuuuuuu        # if the targetSum is not exceeded
        # increase the pointer r and then recalculate the sum from the pointer l all the way to where the current r is at 


class Solution:
    def __init__(self, nums):
        self.nums = nums 

    def reset(self):
        return self.nums

    def shuffle(self):
        array = self.nums
        random.shuffle(array)
        return array

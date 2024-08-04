class Subsetter:
    def __init__(self, nums):
        self.nums = nums
    
    def get_subsets(self):
        self.result = []
        self.backwards(0, [])
        return self.result
    
    def backwards(self, index, current):
        self.result.append(current[:])
        
        for i in range(index, len(self.nums)):
            current.append(self.nums[i])
            self.backwards(i + 1, current)
            current.pop()

generator = Subsetter([4, 5, 6])
subsets = generator.get_subsets()
print(subsets)

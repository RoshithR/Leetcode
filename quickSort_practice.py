
class QuickSort:
    def __init__(self, nums):
        self.nums = nums

    def sort(self):
        self.quick_sort(0, len(self.nums)-1)

    def quick_sort(self, low, high):
        if low>=high:
            return
        pivot = self.partition(low,high)
        self.quick_sort(low, pivot-1)
        self.quick_sort(pivot+1,high)

    def partition(self, low, high):
        pivot_index = (low+high)//2
        self.nums[pivot_index], self.nums[high] = self.nums[high], self.nums[pivot_index]
        for i in range(low, high):
            if self.nums[i]<=self.nums[high]:
                self.nums[low], self.nums[i] = self.nums[i], self.nums[low]
                low+=1
        self.nums[high], self.nums[low] = self.nums[low], self.nums[high]
        return low

if __name__ == "__main__":
    nums=[-1,-2,-7,9,4,5,6,2]
    qs = QuickSort(nums)
    qs.sort()
    print(nums)

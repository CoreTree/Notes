class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        while r > l:
            mid = (r + l) // 2
            print(mid, l, r)
            if nums[mid] < nums[l]:
                l = mid + 1
            if nums[mid] > nums[r]:
                r = mid - 1
        return (r + l) // 2

sol = Solution()
nums = [3, 4, 5, 6, 1, 2]
ret = sol.findMin(nums)
print(ret)

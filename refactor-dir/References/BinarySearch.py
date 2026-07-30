class Solution:
	def search(self, nums:list[int], target:int) -> int:
		l, r = 0, len(nums) - 1
		mid = r // 2
		while r > l:
			mid = (r + l) // 2
			print("MID:", mid, "| LEFT:", l, "| RIGHT:", r)
			if nums[mid] > target:
				r = mid - 1
			if nums[mid] < target:
				l = mid + 1
			if nums[l] == target:
				return l
			if nums[r] == target:
				return r
		return -1

sol = Solution()
nums = [-1, 0, 2, 4, 6, 8]
target_a = 4
target_b  = 3

print("TARGET_A:", sol.search(nums, target_a))
print("TARGET_B:", sol.search(nums, target_b))
print("TARGET_C:", sol.search([-1,0,3,5,9,12], 4))

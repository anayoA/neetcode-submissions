class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checked_nums = set()
        for n in nums:
            if n in checked_nums:
                return True
            checked_nums.add(n)
        return False

        
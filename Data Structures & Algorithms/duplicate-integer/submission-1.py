class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checked_nums = set()
        duplicate = False
        for n in nums:
            if n in checked_nums:
                duplicate = True
            checked_nums.add(n)
        return duplicate

        
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       # 1. make an empty set, use it to filter out duplicates from given list
       # 2. iterate through given list and use set.add() to add each each element from
       # original list to the set -- O(N) time due to going through list length of N
       # 3. Compare the lengths of list and set, if length is same return False (no duplicates),
       # otherwise return true (Duplicates exist)

       nums_set = set()
       for val in nums:
        nums_set.add(val)

       if len(nums) != len(nums_set):
        return True
  
       return False


        
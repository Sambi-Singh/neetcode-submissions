class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #1. intialize a dictionary to hold the actual numbers as keys, and indices of said numbers as values
        indexDict = {}

        #2.iterate through the nums list and add key value pairs to indexDict
        for i in range(len(nums)):
            indexDict[nums[i]] = i
        
        #3. Iterate again! But this time find the complement on each iteration and 
        # check to see if the complement exists in our established dictionary, and IT DOES NOT SHARE SAME INDEX AS CURRENT ITERATION
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in indexDict and indexDict[complement] != i:
                return [i, indexDict[complement]]
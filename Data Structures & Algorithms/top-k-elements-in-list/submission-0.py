class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #1. setup hashmap and list
        count = {} # hashmap to keep track of number freuqencies in input list
        freq = [[] for i in range(len(nums)+1)] # list full of empty buckets or lists
        # MAKE SURE TO ADD + 1, since indicies are 0 indexed and used for counting frequency

        #2. count occurences
        for n in nums:
            #.get get() dict method that checks if n is a key and returns current count, if not return 0
            # adding 1 to it so every number is accounted for
            count[n] = 1 + count.get(n,0) 
        
        #3. fill in the buckets
        for n, c in count.items(): # loop through key value pairs in hashmap
            freq[c].append(n) # actual bucket sort logic
            # tap into freuqency array and use the count as the INDEX, appened the actual number or 
            #value to that list specified by index
        
        #4. gather top k elements
        res = []
        #Move backwards 1 step at a time through the array range(start, stop, step)
        for i in range(len(freq) - 1, 0, -1):
            #Only look through buckets with numbers inside of them
            for n in freq[i]:
                res.append(n) #append once a number found in bucket
                if len(res) == k: #stop once k elements found!
                    return res

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #1st check to see if the length of the strings are the same, of not return False
        # since that means they DO NOT have exact same characters ie not anagrams
        if len(s) != len(t):
            return False
        
        #2. check to see if the characters in s are same as t, do this by keeping track of 
        #  the frequency of each character in the string

        #3. intialize a dictionary for each string
        s_count = {}
        t_count = {}
        
        s_keys = s_count.keys()
        t_keys = t_count.keys()

        #4. iterate through each string and add the counts of each character to each dict
        for char in s:
            if char in s_keys:
                s_count[char] += 1
            else:
                s_count[char] = 1
        
        for char in t:
            if char in t_keys:
                t_count[char] += 1
            else:
                t_count[char] = 1
        
        #5. Compare the dicts of s and t holding the frequencies
        # of characters in each respective string. If they are the same. return true, else false
        if s_count == t_count:
            return True
        return False
        


        
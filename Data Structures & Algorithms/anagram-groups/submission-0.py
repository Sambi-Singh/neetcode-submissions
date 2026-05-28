class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # MAKE SURE to use defaultdict(list) !! This way fix the edge case dealing with empty character counts, pass in list
        # as the parameter to ensure that if no key present a list is added inside instead, so like ['[]']
        result = defaultdict(list) # mapping charCount to list of anagrams
        # loop through input strings in list
        for inputString in strs:
            charCount = [0] * 26 #intialize list with characters a .. z being represented by speicifc positon indicies (o=a, 1=b, etc)

            # looping thrugh characters of 1 specific input string
            for currChar in inputString:
                charCount[ord(currChar) - ord('a')] += 1

                # a = 80, the we get index 0 when 8- - 80 = 0
            result[tuple(charCount)].append(inputString) # make sure to convert count to a tuple! Since lists are mutable and cant serve as keys to dict
        return list(result.values()) #instructions want return value as LIST not DICT, so typecast to list via list()
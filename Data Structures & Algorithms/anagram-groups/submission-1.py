class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 

        result = {}
        
        for s in strs:
            sorted_string = ''.join(sorted(s))
            if sorted_string in result.keys():
                result[sorted_string].append(s)
            else:
                result[sorted_string]=[s]
        
        return list(result.values())


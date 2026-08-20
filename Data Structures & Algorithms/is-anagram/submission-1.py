class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        lst1=[]
        lst2=[]
        for c in s:
            lst1.append(c)
        for c in t:
            lst2.append(c)
        lst1=sorted(lst1)
        lst2=sorted(lst2)
        return lst1==lst2
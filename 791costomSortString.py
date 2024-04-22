from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        countc = Counter(s)

        sort_c = []

        for char in order:
            sort_c.append(char*countc[char])
            countc[char] = 0

        for char, count in countc.items():
            sort_c.append(char*count)
        
        return''.join(sort_c)
        

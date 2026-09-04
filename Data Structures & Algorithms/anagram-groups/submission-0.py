class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = defaultdict(list)

        for stri in strs:
            ans[''.join(sorted(stri))].append(stri)

        return list(ans.values())
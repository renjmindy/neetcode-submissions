class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mp = defaultdict(list)

        for str in strs:
            ordered_str = sorted(str)
            mp[''.join(ordered_str)].append(str)

        return list(mp.values())
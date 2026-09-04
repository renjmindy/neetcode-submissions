class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        ans = list()
        mp = Counter(chars)
        found = False

        for word in words:
            mp = Counter(chars)
            np = Counter(word)
            found = False
            for k, v in np.items():
                print(k, v, found)
                if k not in mp: found = True; break
                else: 
                    if mp[k] >= v: mp[k] -= v
                    else: found = True; break
            if not found: ans.append(word)

        return sum([len(word) for word in ans])
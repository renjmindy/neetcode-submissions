class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize: return False

        hand.sort()

        mp = Counter(hand)

        for card in hand:
            if mp[card] == 0: continue
            for r in range(groupSize):
                if mp[card + r] == 0: return False
                mp[card + r] -= 1

        return True


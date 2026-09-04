class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        cnt, ans = sum(cardPoints[:k]), sum(cardPoints[:k])

        for r in range(k):
            cnt -= cardPoints[k - 1 - r] # delete head
            cnt += cardPoints[len(cardPoints) - 1 - r] # add tail
            ans = max(ans, cnt)

        return ans
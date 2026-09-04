class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        if target in triplets: return True

        ans = [0] * len(target)

        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                for r in range(3):
                    ans[r] = max(ans[r], triplet[r])

            if ans == target: return True


        return False

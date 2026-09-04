class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ans = list()

        for r in range(len(nums1)):
            idx = nums2.index(nums1[r])
            if idx < len(nums2) - 1: 
                maxVal = max(nums2[idx + 1:])
                if maxVal > nums1[r]:
                    for l in range(idx + 1, len(nums2)):
                        if nums2[l] > nums1[r]:
                            ans.append(nums2[l])
                            break
                else: ans.append(-1)
            else: ans.append(-1)

        return ans

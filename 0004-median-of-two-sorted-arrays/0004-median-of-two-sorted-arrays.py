class Solution:

  def findMedianSortedArrays(self, nums1: list[int], nums2:
     list[int]) -> float:

     
    # Merge and sort
    merged = sorted(nums1 + nums2)
    n = len(merged)

    # If even length, average of two middle numbers
    if n % 2 == 0:
      return (merged[n // 2 - 1] + merged[n // 2]) / 2.0
    # If odd length, exact middle number
    else:
      return float(merged[n // 2])
            



      

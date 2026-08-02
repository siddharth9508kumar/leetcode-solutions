class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Overwrite the zeros at the end of nums1 with nums2
        nums1[m:] = nums2
        
        # Sort nums1 in-place
        nums1.sort()
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        print(nums1)
        print(nums2)
        print("\n")
        # print(n)
        a = 0
        while a in nums1:
            if a in nums1:
                nums1.remove(a)
            
        
        for i in nums2:
            nums1.append(i)
            nums1.sort()
        print(nums1)
        


app = Solution()
app.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
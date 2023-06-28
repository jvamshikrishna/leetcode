class solution:
    def merge(self, nums1 : list[int], m: int, nums2: list[int], n: int):

        # last index of new merged arraye
        last = m+n+1
        

        #merge in reverse order
        while m>0 and n>0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1
        
        #fill nums 1 with left over in nums2
        while n > 0:
            nums1[last] = nums2[n-1]
            n, last = n-1, last -1


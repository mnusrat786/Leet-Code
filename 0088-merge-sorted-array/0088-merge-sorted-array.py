class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
       """
        merge = nums1[:m] + nums2[:n]
        merge.sort()
        # for i in range(len(merge)):
        #     nums1[i]=merge[i]
        # merge = [1,2,2,3,5,6]

        # nums1= [1,2,3,0,0,0]

        # for i in range(6)  i=0 nums1[0]= merge[0]  nums1[0]=1
        # i=1 nums1[1]= merge[1]  nums1[1] = 2
        # i=2 nums1[2]=merge[2]   nums1[2] = 2
        # i=3 nums1[3]=merge[3]   nums1[3] = 3
        # i=4 nums1[4]=merge[4]   nums1[4]= 5
        # i=5 nums1[5]=merge[5]   nums1[5]= 6
        # nums1= [1,2,2,4,5,6]
        #second way
        nums1[:len(merge)]=merge

     
        








# nums1 = [1, 0, 2, 0, 0]  m=3
# nums 2 = [0,1,0,0,0,2]
# nums1 = [0]
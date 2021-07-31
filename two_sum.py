""" get sum of two number from a given array return two number index"""
from typing import List
#first approach
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        #  complexity o(n*n) 
        end = len(nums)
        for i in range(end):
            sum = 0 # hold the two number sum
            for j in range(end):
                
                if (j>i):
                    sum = nums[i] + nums[j]
                    if(sum == target):
                        return [i, j]

    
    def twoSumCom(self, nums: List[int], target: int) -> List[int]: 
      #  complexity o(nlogn)
      end = len(nums)
     
      for i in range(end):
          sum = abs(target - nums[i])
          nums.sort()
          s_index = self.binarySearch(sum, end, nums)
          if(s_index != -1):
              
              return [i, s_index]
          sum = 0

    def binarySearch(self, data : int, end :int , nums: List[int])->int:
        print(nums)
        first_index = 0 # this is start index of list
        last_index = end - 1 # this is last index of list
        while (first_index < last_index): # true until o < 3
            mid = (first_index+last_index)//2 # mid (0+3)// 2 this take 1 { floor division // rounds}
            if(data == nums[mid]): 
                return mid
            elif(data < nums[mid]):
                last_index = mid -1
            else:
                first_index = mid +1
        return -1

    def twoSumCheck(self, nums: List[int], target: int) -> List[int]:
        #  complexity o(n) 
        check = set()
        for i in range(len(nums)):
            
            if nums[i] in check:
                return [nums.index(target - nums[i]), i]
            else:
                
                check.add(target - nums[i])



soln_obj = Solution()
print(soln_obj.twoSumCheck([100,200,40,30,29,47,89,3864,848484,90,90,33,889,11,15,73,34,2,7,3,4223,2,323,434,343,43,34,23,543,34,43,234,56,76,6556,543,545,46,67,3,45,43,455,4435,446,334,56,24,46,335],9))
        
    # def twoSum(self, nums, target):
    #     values = {}
    #     for i, num in enumerate(nums):
    #         remaining = target - num
    #         if remaining in values:
    #             return [i, values[remaining]]
    #         else:
    #             values[num] = i
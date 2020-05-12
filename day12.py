<<<<<<< HEAD
#Given a non-empty array of integers, 
# every element appears twice except for one.
#  Find that single one.
class Solution(object):

  def singleNumber(self, nums):

    """
    :type nums: List[int]
    :rtype: int
    """
    no_dup_num = []
    
    for i in nums:

      if i not in no_dup_num:
          no_dup_num.append(i)
      else:
          no_dup_num.remove(i)
    return no_dup_num.pop()
||||||| 2683728
=======
#Given a non-empty array of integers, 
# every element appears twice except for one.
#  Find that single one.
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        no_dup_num = []
        
        for i in nums:
            if i not in no_dup_num:
                no_dup_num.append(i)
            else:
                no_dup_num.remove(i)
        return no_dup_num.pop()
>>>>>>> 0d553f79dc8d7074d4bf7782fe6a80d435f73527

# # Definition for singly-linked list.
# class ListNode:
#   def __init__(self, val=0, next=None):
#     self.val = val
#     self.next = next
class Solution:
  def oddEvenList(self, head: ListNode):
    for_odd = ListNode(0)
    for_even = ListNode(0)
    odd_Head = for_odd
    even_Head = for_even
    isOdd = True
    while head:
      if isodd:
        for_odd.next = head
        for_odd = for_odd.next
      else:
        for_even.next = head
        for_even = for_even.next
      isOdd = not isOdd
      head = head.next
    for_even.next = None
    for_odd.next = even_Head.next
    return odd_Head.next


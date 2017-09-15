# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1, num2 = '', ''
        while (l1 != None):
            num1 += str(l1.val)
            l1 = l1.next
        while (l2 != None):
            num2 += str(l2.val)
            l2 = l2.next
        result = str(int(num1[::-1]) + int(num2[::-1]))
        return [int(char) for char in result[::-1]]

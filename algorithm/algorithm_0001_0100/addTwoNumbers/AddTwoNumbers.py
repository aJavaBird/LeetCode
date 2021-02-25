#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class addTwoNumObj:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        val = (l1.val+l2.val) % 10
        resultNode = ListNode(val)
        l3 = resultNode
        addToNxt = (l1.val+l2.val)//10 # /是精确除法，//是向下取整除法，%是求模
        l1Next = l1.next
        l2Next = l2.next
        while addToNxt>0 or l1Next!=None or l2Next!=None :
            val1 = 0 if l1Next==None else l1Next.val
            val2 = 0 if l2Next == None else l2Next.val
            val3 = (val1 + val2 + addToNxt) % 10
            addToNxt = (val1 + val2 + addToNxt) // 10
            l1Next = l1Next if l1Next==None else l1Next.next
            l2Next = l2Next if l2Next==None else l2Next.next
            l3.next = ListNode(val3)
            l3 = l3.next
        return resultNode

    def getList(self,l: ListNode) -> List[int] :
        list = [l.val];
        next = l.next
        while next!=None :
            list.append(next.val)
            next = next.next
        return list

    def toListNode(self,list: List[int]) -> ListNode :
        listNode = None;
        listNodeIdx1 = None;
        listNodeIdx2 = None;
        for num in list:
            listNodeIdx1 = ListNode(num);
            if listNode==None :
                listNode = listNodeIdx1;
                listNodeIdx2 = listNodeIdx1;
            else :
                listNodeIdx2.next = listNodeIdx1;
                listNodeIdx2 = listNodeIdx1;
        return listNode



#!/usr/bin/python
# -*- coding: UTF-8 -*-

from AddTwoNumbers import *;

solution = addTwoNumObj();

def test():
    l1 = [5];
    l2 = [3];
    res = solution.addTwoNumbers(solution.toListNode(l1), solution.toListNode(l2));
    print('l1={},l2={} --> {}'.format(l1, l2, solution.getList(res)));

    l1 = [2,4,3];
    l2 = [5,6,4];
    res = solution.addTwoNumbers(solution.toListNode(l1), solution.toListNode(l2));
    print('l1={},l2={} --> {}'.format(l1,l2,solution.getList(res)));

    l1 = [0];
    l2 = [0];
    res = solution.addTwoNumbers(solution.toListNode(l1), solution.toListNode(l2));
    print('l1={},l2={} --> {}'.format(l1, l2, solution.getList(res)));

    l1 = [9,9,9,9,9,9,9];
    l2 = [9,9,9,9];
    res = solution.addTwoNumbers(solution.toListNode(l1), solution.toListNode(l2));
    print('l1={},l2={} --> {}'.format(l1, l2, solution.getList(res)));

test();

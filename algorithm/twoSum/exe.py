#!/usr/bin/python
# -*- coding: UTF-8 -*-

from TwoSum import *;

solution = TwoSumObj();

def test():
    nums = [2, 7, 11, 15];
    target = 9;
    res = solution.twoSum(nums, target);
    print('nums={},target={} --> {}'.format(nums,target,res));

    nums = [3, 2, 4];
    target = 6;
    res = solution.twoSum(nums, target);
    print('nums={},target={} --> {}'.format(nums,target,res));

    nums = [3, 3];
    target = 6;
    res = solution.twoSum(nums, target);
    print('nums={},target={} --> {}'.format(nums,target,res));

test();

#!/usr/bin/python
# -*- coding: UTF-8 -*-

from FindMedianSortedArrays import Solution;

solution = Solution();

def test():

    nums1 = [1,3];
    nums2 = [2];
    res = solution.findMedianSortedArrays(nums1,nums2);
    print('num1={}, num2={} --> {}'.format(nums1,nums2,res));

    nums1 = [1,2];
    nums2 = [3,4];
    res = solution.findMedianSortedArrays(nums1, nums2);
    print('num1={}, num2={} --> {}'.format(nums1, nums2, res));

    nums1 = [0, 0];
    nums2 = [0, 0];
    res = solution.findMedianSortedArrays(nums1, nums2);
    print('num1={}, num2={} --> {}'.format(nums1, nums2, res));

    nums1 = [];
    nums2 = [1];
    res = solution.findMedianSortedArrays(nums1, nums2);
    print('num1={}, num2={} --> {}'.format(nums1, nums2, res));

    nums1 = [2];
    nums2 = [];
    res = solution.findMedianSortedArrays(nums1, nums2);
    print('num1={}, num2={} --> {}'.format(nums1, nums2, res));

test();

#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = None;
        nums1Len = len(nums1);
        nums2Len = len(nums2);
        i=0;j=0;
        resList = [];
        if nums1Len==0:
            resList = nums2;
        elif nums2Len==0:
            resList = nums1;
        else:
            while i<nums1Len or j<nums2Len:
                if (i == nums1Len):
                    resList.append(nums2[j]);
                    j += 1;
                elif(j == nums2Len):
                    resList.append(nums1[i]);
                    i += 1;
                elif(nums1[i] > nums2[j]):
                    resList.append(nums2[j]);
                    j += 1;
                else :
                    resList.append(nums1[i]);
                    i += 1;
        resListLen = len(resList);
        # print(resList)
        if (resListLen>0):
            if resListLen%2 ==0:
                result = (resList[int(resListLen/2)] + resList[int(resListLen/2-1)])/2
            else:
                result = resList[int((resListLen-1)/2)]
        return result;

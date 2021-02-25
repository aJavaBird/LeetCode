#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List

class TwoSumObj:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        resultList = [];
        hashMap = {};
        for index,num in enumerate(nums):
            num1 = target - num;  # 第一个数字
            if num in hashMap:
                # 第一个数字的索引号
                # resultList.insert(0, hashMap[num]);
                resultList.append(hashMap[num]);
                # resultList.insert(1, index);
                resultList.append(index);
                return resultList;
            hashMap[num1]=index;
        return resultList;



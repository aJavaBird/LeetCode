#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0;
        if len(s) > 0:
            sList = list(s)
            sMap = {};
            index = 0;
            listLen = len(sList);
            while index < listLen:
                if sList[index] in sMap:
                    if length<len(sMap):
                        length = len(sMap)
                    index = sMap[sList[index]]+1;
                    sMap = {}
                sMap[sList[index]] = index;
                index += 1;  # python 中没有 i++ 运算
            if length < len(sMap):
                length = len(sMap)
        return length;

    # lengthOfLongestSubstringConcise 是更简洁的写法
    def lengthOfLongestSubstringConcise(self, s: str) -> int:
        length = 0;
        if len(s) > 0:
            sList = list(s)
            sMap = {};
            index = 0;
            listLen = len(sList);
            # range(0,3) 相当于 [0,1,2]，后面的数组是不包含的
            for i in range(0,listLen):
                if sList[i] in sMap:
                    # index = sMap[sList[i]] + 1; # 如果这么写，则 abba 会测试失败
                    index = max(index,sMap[sList[i]]+1);
                length = max(length,i-index+1)
                sMap[sList[i]] = i;
        return length;

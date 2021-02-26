#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows<=1:
            return s
        resList = []
        for i in range(0,numRows):
            resList.append([]);
        sList = list(s)
        sLen = len(s)
        isAsc = bool(1)
        resList[0].append(sList[0]);
        index =1
        for i in range(1,sLen):
            resList[index].append(sList[i])
            if index==0 or (index+1)==numRows:
                isAsc = not isAsc
            if isAsc:
                index = index+1;
            else:
                index = index-1;
        resStr = "";
        for i in range(0,numRows):
            resStr = resStr + "".join(resList[i])
        return resStr

    # 精简版
    def convert2(self, s: str, numRows: int) -> str:
        if numRows<=1:
            return s
        resList = ['']*numRows;
        sList = list(s)
        sLen = len(s)
        isAsc = 1
        index = 0
        for i in range(0,sLen):
            resList[index] += sList[i];
            index += isAsc;
            if index==0 or (index+1)==numRows:
                isAsc = -isAsc
        resStr = "".join(resList)
        return resStr

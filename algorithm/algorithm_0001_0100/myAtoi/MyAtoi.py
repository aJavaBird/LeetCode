#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 执行用时：44 ms, 在所有 Python3 提交中击败了66.38%的用户
# 内存消耗：14.7 MB, 在所有 Python3 提交中击败了67.47%的用户
class Solution:
    def myAtoi(self, s: str) -> int:
        numHash = ['0','1','2','3','4','5','6','7','8','9'];
        sList = self.trimToList(s);
        slen = len(sList);
        resStr = "";
        resLen = 0;
        param = 1;
        if slen>0:
            hasSymbol = bool(0);
            if sList[0] in ['+','-']:
                hasSymbol = bool(1);
                if sList[0] == '-':
                    param = -1;
            for i in range(1 if hasSymbol else 0,slen):
                if sList[i] in numHash:
                    if sList[i] == '0' and resLen ==0:
                        continue;
                    resLen += 1;
                    resStr += sList[i];
                else:
                    break;
        resInt = (0 if resLen==0 else int(resStr))*param;
        if resInt< -pow(2,31):
            resInt = -pow(2,31);
        elif resInt> pow(2,31)-1:
            resInt = pow(2, 31)-1;
        return resInt

    def trimToList(self, s: str):
        sList = list(s);
        resList = [];
        hasTrim = bool(0);
        for i in sList:
            if hasTrim or i!=' ':
                hasTrim = bool(1);
                resList.append(i);
        return resList;

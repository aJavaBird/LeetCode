#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 执行用时：28 ms, 在所有 Python3 提交中击败了99.50%的用户
# 内存消耗：14.9 MB, 在所有 Python3 提交中击败了16.49%的用户
class Solution:
    def reverse(self, x: int) -> int:
        res = 0;
        parm =1;
        if x<0:
            x=-x;
            parm = -1;
        while x!=0:
            res = res*10 + x%10;
            x = x//10;
        res = res*parm;
        if res<-pow(2,31) or res>pow(2,31)-1 :
            res =0;
        return res;

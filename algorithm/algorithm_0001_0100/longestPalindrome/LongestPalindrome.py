#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Solution:
    def longestPalindrome(self, s: str) -> str:
        resStr = "";
        resLen = 0;
        if(len(s)>0):
            sList = list(s)
            strLen = len(sList);
            for i in range(0,strLen):
                tsList = [sList[i]];
                j = 1;
                while i - j >= 0 and i + j < strLen and sList[i - j] == sList[i + j]:
                    tsList.insert(0, sList[i - j]);
                    tsList.append(sList[i + j]);
                    j += 1;
                tsList2 = [sList[i]];
                j=1;
                while i + 1 - j >= 0 and i + j < strLen and sList[i - j + 1] == sList[i + j]:
                    if j > 1:
                        tsList2.insert(0, sList[i - j + 1]);
                    tsList2.append(sList[i + j]);
                    j += 1;
                if len(tsList2) > len(tsList):
                    tsList = tsList2;
                if len(tsList)>resLen:
                    resLen = len(tsList);
                    resStr = ''.join(tsList);
        return resStr;

    def test(self,str):
        resStr = self.longestPalindrome(str)
        print('{} --> {}'.format(str,resStr));

solution = Solution();
solution.test('babad');
solution.test('cbbd');
solution.test('a');
solution.test('ac');
solution.test('acahjaisiajd');
solution.test('abbccbbddh');
solution.test('abbccddddh');
solution.test('xabbbcy');
solution.test('xbabbbcy');

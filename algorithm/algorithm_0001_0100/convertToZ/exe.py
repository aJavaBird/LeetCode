#!/usr/bin/python
# -*- coding: UTF-8 -*-

from ConvertToZ import Solution;

solution = Solution();

def test(s,numRows):
    res = solution.convert2(s,numRows);
    print('s={}, numRows={} --> {}'.format(s,numRows,res));

def testMany():
    test("PAYPALISHIRING",3);
    test("PAYPALISHIRING", 4);
    test("A", 1);
    test("adinrojebfkpsqlgchm", 5);

testMany();

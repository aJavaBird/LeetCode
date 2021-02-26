#!/usr/bin/python
# -*- coding: UTF-8 -*-

from MyAtoi import Solution;

solution = Solution();

def test(s):
    res = solution.myAtoi(s);
    print('s=【{}】 --> 【{}】'.format(s,res));

def testMany():
    test("42");
    test("   -42");
    test("4193 with words");
    test("words and 987");
    test("-91283472332");
    test(" 91283472332");
    test("  -9128347 2332");

testMany();

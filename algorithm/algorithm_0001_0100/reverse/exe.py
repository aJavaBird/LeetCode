#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Reverse import Solution;

solution = Solution();

def test(x):
    res = solution.reverse(x);
    print('x={} --> {}'.format(x,res));

def testMany():
    test(123);
    test(-123);
    test(120);
    test(0);
    test(1534236469);

testMany();

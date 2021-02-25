#!/usr/bin/python
# -*- coding: UTF-8 -*-

from LengthOfLongestSubstr import Solution;

solution = Solution();

def test():

    # s = "abcabcbb";
    # res = solution.lengthOfLongestSubstringConcise(s);
    # print('s={} --> {}'.format(s,res));
    #
    # s = "bbbbb";
    # res = solution.lengthOfLongestSubstringConcise(s);
    # print('s={} --> {}'.format(s, res));
    #
    # s = "pwwkew";
    # res = solution.lengthOfLongestSubstringConcise(s);
    # print('s={} --> {}'.format(s, res));
    #
    # s = "";
    # res = solution.lengthOfLongestSubstringConcise(s);
    # print('s={} --> {}'.format(s, res));
    #
    # s = " ";
    # res = solution.lengthOfLongestSubstringConcise(s);
    # print('s={} --> {}'.format(s, res));

    s = "abba";
    res = solution.lengthOfLongestSubstringConcise(s);
    print('s={} --> {}'.format(s, res));

test();

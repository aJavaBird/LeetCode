## 1. 两数之和
### 给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 的那两个整数，并返回它们的数组下标。你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。你可以按任意顺序返回答案。
示例 1：<br/>输入：nums = [2,7,11,15], target = 9<br/>输出：[0,1]<br/>解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：<br/>输入：nums = [3,2,4], target = 6<br/>输出：[1,2]  
示例 3：<br/>输入：nums = [3,3], target = 6<br/>输出：[0,1]
### 链接：https://leetcode-cn.com/problems/two-sum
### 代码：LeetCode/algorithm/algorithm_0001_0100/twoSum/TwoSum.py


## 2. 两数相加
### 给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。请你将两个数相加，并以相同形式返回一个表示和的链表。你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
示例 1：<br/>输入：l1 = [2,4,3], l2 = [5,6,4]<br/>输出：[7,0,8]<br/>解释：342 + 465 = 807.  
示例 2：<br/>输入：l1 = [0], l2 = [0]<br/>输出：[0]  
示例 3：<br/>输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]<br/>输出：[8,9,9,9,0,0,0,1]  
### 链接：https://leetcode-cn.com/problems/add-two-numbers
### 代码：LeetCode/algorithm/algorithm_0001_0100/addTwoNumbers/AddTwoNumbers.py

## 3. 无重复字符的最长子串
### 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
示例1:<br/>输入: s = "abcabcbb"<br/>输出: 3 <br/>解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。  
示例 2:<br/>输入: s = "bbbbb"<br/>输出: 1<br/>解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。  
示例 3:<br/>输入: s = "pwwkew"<br/>输出: 3<br/>解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。  
示例 4:<br/>输入: s = ""<br/>输出: 0
### 链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
### 代码：LeetCode/algorithm/algorithm_0001_0100/lengthOfLongestSubstring/LengthOfLongestSubstr.py

## 4. 寻找两个正序数组的中位数
### 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。<br/>
### 进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？
示例 1：<br/>输入：nums1 = [1,3], nums2 = [2]<br/>输出：2.00000<br/>解释：合并数组 = [1,2,3] ，中位数 2  
示例 2：<br/>输入：nums1 = [1,2], nums2 = [3,4]<br/>输出：2.50000<br/>解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5  
示例 3：<br/>输入：nums1 = [0,0], nums2 = [0,0]<br/>输出：0.00000  
示例 4：<br/>输入：nums1 = [], nums2 = [1]<br/>输出：1.00000  
示例 5：<br/>输入：nums1 = [2], nums2 = []<br/>输出：2.00000  
### 链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
### 代码：LeetCode/algorithm/algorithm_0001_0100/findMedianSortedArrays/FindMedianSortedArrays.py

## 5. 最长回文子串
### 给你一个字符串 s，找到 s 中最长的回文子串。
示例 1：<br/>输入：s = "babad"<br/>输出："bab"<br/>解释："aba" 同样是符合题意的答案。<br/>    
示例 2：<br/>输入：s = "cbbd"<br/>输出："bb"<br/>    
示例 3：<br/>输入：s = "a"<br/>输出："a"<br/>    
示例 4：<br/>输入：s = "ac"<br/>输出："a" 
### 链接：https://leetcode-cn.com/problems/longest-palindromic-substring
### 代码：LeetCode/algorithm/algorithm_0001_0100/longestPalindrome/LongestPalindrome.py

## 6. Z 字形变换
### 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：<br/>
P&nbsp;&nbsp;&nbsp;&nbsp;A&nbsp;&nbsp;&nbsp;H&nbsp;&nbsp;&nbsp;N<br/>A&nbsp;P&nbsp;L&nbsp;S&nbsp;I&nbsp;I&nbsp;G<br/>Y&nbsp;&nbsp;&nbsp;&nbsp;I&nbsp;&nbsp;&nbsp;&nbsp;R<br/>
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。<br/>请你实现这个将字符串进行指定行数变换的函数：<br/>string convert(string s, int numRows);<br/>
示例 1：<br/>输入：s = "PAYPALISHIRING", numRows = 3<br/>输出："PAHNAPLSIIGYIR"<br/>
示例 2：<br/>输入：s = "PAYPALISHIRING", numRows = 4<br/>输出："PINALSIGYAHRPI"<br/>解释：<br/>P&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;N<br/>A&nbsp;&nbsp;&nbsp;L&nbsp;S&nbsp;&nbsp;&nbsp;I&nbsp;G<br/>Y&nbsp;A&nbsp;&nbsp;&nbsp;H&nbsp;R<br/>P&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;I<br/>
示例 3：<br/>输入：s = "A", numRows = 1<br/>输出："A"<br/>
提示：<br/>1 <= s.length <= 1000<br/>s 由英文字母（小写和大写）、',' 和 '.' 组成<br/>1 <= numRows <= 1000<br/>
### 链接：https://leetcode-cn.com/problems/zigzag-conversion
### 代码：LeetCode/algorithm/algorithm_0001_0100/convertToZ/ConvertToZ.py

## 7. 整数反转
### 给你一个 32 位的有符号整数 x ，返回 x 中每位上的数字反转后的结果。
### 如果反转后整数超过 32 位的有符号整数的范围 [−2^31,  2^31 − 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。
示例 1：<br/>输入：x = 123<br/>输出：321<br/>
示例 2：<br/>输入：x = -123<br/>输出：-321<br/>
示例 3：<br/>输入：x = 120<br/>输出：21<br/>
示例 4：<br/>输入：x = 0<br/>输出：0<br/>
### 链接：https://leetcode-cn.com/problems/reverse-integer
### 代码：LeetCode/algorithm/algorithm_0001_0100/reverse/Reverse.py

## 8. 字符串转换整数 (atoi)
### 请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。
函数 myAtoi(string s) 的算法如下：<br/>
读入字符串并丢弃无用的前导空格<br/>
检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。<br/>
读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。<br/>
将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。<br/>
如果整数数超过 32 位有符号整数范围 [−2^31, 2^31 − 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −2^31 的整数应该被固定为 −2^31 ，大于 2^31 − 1 的整数应该被固定为 2^31 − 1 。<br/>
返回整数作为最终结果。<br/>  
注意：<br/>
本题中的空白字符只包括空格字符 ' ' 。<br/>
除前导空格或数字后的其余字符串外，请勿忽略 任何其他字符。<br/>  
示例 1：<br/>输入：s = "42"<br/>输出：42<br/>
示例 2：<br/>输入：s = "   -42"<br/>输出：-42<br/>
示例 3：<br/>输入：s = "4193 with words"<br/>输出：4193<br/>
示例 4：<br/>输入：s = "words and 987"<br/>输出：0<br/>
示例 5：<br/>输入：s = "-91283472332"<br/>输出：-2147483648<br/>
### 链接：https://leetcode-cn.com/problems/string-to-integer-atoi
### 代码：LeetCode/algorithm/algorithm_0001_0100/myAtoi/MyAtoi.py


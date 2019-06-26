"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        data_list = []
        length_list = []
        index = 0
        for data in s:
            if data in data_list:
                repeat_index = data_list.index(data)
                max_length_list = data_list[0:index]
                if index - repeat_index == 1:
                    data_list = []
                else:
                    data_list = data_list[(repeat_index + 1):]
                length_list.append(len(max_length_list))
            data_list.append(data)
            index += 1
        length_list.append(len(data_list))
        return 0 if len(length_list) == 0 else max(length_list)

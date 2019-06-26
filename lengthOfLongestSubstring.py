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

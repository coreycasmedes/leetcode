from collections import OrderedDict

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        ordered_dict  = OrderedDict()
        for a in arr:
            if a in ordered_dict:
                ordered_dict[a] += 1
            else:
                ordered_dict[a] = 1
        distinct_strings = {k: v for k, v in ordered_dict.items() if v == 1}
        distinct_strings = OrderedDict(filter(lambda x: x[1] == 1, ordered_dict.items()))
        print(ordered_dict)
        
        
        print(distinct_strings)
        result = ""
        if k > len(distinct_strings):
            return ""
        for i in range(k):
            result = distinct_strings.popitem(last=False)[0]

        return result

        
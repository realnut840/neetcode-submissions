class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxx = []
        length = len(arr)
        for i in range (length):
            arr_max = []
            if i == len(arr) - 1:
                    maxx.append(-1)
            else:
                for j in range (i + 1, length):
                    nums = arr[j]
                    arr_max.append(nums)
                max_num = max((arr_max))
                maxx.append(max_num)
        return maxx
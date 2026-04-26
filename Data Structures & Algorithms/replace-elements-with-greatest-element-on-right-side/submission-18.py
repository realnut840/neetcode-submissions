class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxx = []
        length = len(arr)
        for i in range(length - 1):
            arr_max = []
            for j in range(i + 1, length):
                nums = arr[j]
                arr_max.append(nums)
            max_num = max(arr_max)
            maxx.append(max_num)
        maxx.append(-1)
        return maxx
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #start from the right 
        #keep track of rightmax 
        #when we get to i, turn it to rightmax
        #compare arr[i] with rightmax, update if arr[i] > rightmax

        rightmax = arr[-1]

        for i in range(len(arr) - 2, -1, -1):
            temp = arr[i]
            arr[i] = rightmax
            rightmax = max(rightmax, temp)
        
        arr[-1] = -1

        return arr
            

        

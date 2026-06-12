class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n):
            sub_array = []
            if i+1 < n:
                sub_array = arr[i+1:]
                sub_array.sort(reverse=True)
                arr[i] = sub_array[0]
        arr[n-1] = -1
        return arr
                    
        
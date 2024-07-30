class Solution:
    def merge(self, arr, l, m, r):
        list1 = arr[l : m + 1]
        list2 = arr[m + 1 : r + 1]

        l1 = len(list1)
        l2 = len(list2)

        left, right = 0, 0
        k = l

        while left < l1 and right < l2:
            if list1[left] <= list2[right]:
                arr[k] = list1[left]
                left += 1
            else:
                arr[k] = list2[right]
                right += 1
            k += 1

        while left < l1:
            arr[k] = list1[left]
            left += 1
            k += 1

        while right < l2:
            arr[k] = list2[right]
            right += 1
            k += 1

        return arr

    def mergeSort(self, arr, l, r):
        if l < r:

            mid = (l + r) // 2

            self.mergeSort(arr, l, mid)
            self.mergeSort(arr, mid + 1, r)

            self.merge(arr, l, mid, r)


# {
# Driver Code Starts
# Initial Template for Python 3
import sys

input = sys.stdin.readline
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        Solution().mergeSort(arr, 0, n - 1)
        for i in range(n):
            print(arr[i], end=" ")
        print()
# } Driver Code Ends

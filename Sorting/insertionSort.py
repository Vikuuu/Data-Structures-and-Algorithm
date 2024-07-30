class Solution:
    def insert(self, alist, i, n):
        j = i - 1
        while j >= 0 and alist[j + 1] < alist[j]:
            temp = alist[j + 1]
            alist[j + 1] = alist[j]
            alist[j] = temp
            j -= 1

    def insertionSort(self, alist, n):
        for i in range(n):
            self.insert(alist, i, n)

        return alist


# Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        Solution().insertionSort(arr, n)

        for i in range(n):
            print(arr[i], end=" ")

        print()

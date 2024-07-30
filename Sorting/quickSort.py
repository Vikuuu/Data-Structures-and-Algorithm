class Solution:
    # Function to sort a list using quick sort algorithm.
    def quickSort(self, arr, low, high):
        if high - low + 1 <= 1:
            return arr

        left = self.partition(arr, low, high)

        self.quickSort(arr, low, left - 1)
        self.quickSort(arr, left + 1, high)

        return arr

    def partition(self, arr, low, high):
        pivot = arr[high]
        left = low

        for i in range(low, high):
            if arr[i] < pivot:
                temp = arr[left]
                arr[left] = arr[i]
                arr[i] = temp
                left += 1

        arr[high] = arr[left]
        arr[left] = pivot

        return left


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        Solution().quickSort(arr, 0, n - 1)
        for i in range(n):
            print(arr[i], end=" ")
        print()

# } Driver Code Ends

from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result_array = []
        sum = 0
        for i in operations:
            if i == "C":
                result_array.pop()
            elif i == "D":
                temp = result_array[-1]
                temp = int(temp) * 2
                result_array.append(int(temp))
            elif i == "+":
                temp1 = result_array[-1]
                temp2 = result_array[-2]
                temp = int(temp1) + int(temp2)
                result_array.append(int(temp))
            else:
                result_array.append(i)

        for i in result_array:
            sum = sum + int(i)

        return sum

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l1, r1 = 0, len(matrix)-1
        while l1 <= r1:
            m1 = (l1+r1)//2
            if matrix[m1][0] <= target <= matrix[m1][-1]:
                l2, r2 = 0, len(matrix[m1])
                while l2 <= r2:
                    m2 = (l2+r2)//2
                    if matrix[m1][m2] == target:
                        return True
                    elif matrix[m1][m2] < target:
                        l2 = m2 + 1
                    else:
                        r2 = m2 - 1
                return False
            elif target < matrix[m1][0]:
                r1 = m1 - 1
            else:
                l1 = m1 + 1
        return False
        
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix)-1

        while top <= bot:
            f_mid = top + (bot - top)//2 
            if target < matrix[f_mid][0]:
                bot = f_mid - 1
            elif target > matrix[f_mid][-1]:
                top = f_mid + 1
            else:
                l, r = 0, len(matrix[f_mid])-1
                while l <= r:
                    s_mid = l + (r - l)//2
                    if matrix[f_mid][s_mid] < target:
                        l = s_mid + 1 
                    elif matrix[f_mid][s_mid] > target:
                        r = s_mid - 1
                    else:
                        return True
                return False
        return False


    

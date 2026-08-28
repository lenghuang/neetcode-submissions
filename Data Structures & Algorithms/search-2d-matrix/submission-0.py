class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # once you have the row, find the column within it

        def myPrint(*args):
            if False:
                print(*args)

        def getMid(lo, hi):
            mid = lo + ((hi - lo) // 2)
            # myPrint("mid of lo", lo, "hi", hi, "is", mid)
            return mid

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        lo_row, lo_col = 0, 0
        hi_row, hi_col = rows - 1, cols - 1
        mid_col = getMid(lo_col, hi_col)

        # first try to find what row its own
        while (lo_row <= hi_row):
            mid_row = getMid(lo_row, hi_row)
            x = matrix[mid_row][mid_col]
            myPrint("is it in row", mid_row, "?")
            if (x == target):
                return True
            elif (x < target):
                lo_row = mid_row + 1
            else:
                hi_row = mid_row - 1

        # the row we ended up finding
        myPrint("Found it somewhere in row", mid_row)

        # check edge cases
        if target < matrix[mid_row][0]:
            mid_row -= 1
        elif target > matrix[mid_row][-1]:
            mid_row += 1

        myPrint("Adjusting midrow to      ", mid_row)

        # return early
        if mid_row < 0 or mid_row >= rows:
            return False

        # now look within the row for it
        while (lo_col <= hi_col):
            mid_col = getMid(lo_col, hi_col)
            y = matrix[mid_row][mid_col]
            if y == target:
                return True
            elif y < target:
                lo_col = mid_col + 1
            else:
                hi_col = mid_col - 1

        return False
class Solution:
    
    def checkDuplicateAndUpdateFreq(self, freq_list, index, item):
        if index < 0 or index >= len(freq_list):
            return True

        freq = freq_list[index]
        
        if item in freq:
            return True
        
        freq[item] = 1
        return False
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        board_len = len(board)
        board_width = len(board[1])
        box_len = 3
        box_width = 3
        box_count = (board_len * board_width) // (box_len * box_width)

        row_freq = [{} for _ in range(len(board))]
        col_freq = [{} for _ in range(len(board[1]))]
        box_freq = [{} for _ in range(box_count)]

        for i in range(len(board)):
            for j in range(len(board[i])):
                num = board[i][j]
                if num == ".":
                    continue
                
                # print("(", i, ",", j, ") =", num)

                if self.checkDuplicateAndUpdateFreq(row_freq, i, num):
                    # print("duplicate at row", i, "for val", nu,)
                    return False

                if self.checkDuplicateAndUpdateFreq(col_freq, j, num):
                    # print("duplicate at col", j, "for val", num)
                    return False

                row_rounded = (i // box_len) * box_len
                col_rounded = (j + box_width) // box_width
                box_index = row_rounded + col_rounded - 1

                # print("box data", "row", row_rounded, "col", col_rounded, "box_index", box_index)

                if self.checkDuplicateAndUpdateFreq(box_freq, box_index, num):
                    # print("duplicate at box", box_index, "for val", num)
                    return False
                
        return True

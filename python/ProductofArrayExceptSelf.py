def isValidSudoku(self, board)
    # check if int and 0<num <=9
    if not board:
        return False

    num_rows = len(board)
    num_cols = len(board[0])

    def check_unique_rows():

        for i in range(num_rows):
            row_list = get_slices(i, -1)
            if not is_unique_nums(row_list):
                return False
        return True

    def get_slices(row, col):
        if row >= 0:
            return board[row][:]
        if col >= 0:
            return board[:][col]

    def is_unique_nums(nums_list):
        unique_nums_set = set()
        for num in nums_list:
            if num in unique_nums_set:
                return False
            else:
                unique_nums_set.add(num)

    def check_unique_cols():

        for i in range(num_cols):
            col_list = get_slices(-1, i)
            if not is_unique_nums(col_list):
                return False
        return True

    def check_unique_sub_box():
            


    is_row_unique = check_unique_rows()
    is_col_unique = check_unique_cols()
    is_sub_box_unique = check_unique_sub_box()

    if is_row_unique and is_col_unique and is_sub_box_unique:
        return True

    else:
        return False
"""
U:
    i: list of lists (sudoku)
    o: boolean

    constraints: 
        board.length == 9
    board[i].length == 9
    board[i][j] is a digit 1-9 or '.'.

M: set to see if values repeat, 3 dict for rows, columns, boxes where key will tell which row, which column, which box, each cell belong to 
P: 
    1. create 3 dict, rows, columns, boxes

    for each list of list of lists, 
        for each cell of each list //iterating each rows
        2. keys from 0 to 8 for rows, columns 
            keys from (0,0) to (0,2) and (2,2) for boxes  //use ****tuple*** tuples are hashable
            values = set 
        if cell is in 1 of the set of 3 dict, return False 
        else: add the value to the corresponding set of 3 dict 
    3. return False 
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = {}
        columns = {}
        boxes = {}

        for i in range(len(board)): #row
            each_list = board[i] 

            for j in range(len(each_list)): #col
                curr_str = each_list[j] #board[i][j]

                if curr_str != '.': 
                    elem = int(curr_str)

                    if i not in rows: 
                        rows[i] = set()
                    if j not in columns: 
                        columns[j] = set()
                    
                    # for boxes dict's key
                    r = i // 3 
                    c = j // 3 

                    if (r,c) not in boxes: 
                        boxes[(r,c)] = set()

                    if elem in rows[i] or elem in columns[j] or elem in boxes[(r,c)]:
                        return False 
                    
                    rows[i].add(elem)
                    columns[j].add(elem)
                    boxes[(r,c)].add(elem)

        return True



    
        
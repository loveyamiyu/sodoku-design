import random



class Generate:
    def __init__(self, level):
        self.level = level

    def sudoku_generator(self):
        sudoku = []

        filename='sudokus/' + self.level + '.txt'
        file = open(filename, 'r') #read sudoku file with specified difficulty level
        lines = file.readlines()

        r_num = random.randint(0, 400) 
        r_line = lines[r_num] # randomly pick up a line from sudoku file

        if len(r_line) == 0:
            r_line = lines[r_num + 1] # skip to the next line when the current line is empty
        
        for i in range(9):
            grid_row = []
            for j in range(9):
                char = r_line[i*9+j]
                if char == '.':
                    # append a 0 (representing a blank in the grid) if
                    #   the character is a . in the text file
                    grid_row.append(0)
                else:
                    grid_row.append(char)
            sudoku.append(grid_row)
        
        return sudoku
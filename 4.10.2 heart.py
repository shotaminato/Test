def heart():
    grid = [
        ['.','.','.','.','.','.'],
        ['.','0','0','.','.','.'],
        ['0','0','0','0','.','.'],
        ['0','0','0','0','0','.'],
        ['.','0','0','0','0','0'],
        ['0','0','0','0','0','.'],
        ['0','0','0','0','.','.'],
        ['.','0','0','.','.','.'],
        ['.','.','.','.','.','.'],
        ]
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            print(str(grid[j][i]), end = '') #jとiの順番に気をつけよう
        print()

heart()


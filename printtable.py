def printTable(table):
    col_widths = getLongestWordLength(table)
    for col in range(len(table[0])): #coluna da tableData table[0]
        for row in range(len(table)): #elementos da linha de table return 3
            print(table[row][col].rjust(col_widths[row]), end=' ') #row = 1, col = 1 ('apples, Alice, dogs') exemplo
        print()


def getLongestWordLength(table):
    return[max([len(item) for item in line]) for line in table]


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


printTable(tableData)
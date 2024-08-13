tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def printTable(x):
    # finding the longest string in each list
    long = [0]*len(x) 
    for e in x[0]:
            if(long[0] < len(e)):
                long[0] = len(e)
    for e in x[1]:
        if(long[1] < len(e)):
                long[1] = len(e)
    for e in x[2]:
        if(long[2] < len(e)):
                long[2] = len(e)
    j = 0
    while(j <4):
        print(tableData[0][j].rjust(long[0]+1)+tableData[1][j].rjust(long[1]+1)+tableData[2][j].rjust(long[2]+1))
        j= j+1


printTable(tableData)
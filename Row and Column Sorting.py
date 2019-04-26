def read_matrix(filename):
    with open(filename, 'r') as input_file:
        matrixlist=[[int(column) for column in row.split()] for row in input_file]
        rowsum=[]
        columnsum=[]
        for eachrow in matrixlist:
            rowsum.append(sum(eachrow))
        columsum=sum(row[n] for row in eachrow for n in range(0,len(eachrow+1)))
        
    return columnsum
        

print(read_matrix("testmatrix0.txt"))

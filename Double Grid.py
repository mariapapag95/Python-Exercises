with open("grid.txt","r")as input_file, open("doublegrid.txt","w") as output_file:
    doublegrid=[]
    for line in input_file:
        line=line.strip()
        digits=line.split(" ")
        doublegrid=doublegrid.append(digits)
        for j in digits:
            j=int(j)
            doubledigits=(j*2)
            doubledigits=str(doubledigits)
            #doubledigits=doubledigits.join(" ")
            #doublegrid.append(doubledigits
    print(doublegrid)
    print(doublegrid, file=output_file, end="")
    
    #CREATE ONE LONG LIST WITH ALL THE GRID, DOUBLE, THEN REBUILD THE GRID
    
    
    
    #for i in input_file:
        #if i.isdigit:
            #i=(i)*2
            #doublegrid=i
        #else:
            #pass
        ##doublegrid=grid REPLACE WITH DIGIT
        #print(doublegrid, file=output_file, end="")

    #numlist=input_file.split(" ")
    #for num in numlist:
        #doublenum=num*2
    #doublenum.join(" ")
    #doublegrid=doublenum, #\n after 10 characters
    #print(doublegrid, file=output_file)

"""
    doublegrid=[]
    for line in input_file:
        line=line.strip()
        digits=line.split(" ")
        for j in digits:
            j=int(j)
            j=j*2
        digits=str(digits)
        doublegrid=doublegrid.append(digits.join(" "))
        print(doublegrid, file=output_file, end="")
        """
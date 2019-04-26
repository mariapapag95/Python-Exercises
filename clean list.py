var2=["3","three",["maria",5],3,3.0,True,None]
def printlist(lst):
    answers=[]
    for i in lst:
        if isinstance(i, list)==True:
            for j in i:
                answers.append(j)
        else:
            answers.append(i)
    return answers
            
print(printlist(var2))

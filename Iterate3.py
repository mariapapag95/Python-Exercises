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

#ask how to get this to return each item on list without printing the as list
#how to do this ^ withtout having "print" command inside function
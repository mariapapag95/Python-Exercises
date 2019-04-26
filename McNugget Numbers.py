def isnugget(n):
    return n==0 or any(n >= i and isnugget(n - i) for i in (6,9,20))
nonnugs=[]
for number in range(700):
    if isnugget(number)==False:
        nonnugs.append(number)
print(nonnugs)

#rewrite line 5
#if not isnugget:
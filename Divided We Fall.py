def divisors(num):
    divisor=[]
    for i in range(1,num+1):
        if num%i==0:
            divisor.append(i)
    divsum=sum(divisor)
    divnum=len(divisor)
    result=[divisor,divsum,divnum]
    return result

print(divisors(60))
num=int(input("Enter a number: "))
def arabic2roman(num):
    'This function takes one number'
    'and returns the roman numeral of'
    'that number'
    'expected input= digit'
    'expected output= string'

    romans = {"M":1000,"CM":900,
    "D":500,"CD":400,
    "C":100,"XC":90,
    "L":50,"XL":40,
    "X":10,"IX":9,
    "V":5,"IV":4,
    "I":1}
    result=""
    for i in romans:
        R=num//romans[i]
        if R>0:
            result+=i*R
            num=num-(R*romans[i])
    return result
            
print(arabic2roman(num))
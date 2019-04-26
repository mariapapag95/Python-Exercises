def currency_converter(amount):
    amount=amount*100
    denominations={
        "hundred-dollar bill" : 10000,
        "fifty-dollar bill" : 5000,
        "twenty-dollar bill" : 2000,
        "ten-dollar bill" : 1000,
        "five-dollar bill" : 500,
        "one-dollar bill" : 100,
        "quarter" : 25,
        "dime" : 10,
        "nickel" : 5,
        "penny" : 1
    }
    for i in denominations:
        numbills=amount//denominations[i]
        if numbills>0:
            print(int(numbills),i)
            amount=amount-(numbills*denominations[i])

currency_converter(107.69)
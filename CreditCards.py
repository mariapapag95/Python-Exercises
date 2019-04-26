cardNumber="75"
cardNumber=int(cardNumber)
try:
    if cardNumber:
        if cardNumber[0]==4:
            print("This card is a valid Visa.")
except ValueError:
    print("This card is invalid.")

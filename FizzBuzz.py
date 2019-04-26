def fizzbuzz(num):
    for i in range(1,num):
        if i%5==0 and i%3==0:
            print ("FizzBuzz")
        elif i%5==0:
            print ("Buzz")
        elif i%3==0:
            print ("Fizz")
        else:
            print (i)

fizzbuzz(20)
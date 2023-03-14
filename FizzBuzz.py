def FizzBuzz():
    s=""
    for i in range(1,101):
        Fizz = ""
        Buzz = ""
        x= ""
        if i%3==0:
            Fizz = "Fizz"
        if i%5==0:
            Buzz = "Buzz"
        if i%5!=0 and i%3!=0:
            x = i
        s+= str(x)+Fizz+Buzz+"\n"
    return s
print(FizzBuzz())
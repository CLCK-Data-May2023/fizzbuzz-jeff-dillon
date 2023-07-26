# add your code here
for number in range(1,101):
    by_five = number % 5 == 0
    by_three = number % 3 == 0

    if(by_five and by_three):
        print("FizzBuzz")
    elif(by_three):
        print("Fizz")
    elif(by_five):
        print("Buzz")
    else:
        print(str(number))

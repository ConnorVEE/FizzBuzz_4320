## Program start
## imports

## Loop through each number 0 to 100
for num in range(0, 100):

    #check if number is divisible by 3 and 5
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")

    #Check if num is divisible by 3
    elif num % 3 == 0:
        print("Fizz")

    #Check if num is divisible by 5
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

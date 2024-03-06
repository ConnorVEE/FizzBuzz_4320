## Program start
## imports

## Loop through each number 0 to 100
for num in range(0, 100):

    #Check if num is divisible by 3
    #Check if num is divisible by 5
    if num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

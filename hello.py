print("Hello, git!")
def fizzbuzz():

    for num in range(1, 101):
        if num % 15 == 0:
            print("FizzBuzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else :
            print(num)
        
        
fizzbuzz()

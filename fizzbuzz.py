#Given a number, count to it and replace all numbers divisible by 3 with "fizz" and those divisible by 5 with "buzz".
#Those satisfying both conditions are replaced with "fizzbuzz"

def fizzbuzz(val: int):
    for i in range(1, val+1): #beginning at 1 so we ignore zero, val+1 to include actual number given
            if i%3 == 0 and i%5 == 0:
                print("Fizzbuzz!")
            elif i%3 == 0:
                print("Fizz!")
            elif i%5 == 0:
                print("Buzz!")
            else:
                print(i)

fizzbuzz(100)

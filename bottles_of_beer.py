#Given an input of some number, write a program to write a "bottles of beer on the wall" song

def bottles_of_beer(val: int):
    for i in range(val, 0, -1): #specify that the range should be iterated through backwards until reaching 0
        song = "{number} bottles of beer on the wall, {number} bottles of beer! Take one down, pass it around, {next} bottles of beer on the wall!"
        print( song.format(number = i, next = i-1) ) #fancy formatted string

    print("No more bottles of beer on the wall, no more bottles of beer! We've taken them down and passed them around, now we're drunk and passed out!") #when there are 0 bottles, or input is a negative

bottles_of_beer(99)
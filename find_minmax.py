#Given an input list of real numbers, write a function to return the greatest value.
#*Without using builtin sorting functions such as sort()!
#This is an o(n) solution.

def findmax(lst: list):
    currentMax = lst[0] #set the current maximum to a number within bounds of the list for the purpose of comparison against all other values
    for i in lst:
        if i > currentMax:
            currentMax = i #"If the list value we're considering is greater than the largest value encountered so far, the considered value is the new largest value encountered so far."
    return currentMax

#a simple inversion of the above code to instead find the smallest value of a list input
def findmin(lst):
    currentMin = lst[0] #set the current maximum to a number within bounds of the list for the purpose of comparison against all other values
    for i in lst:
        if i < currentMin:
            currentMin = i
    return currentMin

list1 = [81, 57, 55, 52, 82, 7, 9, 9, 9, 9, 9, 2, 139, 32, 99.99, 33.33, 12.39382, 3.14597, 87, 34, 9, 1, 12, 93, -5, -3, -12,] #greatest value is 139, smallest value is -12
list2 = [-1, -4, -992.28, -93, -60, -30, -32, -1100, -41, -37,] #a peculiar list containing all negative numbers. greatest: -1, smallest: -1100.

greatest_value_list1 = findmax(list1)
greatest_value_list2 = findmax(list2)
print("Of list 1, greatest value is: " + str(greatest_value_list1))
print("Of list 2, greatest value is: " + str(greatest_value_list2) + "\n")

smallest_value_list1 = findmin(list1)
smallest_value_list2 = findmin(list2)
print("Of list 1, smallest value is: " + str(smallest_value_list1))
print("Of list 2, smallest value is: " + str(smallest_value_list2) + "\n")



#Write your solution here.
#Write a Function that:
#checks if x is present and return it's location(index)
# and if is not return -1

def solve_me(arr, n, x):
    
    for i in range (0, n):
        if (arr[i] == x):
            return i
    return -1
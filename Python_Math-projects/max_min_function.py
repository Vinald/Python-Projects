# To  find the maximum number
def max_number(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3


num1 = int(input('Enter the first numbers: \n'))
num2 = int(input('Enter the sseconrd number: \n'))
num3 = int(input('Enter the third number: \n'))
print('the largest number is', max_number(num1, num2, num3))

# using in_built function
print('the largest number is', max(num1, num2, num3))


# using a user function
def min_number(n1, n2, n3):
    if n1 < n2 and n1 < n3:
        return n1
    elif n2 < n1 and n2 < n3:
        return n2
    else:
        return n3


num1 = int(input('Enter the first numbers: \n'))
num2 = int(input('Enter the sseconrd number: \n'))
num3 = int(input('Enter the third number: \n'))
print('the smallest number is', min_number(num1, num2, num3))

# using in_built function
print('the smallest number is', min(num1, num2, num3))
def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)


num = int(input("Enter a number: "))

if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", recur_factorial(num))


# using in built methods
def factorail_computing(num):
    return(math.factorial(num))


number = int(input('Enter a number: '))
factorial_number = factorail_computing(number)
print('the factorial of', number, 'is', factorial_number)

# using a for while loop
number = int(input('Enter a number: '))
fac = 1
i = 1
while i < number:
    fac *= i
    i += 1

print("factorial of", number, 'is', fac)


# for the for loop
def fac_iterative_method(n):
    fac = 1
    for i in range(n):
        fac = (fac * (i + 1))
        print('fac of', i + 1, '=', fac)


number = int(input('enter the number'))
fact = fac_iterative_method(number)
print('the factorial of', number, 'is', fact)

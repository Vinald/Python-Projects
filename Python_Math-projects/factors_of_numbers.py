def factor_of_number(num):
    print('the factors of', num, 'are')
    for i in range(1, num+1):
        if num % i == 0:
            print(i)


number = int(input('Enter a number: '))
num1 = factor_of_number(number)
print(num1)

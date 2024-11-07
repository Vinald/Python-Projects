def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 3, 6]
    dup_number = find_duplicate_number(numbers)
    print(f'List of duplicate number(s) is: {dup_number}')

def find_duplicate_number(arg):
    dup = []
    for i in range(len(arg)):
        for j in range(i+1, len(arg)):
            if arg[i] == arg[j]:
                dup.append(arg[i])
    return dup
            

if __name__ == '__main__':
    main()
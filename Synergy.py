repeated = set()

while True:
    print('Введите последовательность чисел через пробел')
    numbers = set(map(int, input().split()))
    
    for number in numbers:
        if number in repeated:
            print(f'Число {number} - YES')
        else: print(f'Число {number} - NO')

    repeated.update(set(numbers))
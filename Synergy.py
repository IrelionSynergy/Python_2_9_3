repeated = set()
command = ''

while True:
    print('Введите последовательность чисел через пробел')
    print('Для остановки программы введите: stop')
    line = input()
    if line.lower() == 'stop':
        break
    numbers = set(map(int, line.split()))
    
    for number in numbers:
        if number in repeated:
            print(f'Число {number} - YES')
        else: print(f'Число {number} - NO')

    repeated.update(set(numbers))
n = int(input('Digite um número: ')) #primo = n / n and n / 1
total = 0
for x in range(1, n + 1):
    if n % x == 0:
        print('\033[33m', end=' ')
        total = total + 1                 # ou tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(x), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(n, total))
if total == 2:
    print('Por isso ele É primo')
else:
    print('Por isso ele NÃO é primo')

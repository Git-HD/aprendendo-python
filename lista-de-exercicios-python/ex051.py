primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
pa = primeiro + (10 - 1) * razão
for x in range(primeiro, pa + razão, razão):
    print('{} '.format(x), end=' > ')
print('ACABOU')
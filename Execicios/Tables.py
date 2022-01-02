print('**** Print Tables ****')
table = int(input('Choose a number to make a table: '))
print('Tables {}'.format(table))

for i in range(1, 11):
    result = table * i
    print('{} X {} = {}'.format(table, i, result))

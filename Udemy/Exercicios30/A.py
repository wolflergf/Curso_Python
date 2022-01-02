numero = input('Digite um numero inteiro: ')
if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print('O numero digitado e um numero par.')
    else:
        print('O numero digitado e um numero impar.')
else:
    print('O que foi digitado nao e um numero inteiro')
    print('Por favor digite um numero inteiro.')
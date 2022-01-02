hora = input('Digite um horario entre 0 - 23: ')
if hora.isdigit():
    hora = int(hora)
    if hora < 0 or hora > 23:
        print('O valor digitado deve estar entre 0 e 23!')
    else:
        if 0 <= hora < 6:
            print('Boa madrugada!')
        elif 6 <= hora < 12:
            print('Bom dia!')
        elif 12 <= hora < 18:
            print('Boa tarde!')
        elif 18 <= hora < 23:
            print('Boa noite!')
else:
    print('Voce digitou uma letra, favor digitar um numero entre 0 e 23!')

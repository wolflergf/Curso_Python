usuario = input('Digite o nome do usuario: ')
senha = input('Digite sua senha: ')
usuario_bd = 'Luiz'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Voce esta logado no sistema')
else:
    print('Usuario ou senha invalida!')

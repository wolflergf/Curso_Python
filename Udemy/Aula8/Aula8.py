nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura ** 2)
ano_atual = 2022
ano_nascimento = ano_atual - idade

print('{} tem {} anos, {} de altura e pesa {}Kg'.format(nome, idade, altura, peso,))
print('O IMC de {} e {:.2f}.'.format(nome, imc))
print('{} nasceu em {}.'.format(nome, ano_nascimento))

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura ** 2)

print(nome, 'tem,', idade, 'anos de idade e seu IMC e:', imc)
print(f'{nome} tem {idade} anos de idade e seu IMC e: {imc:.2f}')
print('{} tem {} anos de idade e seu imc e {:.2f}'.format(nome, idade, imc))

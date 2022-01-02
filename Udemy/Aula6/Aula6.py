'''
A variavel inicia-se com letra, pode conter numeros, serapar por _, Latras minusculas
'''


nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura * altura)

print(nome, 'tem,', idade, 'anos de idade e seu IMC e: ', imc)



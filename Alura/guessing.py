import random
def game_guessing():
    print('********************************')
    print('* Welcome to the Guessing game *')
    print('********************************')
    numero_escolhido = round(random.randrange(1, 101))
    total_de_tentativas = 0
    score_inicial = 1000

    print('Choose a level.')
    nivel = int(input('(1) Easy, (2) Normal, (3) Hard: '))
    if nivel == 1:
        total_de_tentativas = 10
    else:
        if nivel == 2:
            total_de_tentativas = 6
        elif nivel == 3:
            total_de_tentativas = 3

    for rodada in range(1, total_de_tentativas + 1):
        print('Attempt: {} de {}'.format(rodada, total_de_tentativas))
        palpite = int(input('Enter a number between 1 and 100: '))
        if palpite < 1 or palpite > 100:
            print('You must enter a number between 1 and 100!')
            continue

        acerto = palpite == numero_escolhido
        maior = palpite > numero_escolhido
        menor = palpite < numero_escolhido

        if acerto:
            print('You win an you score is {}!'.format(score_inicial))
            break
        else:
            if maior:
                print('You missed! The number you entered is greater than the secret number!')
            elif menor:
                print('You missed! The number you entered is less than the secret number ')
                score_lost = abs(numero_escolhido - palpite)
                score_inicial = score_inicial - score_lost


    print('The number was: {} and you score is {}'.format(numero_escolhido, score_inicial))
    print('Game Over!')
if __name__ == '__main__':
    game_guessing()

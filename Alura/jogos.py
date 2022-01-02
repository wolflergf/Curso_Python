import forca
import guessing
def jogos():
    print("*********************************")
    print("*******       Games       *******")
    print("*********************************")

    print("(1) Forca (2) Guessing")
    game = int(input("Choose a game: "))
    if game == 1:
        print("Playing Forca")
        forca.game_forca()
    elif game == 2:
        print("Playing Guessing")
        guessing.game_guessing()
if __name__ == '__main__':
    jogos()

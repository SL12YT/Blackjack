from random import randint as r

class cards:
    normal = [[1,6,7,8,9,10,11,12,13, 0], [1,6,7,8,9,10,11,12,13, 0],
              [1,6,7,8,9,10,11,12,13, 0], [1,6,7,8,9,10,11,12,13, 0]]
    extra = [[1,2,3,4,5,6,7,8,9,10,11,12,13, 0],
             [1,2,3,4,5,6,7,8,9,10,11,12,13, 0],
             [1,2,3,4,5,6,7,8,9,10,11,12,13, 0],
             [1,2,3,4,5,6,7,8,9,10,11,12,13, 0]]
    mini  = [[1,8,9,10,11,12,13, 0], [1,8,9,10,11,12,13, 0],
             [1,8,9,10,11,12,13, 0], [1,8,9,10,11,12,13, 0]]

    
    def gendeck(n : int):
        """ generates deck \n
            1 - normal, 2 - extra, 3 - mini """
        
        if n not in (1,2,3):
            n = 1
        deck = []
        if n == 1:
            deck = cards.normal
        elif n == 2:
            deck = cards.extra
        else:
            deck = cards.mini
       
        return deck
        
class game:
    deck = {} # current game deck
    player = [] # player's deck
    
    def getCard():

        m = r(0,3); n = r(0, len(game.deck[1]) - 1)
        while game.deck[m][n] == 0:
            m = r(0, 3)
            n = r(0, len(game.deck[1]) - 1)  
        card = game.deck[m][n]
        game.deck[m][n] = 0
        return m, card
    
    def stat():
        """ checks if player win of lose """
        s = sum(game.player)
        if s > 21:
            return 2 # FAIL
        elif s == 21:
            return 1 # WIN
        else:
            return 0
    
    def main():
        card = game.getCard()
        game.player.append(card[1])
        s = game.stat()
        mast = "♡♧◇♤"
        if card[1] in [1, 11, 12, 13]:
            card = [card[0], [0, 'T',2,3,4,5,6,7,8,9,10,'B','D','K'][card[1]]]
        print("card :", mast[card[0]], card[1])
        if s == 2:
            print("YOU FAILED | Score :", sum(game.player))
        elif s == 1:
            print("YOU WIN!")
        else:
            print("Want to get new card?")
            inp = input("[y/n] >> ")
            if inp == "n":
                print("YOU FAILED | Score :", sum(game.player))
            elif inp == "y":
                game.main()


while True:
    d = int(input("chose deck [1,2,3] >> "))

    game.deck = cards.gendeck(d)
    game.main()

    ask = input("want to play again? [y/n] >> ")
    if ask == 'n':
        print('Thanks for playing :)')
        exit()

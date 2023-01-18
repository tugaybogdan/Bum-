import random
import easygui as gui

playerdeck = []
class Card:
    deck = ["Т", "2", "3", "4", "5", "6", "7",
         "8", "9", "10", "В", "Д", "K"] 
    SUITS = [u'\u2660', u'\u2663', u'\u2665', u'\u2666'] # ♠ ♣ ♥ ♦ 
    SUITS_STR = ''.join(SUITS)
    SUITS_NAMES = 'schd'
    global cardplayed

    

    def card_images(self):
            rep = []
            if self.cards:
                for card in self.cards:
                    card_name = str(card)
                
                    table = card_name.maketrans (Card.SUITS_STR, Card.SUITS_NAMES)
                    card_name = card_name.translate(table)
                    filename = f'{card_name[-1]}{(Card.RANKS.index(card_name[:-1]) + 1):0>2}.png'
                rep.append('assets/' + filename)
            return rep

    def specialcardrule(cards, index, cardplayed):
        card = cards[index - 1]

    def createcard():
        deckcard = Card.deck[random.randrange(len(Card.deck)) -1]
        colorcard = Card.SUITS[random.randrange(len(Card.SUITS)) -1]

        card = (deckcard, colorcard)
        return card

    def checkcards(cards):
        index = 0
        for card in cards:
        

            index += 1


class Play:
    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

    def playerturn():
        answer = gui.msgbox('What card do you want choose?')
        return answer

    def playable(cards, index, cardplayed):
        card = cards[index - 1]

        if card[0] == cardplayed[0]:
            return True
        elif card[1] == cardplayed[1]:
            return True
        else:
            return False
    

def startgame():
    for i in range(7):
        card = Play.createcard()
        playerdeck.append(card)

    Play.checkcards(playerdeck)

    gui.msgbox(*playerdeck, sep='\n')
    
    index = Play.playerturn()
    cardplayed = playerdeck[index - 1]
    playerdeck.pop(index - 1)

    gui.msgbox(f'The last card being played: {cardplayed}')
    gui.msgbox(*playerdeck, sep='\n')

    while True:
        index = Play.playerturn()

        if playerdeck[index - 1][0]:
            cardvalue = Card.specialcardrule(playerdeck, index, cardplayed)
            cardplayed =cardvalue
            playerdeck.pop(index - 1)
        else:   
            result = Play.playable(playerdeck, index, cardplayed)

            if result:
                cardplayed = playerdeck[index - 1]
                playerdeck.pop(index - 1)
            else:
                gui.msgbox('You lost')
                break

        gui.msgbox(f'The last card being played: {cardplayed}')
        gui.msgbox(*playerdeck,)



startgame()
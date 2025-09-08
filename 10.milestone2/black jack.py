from random import shuffle as sh
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card():
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    def __str__(self):
        return f"{self.rank} of {self.suit}"
new_card=Card("Hearts","Two")
print(new_card)

class Deck:
    
    def __init__(self):
        self.all_cards = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                create_card=Card(suit,rank)
                self.all_cards.append(create_card)
    
    def __str__(self):
        cardlist=""
        for i in self.all_cards:
            cardlist+=str(i)+"\n"
        return cardlist

    def shuffle(self):
        sh(self.all_cards)
        
    def deal(self):
        single_card=self.all_cards.pop()
        return single_card
    
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        #card passeed in from Deck.deal()-->single_card(suit,rank)
        self.cards.append(card)
        self.value+=values[card.rank]
        
        self.aces+=1
        
    def adjust_for_ace(self):
        while self.value>21 and self.aces>0:
            self.value-=10
            self.aces-=1
            
class Chips:
    def __init__(self,total=100):
        self.total=total 
        self.bet=0
        
    def win_bet(self):
        self.total+=self.bet
        
    def lose_bet(self):
        self.total-=self.bet

from random import shuffle as sh
suits=('Hearts','Diamonds','Spades','Clubs')
ranks=('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
#-------------------------------------------------------------------------------------
Values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}
class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=Values[rank]
    def __str__(self):
        return self.rank+" of "+self.suit
#-------------------------------------------------------------------------------------
class Deck:
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                create_card=Card(suit,rank)
                self.all_cards.append(create_card)
    def shuffle(self):
        sh(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()
#-------------------------------------------------------------------------------------
class Player:
    def __init__(self,name):
        self.name=name
        self.all_cards=[]
    def remove_one(self):
        return self.all_cards.pop(0)
    def add_one(self,newcards):
        if type(newcards)==type([]):
            self.all_cards.extend(newcards)
        else:
            self.all_cards.append(newcards)
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'
new_deck=Deck()
new_deck.shuffle()
my_card=new_deck.deal_one()
print(my_card)
new_player=Player('Beni')
new_player.add_one(my_card)
Cardlist=new_player.all_cards
print(new_player.all_cards[0])
new_player.add_one([my_card,my_card,my_card])
print(new_player)
new_player.remove_one()
print(new_player)
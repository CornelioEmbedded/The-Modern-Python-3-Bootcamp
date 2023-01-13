# Here I did some tests as I understood Colt, he did something different,
# and hardcoded, but it help me to learn.

import unittest
import sys
sys.path.append(r"C:\Users\DELL\Desktop\Cornelio\Github_repos\The-Modern-Python-3-Bootcamp\25_Deck_Of_Cards_Exercise")
from deck_cards import Deck, Card
import random

class DeckOfCardsTests(unittest.TestCase):
    """Test for Deck and Card classes"""
    def setUp(self):
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        
    def test_representation_card(self):
        for suit in self.suits:
            for value in self.values:
                card_object = Card(suit, value)
                self.assertEqual(str(card_object), f'{value} of {suit}')
    
    def test_representation_deck(self):
        deck_object = Deck()
        self.assertEqual(str(deck_object), f'Deck of {deck_object.count()}')
    
    def test_count_deck(self):
        deck_object = Deck()
        deck_count = deck_object.count()
        self.assertEqual(deck_count, len(deck_object.cards))
    
    # def test_deal_card(self):
    #     deck_object = Deck()
    #     deck_deal_card = deck_object.deal_card()
    #     self.assertEqual(deck_deal_card, deck_object._deal(-1)[0])



if __name__ == '__main__':
    unittest.main()






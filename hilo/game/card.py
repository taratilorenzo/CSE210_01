import random

class Card:
    """A deck of 13 cards numbered 1-13.
    The responsibility of Cards is to keep track of the values of cards and points for it.
    Attributes:
        value (int): The number of the card.
        points (int): The number of points the player has.
        hilo (string): A string of 'h' or 'l'
    """
    def __init__(self):
        """Constructs a new instance of Cards.
        Args:
            self (Cards): An instance of Cards.
        """
        self.current_card_value = 0
        self.next_card_value = random.randint(1, 13)
        self.points = 0
        self.hilo = ""
        self.player_guess = ""
        self.confirm_points = True

    def draw_card(self):
        """Draws a random card to display.
        Args:
            self (Card): An instance of Card.
        """
        self.current_card_value = self.next_card_value
        self.next_card_value = random.randint(1, 13)
    
    def confirm_guess(self):
        """Uses the player's response to generate a boolean for point calculation.
        Args:
            self (Cards): An instance of Cards.
        """
        
        if self.next_card_value <= self.current_card_value:
            self.hilo = "l"
        elif self.next_card_value >= self.current_card_value:
            self.hilo = "h"

        self.confirm_points = (self.hilo == self.player_guess)

        self.points = 100 if self.confirm_points == True else (-75) if self.confirm_points == False else 0
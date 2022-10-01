from game.card import Card
import random


class Director:
    """A person who directs the game.
    The responsibility of the Director is to control the sequence of play.
    Attributes:
        cards (List[Card]): A list of Card instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        current_card_value (int): The value of the current card.
        next_card_value (int): The value of the next card.
        hilo_value (string): The given value of a player-given input.
    """

    def __init__(self):
        """Constructs a new Director.
        Args:
            self (Director): an instance of Director.
        """
        self.cards = Card()
        self.is_playing = True
        self.score = 300
        self.current_card_value = 0
        self.next_card_value = 0
        self.hilo_value = ""

        card = self.cards
        self.current_card_value = card.current_card_value
        self.next_card_value = card.next_card_value
    
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self.current_card_value = random.randint(1, 13)
        self.next_card_value = random.randint(1, 13)
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            self.continue_game()
        
        print(f"Final score was {self.score}!\n")
        
    
    def get_inputs(self):
        """Prompt the user for a response to Higher or lower and ask the user if they want to draw another card.
        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        print(f"The card is: {self.current_card_value}")
        self.hilo_value = input("Higher or lower? [h/l] ")

    def do_updates(self):
        """Updates the player's score and current_card_value.
        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        card = self.cards
        card.draw_card()
        self.current_card_value = card.current_card_value
        self.next_card_value = card.next_card_value
        card.player_guess = self.hilo_value
        card.confirm_guess()
        self.score += card.points
            
    def do_outputs(self):
        """Displays the cards and the score. Also asks the player if they want to draw again.
        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        print(f"Next card was: {self.next_card_value}")
        print(f"Your score is: {self.score}")
        self.is_playing == (self.score > 0)
        
    def continue_game(self):
        """Ask the user if they would like to continue playing.
        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        draw_card = input("Play again? [y/n] ")
        self.is_playing = (draw_card == "y")
from pickle import FALSE
import random

class Puzzle:
    """The secret word chosen from the list. 
    
    The responsibility of the Puzzle class is to keep track of its letters. 
    
    Attributes:
        _word (List[string]): The word of the puzzle.
        _letters (List[string]): The letters from the word of the puzzle.
        _guesses (int): The  umber of guesses we have before the jumper falls
    """

    def __init__(self):
        """Constructs a new Puzzle.

        Args:
            self (Puzzle): An instance of Puzzle.
        """
        self._word = random.choice(["orange","chocolate","pathway","trouble","plane"]) #chose randomly from the list
        self._letters = list(self._word) #return ['p','l','a','n','e'] if plane was the puzzle word to find
        self._guesses = 0

    def is_found(self, letter):
        """Whether or not the letter belong to the word puzzle.

        Args:
            self (Puzzle: An instance of Puzzle.
            
        Returns:
            boolean: True if the letter was found; false if otherwise.
        """
        return ( letter in self._letters)
        
    def watch_turns(self):
        """Keeping track of how many guesses we have left.

        Args:
            self (Puzzle): An instance of Puzzle.
        """
        if (self._is_found() == False): self._guesses = self._guesses + 1
        
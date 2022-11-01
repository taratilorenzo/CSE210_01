class Jumper:
    """The person looking for the word puzzle. 
    
    The responsibility of a Jumper is to find the word puzzle before we fall (4 turns)
    
    Attributes:
        letter (string): The guess of the jumper between [a-z]
    """

    def __init__(self):
        """Constructs a new Jumper.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self._letter = ''
        self._number_of_guesses = 0
       
    def get_letter(self):
        """Gets the current letter.
        
        Returns:
            letter: The current letter,
        """
        return self._letter

    def watch_turns(self):
        self._number_of_guesses = self._number_of_guesses + 1
        return self._number_of_guesses
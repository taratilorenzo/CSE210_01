import random

# 1) Add the class declaration. Use the following class comment.
class Jumper:
    """The person looking for the word puzzle. 
    
    The responsibility of a Jumper is to find the word puzzle before we fall (4 turns)
    
    Attributes:
        letter (string): The guess of the jumper between [a-z]
    """

    # 2) Create the class constructor. Use the following method comment.
    def __init__(self):
        """Constructs a new Jumper.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self._letter = ''
       
    # 3) Create the get_location(self) method. Use the following method comment.
    def get_location(self):
        """Gets the current location.
        
        Returns:
            number: The current location,
        """
        return self._letter
        
    # 4) Create the move_location(self, location) method. Use the following method comment.
    def move_location(self, location): 
        """Moves to the given location.

        Args:
            self (Seeker): An instance of Seeker.
            location (int): The given location.
        """
        self._location = location
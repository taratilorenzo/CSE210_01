import random

class Word:
    """The secret word chosen from the list. 
    
    The responsibility of the Word class is to keep track of its letters. 
    
    Attributes:
        _word (List[string]): The word of the puzzle.
        _letters (List[string]): The letters from the word of the puzzle.
    """

    def __init__(self):
        """Constructs a new Word.

        Args:
            self (Word): An instance of Word.
        """
        self._word = random.choice(["orange","chocolate","pathway","trouble","plane"]) #chose randomly from the list
        self._letters = list(self._word) #return ['p','l','a','n','e'] if plane was the puzzle word to find
        self._guess_letter = ""
        self._guess_index = 0
        self._empty_list = []
        self._guessed_letters = []
        for i in range(len(self._letters)): self._empty_list.append('_')
        

    def guessed_word(self):
        for i in range(len(self._empty_list)): print(self._empty_list[i], end=" ")

    def is_found(self):
        """Whether or not the letter belong to the word.

        Args:
            self (Word): An instance of Word.
            
        Returns:
            boolean: True if the letter was found; false if otherwise.
        """
        return ( self._guess_letter in self._letters)

    def index(self):
        self._guess_index =  self._letters.index(self._guess_letter)

    def get_hint(self):
        hint = ""
        if self._empty_list == self._letters:
            hint = "Well done! You saved the Jumper!"
            print("The word was " + self._word)
        elif self._guess_letter in self._guessed_letters:
            hint = "You have use this guessed before Already!"
        elif self.is_found():
            self.index()
            self._empty_list[self._guess_index] = self._guess_letter
            hint = "Nice guess Mate"
        elif self.is_found() == False:
            hint = "Sorry this guess is wrong!"
            self._guessed_letters.append(self._guess_letter)

        return hint
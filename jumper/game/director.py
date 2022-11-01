from game.terminal_service import TerminalService
from game.word import Word
from game.jumper import Jumper


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        jumper (Jumper): The game's jumper.
        is_playing (boolean): Whether or not to keep playing.
        puzzle (Puzzle): The game's secret word.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._is_playing = True
        self._word = Word()
        self._jumper = Jumper()
        self._terminal_service = TerminalService()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._word.guessed_word()
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Moves the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        self._word._guess_letter =  self._terminal_service.read_letter("\nGuess a letter  [a-z]: ")
        
    def _do_updates(self):
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """
        if self._word.is_found() == False:
            if self._jumper.watch_turns() == 5:
                self._is_playing = False

        
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        
        hint = self._word.get_hint()
        self._terminal_service.write_text(hint)
        if self._word._empty_list == self._word._letters:
            hint = self._word.get_hint()
            self._terminal_service.write_text(hint)
            self._is_playing = False
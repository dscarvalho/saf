__author__ = 'danilo@jaist.ac.jp'

from typing import List, Dict

from .annotable import Annotable
from .term import Term
from .token import Token


class Sentence(Annotable):
    """Description of a sentence.

    Attributes:
    tokens (list of Token): Sequence of tokens composing the sentence, in reading order.
    terms (list of Term): [optional] Sequence of terms (morphemes -> phrases) composing the sentence, in reading order.
    annotations (dict): [optional] Sentence level annotations, identified by the dictionary key.
        Examples: sentence vector, inclusion status (in extractive summarization).
    """

    def __init__(self):
        super(Sentence, self).__init__()
        self.tokens: List[Token] = []
        self.terms: List[Term] = []
        self._surface: str = None

    @property
    def surface(self) -> str:
        if (not self._surface):
            raise NotImplementedError

        return self._surface

    @surface.setter
    def surface(self, value):
        self._surface = value

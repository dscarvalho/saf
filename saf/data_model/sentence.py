__author__ = 'danilo@jaist.ac.jp'

from annotable import Annotable


class Sentence(Annotable):
    """Description of a sentence.

    Attributes:
    tokens (list of Token): Sequence of tokens composing the sentence, in reading order.
    terms (list of Term): [optional] Sequence of terms (morphemes -> phrases) composing the sentence, in reading order.
    annotations (dict): [optional] Sentence level annotations, identified by the dictionary key.
        Examples: sentence vector, inclusion status (in extractive summarization).
    """

    def __init__(self):
        self.tokens = []
        self.terms = []
        self.annotations = dict()
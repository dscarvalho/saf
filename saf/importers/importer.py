__author__ = 'Danilo S. Carvalho <danilo@jaist.ac.jp>, Vu Duc Tran <vu.tran@jaist.ac.jp>'

from abc import ABC
from abc import abstractmethod


class Importer(ABC):
    def __init__(self, sentence_tokenizer, word_tokenizer):
        """Formatter constructor

        Constructs a formatter object that tokenizes a plain text document into sentences using
        sentence_tokenizer and words in a sentence using word_tokenizer.

        :param sentence_tokenizer: tokenizer to separate sentences in a document.
            Should be a callable object tokenizer(txt: str) -> List[str]
            Example: NLTK sent_tokenize
        :param word_tokenizer: tokenizer to separate words in a sentence.
            Should be a callable object tokenizer(txt: str) -> List[str]
        :return: new Formatter instance.
        """

        self.sent_tokenizer = sentence_tokenizer
        self.word_tokenizer = word_tokenizer


    @abstractmethod
    def import_document(self, document):
        """Imports a plain text document

        Args:
            document (str): plain text to be imported as a document.

        :return: Document object
        """
        raise NotImplementedError()



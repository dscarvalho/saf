__author__ = 'danilo.carvalho@manchester.ac.uk'

from typing import List, Dict, Iterable, Union
from collections import Counter

from .annotable import Annotable


class Vocabulary:
    """Represents the vocabulary that constitutes a collection of Annotables

        Each token in the collection is associated to a symbol (its surface form).
        Each symbol is mapped to an index, which can be used for vectorizing the annotables.

        :param data (list of Annotable): list of annotables for which the vocabulary will be extracted.
        :param maxlen (int): maximum size of the vocabulary. If exceeded, the most frequent symbols are selected.
        """
    def __init__(self, data: List[Annotable] = None, maxlen: int = None):
        if (data):
            tokens = list()
            for annotable in data:
                if (hasattr(annotable, "sentences")):
                    for sent in annotable.sentences:
                        tokens.extend(sent.tokens)
                elif (hasattr(annotable, "tokens")):
                    tokens.extend(annotable.tokens)

            self.freqs: Counter[str] = Counter([tok.surface for tok in tokens])
            self.vocab: Dict[str, int] = {symbol: i for i, symbol in enumerate(sorted(self.freqs.keys()))}

            if (maxlen):
                excl = set(self.freqs.keys()) - set([symbol for symbol, freq in self.freqs.most_common(maxlen)])
                self.del_symbols(list(excl))

    def __len__(self):
        return len(self.vocab)

    @property
    def symbols(self) -> Iterable[str]:
        return self.vocab.keys()

    def add_symbols(self, symbols: List[str]):
        for symbol in symbols:
            if (symbol not in self.vocab):
                self.vocab[symbol] = len(self.vocab)

    def del_symbols(self, symbols: List[str]):
        for symbol in symbols:
            del self.vocab[symbol]
            del self.freqs[symbol]

        self.vocab = {s: i for i, s in enumerate(self.vocab.keys())}

    def to_indices(self, data: List[Annotable], default: int = -1, padding: int = 0,
                   pad_symbol: str = None, start_symbol: str = None, end_symbol: str = None) -> Union[List[List[int]], List[List[List[int]]]]:
        indices = list()

        if (padding < 0):
            for annotable in data:
                if (hasattr(annotable, "sentences")):
                    maxlen = max([len(sent.tokens) for sent in annotable.sentences])
                    padding = maxlen if (padding < maxlen) else padding
                elif (hasattr(annotable, "tokens")):
                    padding = len(annotable.tokens) if (padding < len(annotable.tokens)) else padding

            if (start_symbol):
                padding += 1
            if (end_symbol):
                padding += 1

        for annotable in data:
            if (hasattr(annotable, "sentences")):
                indices.append(list())
                for sent in annotable.sentences:
                    indices[-1].append([self.vocab.get(tok.surface, default) for tok in sent.tokens])
                    if (start_symbol is not None):
                        indices[-1][-1].insert(0, self.vocab.get(start_symbol, default))
                    if (end_symbol is not None):
                        indices[-1][-1].append(self.vocab.get(end_symbol, default))
                    if (padding and len(indices[-1][-1]) < padding):
                        indices[-1][-1].extend([self.vocab.get(pad_symbol, default)] * (padding - len(indices[-1][-1])))
            elif (hasattr(annotable, "tokens")):
                indices.append([self.vocab.get(tok.surface, default) for tok in annotable.tokens])
                if (start_symbol is not None):
                    indices[-1].insert(0, self.vocab.get(start_symbol, default))
                if (end_symbol is not None):
                    indices[-1].append(self.vocab.get(end_symbol, default))
                if (padding and len(indices[-1]) < padding):
                    indices[-1].extend([self.vocab.get(pad_symbol, default)] * (padding - len(indices[-1])))

        return indices


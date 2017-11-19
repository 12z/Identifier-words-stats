from collections import Counter
from typing import Iterable
from .verb_extractor import PartOfSpeech, WordLocation, DataItem


def calculate_frequencies(data_items: Iterable[DataItem],
                          part_of_speech: PartOfSpeech, location: WordLocation)-> Counter:
    counter = Counter()
    for item in data_items:
        if item.part_of_speech == part_of_speech and item.location == location:
            counter.update([item.word])

    return counter

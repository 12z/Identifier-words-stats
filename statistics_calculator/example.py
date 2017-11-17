from typing import Iterable

import collections
import os
import nltk
from enum import Enum, auto

from .verb_extractor import get_verbs_in_path


from collections import namedtuple

DataItem = namedtuple('DataItem', ['word', 'part_of_speech', 'location'])


class PartOfSpeech(Enum):
    VERB = auto()
    NOUN = auto()


class WordLocation(Enum):
    FUNCTION = auto()
    VARIABLE = auto()


class ResultsRepresentationType(Enum):
    CONSOLE = auto()
    JSON_FILE = auto()
    CSV_FILE = auto()


NUMBER_OF_TOP_VERBS = 10


def run_example():

    # using nltk package here as it is needed to be installed anyway
    nltk_dir = os.path.dirname(nltk.__file__)
    counter = collections.Counter()
    counter.update(get_verbs_in_path(nltk_dir))

    for verb, occurrence in counter.most_common(NUMBER_OF_TOP_VERBS):
        print(verb, occurrence)


def download_repo(repository_url: str) -> str:
    return ''


def get_data(repo_path: str) -> Iterable[DataItem]:
    return ''


def calculate_frequencies(data: Iterable[DataItem], part_of_speech: PartOfSpeech, word_location: WordLocation) -> dict:
    return {'': ''}


def show_results(results: dict, report_type: ResultsRepresentationType):
    return ''


def get_statistics(repository_url, part_of_speech, word_location, report_type):
    repo_path = download_repo(repository_url)
    data = get_data(repo_path)
    results = calculate_frequencies(data, part_of_speech, word_location)
    show_results(results, report_type)

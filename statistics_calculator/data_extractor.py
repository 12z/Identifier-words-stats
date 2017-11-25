import os
import ast
from typing import Iterable, Union, Tuple
from collections import namedtuple
from enum import Enum, auto

from nltk import pos_tag


class PartOfSpeech(Enum):
    VERB = auto()
    NOUN = auto()


class WordLocation(Enum):
    FUNCTION = auto()
    VARIABLE = auto()


DataItem = namedtuple('DataItem', ['word', 'part_of_speech', 'location'])


def get_data(path):
    sources = _read_sources_from_path(path)
    yield from _get_marked_words_from_sources(sources)


def _read_sources_from_path(path: str) -> Iterable[str]:

    for root, dirnames, filenames in os.walk(path):

        for filename in filenames:

            if not filename.endswith('.py'):
                continue

            with open(os.path.join(root, filename), 'r', encoding='utf-8') as file:
                yield file.read()


def _get_marked_words_from_sources(sources):
    for source_code in sources:
        yield from _get_marked_words_from_source_code(source_code)


def _get_marked_words_from_source_code(source_code):

    try:
        for node in ast.walk(ast.parse(source_code)):
            yield from _find_functions_words(node)
            yield from _find_variables_words(node)
    except SyntaxError:
        pass  # ignore files with invalid syntax


def _find_functions_words(node):

    if isinstance(node, ast.FunctionDef):
        for word, pos in _mark_words_in_identifier(node.name):
            yield DataItem(word=word, part_of_speech=pos, location=WordLocation.FUNCTION)


def _find_variables_words(node):

    if hasattr(node, 'target'):
        yield from _get_variables_words_from_target_subtree(node)

    if hasattr(node, 'targets'):
        for target in node.targets:
            yield from _get_variables_words_from_target_subtree(target)


def _get_variables_words_from_target_subtree(target):
    for target_node in ast.walk(target):

        if not isinstance(target_node, ast.Name):
            continue

        for word, pos in _mark_words_in_identifier(target_node.id):
            yield DataItem(word=word, part_of_speech=pos, location=WordLocation.VARIABLE)


def _mark_words_in_identifier(identifier):

    if not (identifier.startswith('__') or identifier.endswith('__')):
        yield from _get_marked_words_from_identifier(identifier.lower())


def _get_marked_words_from_identifier(identifier) -> Iterable[Tuple[str, PartOfSpeech]]:

    for word in identifier.split('_'):

        if not word:
            continue

        part_of_speech = _get_part_of_speech(word)
        if part_of_speech:
            yield word, part_of_speech


def _get_part_of_speech(word: str) -> Union[PartOfSpeech, None]:
    """
    Only supports verbs and nouns for now
    """
    pos_info = pos_tag([word])[0][1]

    if pos_info.startswith('VB'):
        return PartOfSpeech.VERB

    elif pos_info.startswith('NN'):
        return PartOfSpeech.NOUN

    else:
        return None  # Explicit is better than implicit. (c) PEP 20

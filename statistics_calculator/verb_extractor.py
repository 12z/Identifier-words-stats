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


def _read_file_content(filename: str) -> Union[str, None]:

    if not filename.endswith('.py'):
        return

    with open(filename, 'r', encoding='utf-8') as file:
        try:
            return file.read()
        except SyntaxError:
            pass  # ignoring files with invalid python syntax


def _read_sources_from_path(path: str) -> Iterable[str]:

    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            sources = _read_file_content(os.path.join(root, filename))
            if sources:
                yield sources


def _get_function_names_from_source_code(source_code: str) -> Iterable[str]:

    for node in ast.walk(ast.parse(source_code)):
        if not isinstance(node, ast.FunctionDef):
            continue

        starts_with_underscores = node.name.startswith('__')
        ends_with_underscores = node.name.endswith('__')
        if not (starts_with_underscores or ends_with_underscores):
            yield node.name.lower()


def _get_function_names_from_sources(sources: Iterable[str]) -> Iterable[str]:

    for source_code in sources:
        for function_name in _get_function_names_from_source_code(source_code):
            yield function_name


def _get_verbs_from_sources(sources: Iterable[str]):
    function_names = _get_function_names_from_sources(sources)
    return _get_verbs_from_function_names(function_names)


def _is_verb(word: str) -> bool:
    if not word:
        return False
    pos_info = pos_tag([word])
    return pos_info[0][1] == 'VB'


def _get_verbs_from_function_names(function_names: Iterable[str]) -> Iterable[str]:

    for function_name in function_names:
        for word in function_name.split('_'):
            if _is_verb(word):
                yield word


def get_verbs_in_path(path: str) -> Iterable[str]:
    sources = _read_sources_from_path(path)
    return _get_verbs_from_sources(sources)


def get_data(path):
    sources = _read_sources_from_path(path)
    yield from get_marked_words_from_sources(sources)


def get_marked_words_from_sources(sources):
    for source_code in sources:
        yield from get_marked_words_from_source_code(source_code)


def get_marked_words_from_source_code(source_code):

    for node in ast.walk(ast.parse(source_code)):
        yield from find_functions_words(node)
        yield from find_variables_words(node)


def find_functions_words(node):

    if isinstance(node, ast.FunctionDef):
        for word, pos in mark_words_in_identifier(node.name):
            yield DataItem(word=word, part_of_speech=pos, location=WordLocation.FUNCTION)


def find_variables_words(node):

    if hasattr(node, 'target'):
        yield from get_variables_words_from_target_subtree(node)

    if hasattr(node, 'targets'):
        for target in node.targets:
            yield from get_variables_words_from_target_subtree(target)


def get_variables_words_from_target_subtree(target):
    for target_node in walk_target_subtree(target):
        for word, pos in mark_words_in_identifier(target_node.id):
            yield DataItem(word=word, part_of_speech=pos, location=WordLocation.VARIABLE)


def walk_target_subtree(root):
    for target_node in ast.walk(root):
        if isinstance(target_node, ast.Name):
            yield target_node


def mark_words_in_identifier(identifier):
    starts_with_underscores = identifier.startswith('__')
    ends_with_underscores = identifier.endswith('__')
    if not (starts_with_underscores or ends_with_underscores):
        yield from get_marked_words_from_identifier(identifier.lower())


def get_marked_words_from_identifier(identifier) -> Iterable[Tuple[str, PartOfSpeech]]:
    for word in identifier.split('_'):
        if word:
            part_of_speech = get_part_of_speech(word)
            if part_of_speech:
                yield word, part_of_speech


def get_part_of_speech(word: str) -> Union[PartOfSpeech, None]:
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


if __name__ == '__main__':
    for item in get_data('/tmp/repos/Verb-extractor'):
        print('{:11} {} {}'.format(item.word, item.part_of_speech.name, item.location.name))

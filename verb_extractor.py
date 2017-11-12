import os
import ast
from typing import Iterable, Union
from nltk import pos_tag


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
        if isinstance(node, ast.FunctionDef) and \
                (not node.name.startswith('__') and not node.name.endswith('__')):
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

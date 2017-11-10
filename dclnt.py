import ast
import os
import collections

from nltk import pos_tag


def flat(_list):
    """ [(1,2), (3,4)] -> [1, 2, 3, 4]"""
    return sum([list(item) for item in _list], [])


def is_verb(word):
    if not word:
        return False
    pos_info = pos_tag([word])
    return pos_info[0][1] == 'VB'


def get_filenames(path):
    filenames = []

    for dir_path, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.py'):
                filenames.append(os.path.join(dir_path, file))

    print('total %s files' % len(filenames))

    return filenames


def get_trees_from_filenames(filenames):
    trees = []

    for filename in filenames:

        with open(filename, 'r', encoding='utf-8') as attempt_handler:
            main_file_content = attempt_handler.read()
        try:
            tree = ast.parse(main_file_content)
            trees.append(tree)
        except SyntaxError as e:
            print(e)
            continue

    return trees


def get_trees(path):

    filenames = get_filenames(path)
    trees = get_trees_from_filenames(filenames)
    print('trees generated')

    return trees


def get_verbs_from_function_name(function_name):
    return [word for word in function_name.split('_') if is_verb(word)]


def get_top_verbs_in_path(path, top_size=10):

    trees = [t for t in get_trees(path) if t]

    fncs = [f for f in
            flat([[node.name.lower() for node in ast.walk(t) if isinstance(node, ast.FunctionDef)] for t in trees]) if
            not (f.startswith('__') and f.endswith('__'))]

    print('functions extracted')
    verbs = flat([get_verbs_from_function_name(function_name) for function_name in fncs])

    return collections.Counter(verbs).most_common(top_size)

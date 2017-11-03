import builtins
import django
import pyramid as pyramid

from dclnt import get_top_verbs_in_path
import nltk
import os
import collections

import flask
import requests


# wds = []
projects = [
    flask,
    requests,
    pyramid,
    django,
]

# projects = [
#     'django',
#     'flask',
#     'pyramid',
#     'reddit',
#     'requests',
#     'sqlalchemy',
# ]

path = os.path.dirname(os.path.dirname(nltk.__file__))
wds = get_top_verbs_in_path(path)

# for project in projects:
#     pack = builtins
#     path = os.path.dirname(project.__file__)
#     # path = os.path.join('.', project)
#     wds += get_top_verbs_in_path(path)

print(wds)

top_size = 200
print('total %s words, %s unique' % (len(wds), len(set(wds))))
for word, occurence in collections.Counter(wds).most_common(top_size):
    print(word, occurence)

import django
import pyramid as pyramid

from dclnt import get_top_verbs_in_path
import nltk
import os
import collections

import flask
import requests


projects = [
    flask,
    requests,
    pyramid,
    django,
]


# using nltk package here as it is needed to be installed anyway
nltk_dir = os.path.dirname(nltk.__file__)
path = os.path.dirname(nltk_dir)
wds = get_top_verbs_in_path(nltk_dir, 200)

# for project in projects:
#     pack = builtins
#     path = os.path.dirname(project.__file__)
#     # path = os.path.join('.', project)
#     wds += get_top_verbs_in_path(path)


top_size = 200
print('total %s words, %s unique' % (len(wds), len(set(wds))))
for word, occurence in wds:
    print(word, occurence)

from dclnt import get_top_verbs_in_path
import os
import collections

import flask, requests

wds = []
projects = [
    flask,
    requests
]
# projects = [
#     'django',
#     'flask',
#     'pyramid',
#     'reddit',
#     'requests',
#     'sqlalchemy',
# ]

for project in projects:
    path = os.path.dirname(project.__file__)
    # path = os.path.join('.', project)
    wds += get_top_verbs_in_path(path)

top_size = 200
print('total %s words, %s unique' % (len(wds), len(set(wds))))
for word, occurence in collections.Counter(wds).most_common(top_size):
    print(word, occurence)

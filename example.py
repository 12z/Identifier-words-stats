import collections
import os
import nltk
from verb_extractor import get_verbs_in_path


NUMBER_OF_TOP_VERBS = 10


# using nltk package here as it is needed to be installed anyway
nltk_dir = os.path.dirname(nltk.__file__)
counter = collections.Counter()
counter.update(get_verbs_in_path(nltk_dir))

for verb, occurrence in counter.most_common(NUMBER_OF_TOP_VERBS):
    print(verb, occurrence)

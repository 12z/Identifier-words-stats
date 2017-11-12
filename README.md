# Verb extractor

This tool can be used to extract verbs from function names of ".py" files that recide in a given directory.
Extracted verbs can serve as data for statistic reports of different sorts.

For this to work tagger for language package needs to be downloaded first like so:
```
>>> import nltk
>>> nltk.download('averaged_perceptron_tagger')
```
After that you are all set to go.

Usage example can be found in example.py

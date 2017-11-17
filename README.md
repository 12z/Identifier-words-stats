# Verb extractor

This tool can be used to extract verbs from function names of ".py" files that recite in a given directory.
Extracted verbs can serve as data for statistic reports of different sorts.

## Requirements

For this to work tagger for language package needs to be downloaded first like so:
```
>>> import nltk
>>> nltk.download('averaged_perceptron_tagger')
```

Also requires `git` to be installed on the system and available in `PATH`.
If it is not in your `PATH`, you can help GitPython (that is used underneath) find it by setting the `GIT_PYTHON_GIT_EXECUTABLE=<path/to/git>` environment variable.
After that you are all set to go.

Usage example can be found in example.py

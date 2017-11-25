# Identifier words stats

## Features
This tool can be used to calculate statistics of what words are used in identifiers in the code. 
 For now it supports code in `python`
 
 Can extract words from:
 - variables
 - function names
 
 Divides words into:
 - nouns
 - verbs
 
 It also provides ways to display calculated statistics in:
 - JSON file
 - CSV file
 - console output
 
 Can download repositories from **github.com** and apply selected statistics calculation on it
 
## Requirements
#### PoS tagger
Apart from installing packages in requirements.txt part of speech tagger needs to be downloaded like so:
```
>>> import nltk
>>> nltk.download('averaged_perceptron_tagger')
```
#### git
Also requires `git` to be installed on the system and available in `PATH`.
If it is not in your `PATH`, you can help GitPython (that is used underneath) find it by setting the `GIT_PYTHON_GIT_EXECUTABLE=<path/to/git>` environment variable.

After that you are all set to go.

## Usage

CLI client is provided. It takes 4 to 5 arguments:
- url to repository to analyze
- part of speech to account for (`verb`, or `noun`)
- where to look for words (`functon`, or `variable`)
- where to save report (`json`, `csv`, or `console`)
- filename of report to save (only applicable for `json` and `csv`)

Results will be stored in `/tmp/results` directory which will be created if does not exist
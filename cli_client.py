import sys

from statistics_calculator.statistics import get_statistics
from statistics_calculator.data_extractor import PartOfSpeech, WordLocation
from statistics_calculator.results_presentor import ResultsRepresentationType
from statistics_calculator.exc import InvalidCliArgument


def cli_client():
    args_len = len(sys.argv)
    if not (5 <= args_len <= 6):
        print_help()

    try:
        repository_url = sys.argv[1]
        part_of_speech = sys.argv[2]
        word_location = sys.argv[3]
        report_type = sys.argv[4]

    except InvalidCliArgument:
        print_help()
        return

    if args_len == 5:
        filename = sys.argv[5]
    else:
        filename = None

    get_statistics(repository_url, part_of_speech, word_location, report_type, filename)


def parse_part_of_speech(pos):
    if pos == 'verb':
        return PartOfSpeech.VERB

    elif pos == 'noun':
        return PartOfSpeech.NOUN

    else:
        raise InvalidCliArgument


def parse_word_location(location):
    if location == 'function':
        return WordLocation.FUNCTION

    elif location == 'variable':
        return WordLocation.VARIABLE

    else:
        raise InvalidCliArgument


def parse_report_type(report_type):
    if report_type == 'console':
        return ResultsRepresentationType.CONSOLE

    elif report_type == 'csv':
        return ResultsRepresentationType.CSV_FILE

    elif report_type == 'json':
        return ResultsRepresentationType.JSON_FILE

    else:
        raise InvalidCliArgument


def print_help():
    print('There should be 4 or 5 arguments provided:\n',
          '1: url pf repository on github.com\n',
          '2: part of speech ("verb" or "noun")\n',
          '3: location of words ("function" or "variable"\n',
          '4: where to save report ("console", "csv", or "json"\n',
          'in case of json or csv:\n'
          '5: filename to store results.')


if __name__ == '__main__':
    cli_client()

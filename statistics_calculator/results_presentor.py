import json

import os
from collections import OrderedDict
from enum import Enum, auto


RESULTS_DIR = '/tmp/results'


class ResultsRepresentationType(Enum):
    CONSOLE = auto()
    JSON_FILE = auto()
    CSV_FILE = auto()


def present_results(counter, report_type, filename=None):

    if report_type == ResultsRepresentationType.JSON_FILE and filename:
        return present_in_json_file(counter, filename)

    elif report_type == ResultsRepresentationType.CSV_FILE and filename:
        return present_in_csv_file(counter, filename)

    elif report_type == ResultsRepresentationType.CONSOLE and filename:
        return present_in_console(counter)


def present_in_json_file(counter, filename):
    _create_dir_for_results_if_needed()
    filename = _form_full_file_name(filename)

    results = OrderedDict((k, v) for k, v in counter.most_common())

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(results, file, indent=4)


def present_in_console(counter):
    for word, occurrence in counter.most_common():
        print('{}: {}'.format(word, occurrence))


def present_in_csv_file(counter, filename):
    _create_dir_for_results_if_needed()
    filename = _form_full_file_name(filename)

    with open(filename, 'w', encoding='utf-8') as file:
        for word, occurrence in counter.most_common():
            file.write('{}: {}\n'.format(word, occurrence))


def _create_dir_for_results_if_needed():
    os.makedirs(RESULTS_DIR, exist_ok=True)


def _form_full_file_name(filename):
    return os.path.join(RESULTS_DIR, filename)

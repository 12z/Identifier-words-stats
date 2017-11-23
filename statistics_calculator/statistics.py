from .downloader import download_repo

from .data_extractor import PartOfSpeech, WordLocation
from .data_extractor import get_data
from .results_presentor import ResultsRepresentationType

from .occurrences_calculator import calculate_frequencies
from .results_presentor import present_results


NUMBER_OF_TOP_VERBS = 10


def get_statistics(repository_url, part_of_speech, word_location, report_type, filename=None):
    repo_path = download_repo(repository_url)
    data = get_data(repo_path)
    counter = calculate_frequencies(data, part_of_speech, word_location)
    present_results(counter, report_type, filename)


if __name__ == '__main__':

    repo_url = 'https://github.com/gitpython-developers/GitPython'
    pos = PartOfSpeech.NOUN
    location = WordLocation.FUNCTION
    type_of_report = ResultsRepresentationType.CONSOLE
    report_file = 'test.json'

    get_statistics(repo_url, pos, location, type_of_report, report_file)

class StatisticsCalculatorError(ValueError):
    """
    Base exception for all exceptions in the module
    """


class RepositoryCloningError(StatisticsCalculatorError):
    def __init__(self):
        super().__init__('Unable to clone repository')


class RepositoryUrlError(StatisticsCalculatorError):
    def __init__(self):
        super().__init__('Repository URL cannot be reached or invalid')


class InvalidCliArgument(StatisticsCalculatorError):
    def __init__(self):
        super().__init__('Invalid argument provided to CLI')

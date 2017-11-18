class StatisticsCalculatorError(ValueError):
    """
    Base exception for all exceptions in the module
    """


class RepositoryCloningError(StatisticsCalculatorError):
    def __init__(self):
        super().__init__('Unable to clone repository')

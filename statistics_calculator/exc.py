class StatisticsCalculatorError(ValueError):
    """
    Base exception for all exceptions in the module
    """


class RepositoryExistsError(StatisticsCalculatorError):
    def __init__(self):
        super().__init__('Repository being cloned already exists on disk')

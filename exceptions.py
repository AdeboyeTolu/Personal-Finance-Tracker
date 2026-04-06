"""
Custom exceptions for the Personal Finance Tracker.
"""


class BudgetExceededError(Exception):
    """Raised when spending exceeds the budget limit."""
    pass


class InvalidTransactionError(Exception):
    """Raised when a transaction has invalid data."""
    pass


class DuplicateTransactionError(Exception):
    """Raised when an identical transaction already exists."""
    pass

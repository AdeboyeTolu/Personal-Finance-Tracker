"""
Transaction model for the Personal Finance Tracker.
"""

import logging
from datetime import datetime
from exceptions import InvalidTransactionError

logger = logging.getLogger("FinanceTracker")


class Transaction:
    """Represents a single financial transaction."""

    VALID_TYPES = ("income", "expense")

    def __init__(self, date, amount, category, description, trans_type):
        """
        Initialise a new Transaction.

        Raises:
            InvalidTransactionError: If any field is invalid.
        """
        # TODO: Validate date format using datetime.strptime.
        # TODO: Validate amount > 0.
        # TODO: Validate trans_type is "income" or "expense".
        # TODO: Validate category and description are non-empty.
        # TODO: Assign all attributes.
        pass

    def is_expense(self):
        """Return True if this is an expense."""
        # TODO: Check self.trans_type
        pass

    def get_month(self):
        """Return the month portion as YYYY-MM."""
        # TODO: Return self.date[:7]
        pass

    def __str__(self):
        """Return a formatted string for display."""
        # TODO: Use f-string with aligned columns.
        pass

    def to_dict(self):
        """Convert to dictionary for JSON serialisation."""
        # TODO: Return dict with all attributes.
        pass

    @classmethod
    def from_dict(cls, data):
        """Create a Transaction from a dictionary."""
        # TODO: Unpack dict and return new Transaction.
        pass

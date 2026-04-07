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
        # Validating the date format
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise InvalidTransactionError("Invalid date format. Use YYYY-MM-DD.")

        # TODO: Validate amount > 0.
        # Validating the amount
        if amount <= 0:
            raise InvalidTransactionError("Amount must be greater than zero.")

        # TODO: Validate trans_type is "income" or "expense".
        # validating the transaction type
        if trans_type not in self.VALID_TYPES:
            raise InvalidTransactionError(
                "Invalid transaction type. Must be an 'income' or 'expense'."
            )

        # TODO: Validate category and description are non-empty.
        # Validating the category and description
        # Using the strip() method to clean the 'string' attributes.

        if not category.strip():
            raise InvalidTransactionError("Category cannot be empty.")

        # Validating the description
        if not description.strip():
            raise InvalidTransactionError("Description cannot be empty.")

        # TODO: Assign all attributes.
        self.date = date
        self.amount = amount
        self.category = category.strip()
        self.description = description.strip()
        self.trans_type = trans_type

    def is_expense(self):
        """Return True if this is an expense."""
        # TODO: Check self.trans_type
        return self.trans_type == "expense"
        # pass
        # No need to define is_income() since there can only be two types of transactions.

    def get_month(self):
        """Return the month portion as YYYY-MM."""
        # TODO: Return self.date[:7]
        # returns the first seven characters of the date string - YYYY-MM.
        return self.date[:7]
        # pass

    def __str__(self):
        """Returning a formatted string for display."""
        # TODO: Use f-string with aligned columns.
        # This returns the f-string in columns, separated by Tabs(\t).
        return f"{self.date}\t{self.amount}\t{self.category}\t{self.description}"
        # pass

    def to_dict(self):
        """Converting to dictionary for JSON serialisation."""
        # TODO: Return dict with all attributes.
        # Creating a dictionary with the transaction attributes, for easy serialization to JSON format.
        return {
            "date": self.date,
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "trans_type": self.trans_type,
        }
        # pass

    @classmethod
    def from_dict(cls, data):
        """Create a Transaction from a dictionary."""
        # TODO: Unpack dict and return new Transaction.
        # using the **data kwarg to unpack the dictionary above and pass its values as keyword arguments to the transaction constructor.
        return cls(**data)

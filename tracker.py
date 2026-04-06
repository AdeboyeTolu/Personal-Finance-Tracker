"""
FinanceTracker class for the Personal Finance Tracker.
"""

import json
import logging
import os

from transaction import Transaction
from budget import Budget

logger = logging.getLogger("FinanceTracker")


class FinanceTracker:
    """Central class managing transactions and budgets."""

    def __init__(self, data_file="data/transactions.json",
                 budget_file="data/budgets.json"):
        self.transactions = []
        self.budgets = {}
        self.data_file = data_file
        self.budget_file = budget_file
        # TODO: Call load methods to restore saved data.

    def add_transaction(self, transaction):
        """Add a transaction and check budget status."""
        # TODO: Append transaction, log it.
        # TODO: If expense, compute total spent for that category
        #       this month (use a comprehension) and check budget.
        pass

    def _total_spent(self, month, category):
        """Calculate total spent in a category for a month."""
        # TODO: Use a generator expression with sum().
        pass

    def get_transactions_by_category(self, category):
        """Filter transactions by category."""
        # TODO: Return filtered list using a comprehension.
        pass

    def summary_by_category(self, trans_type=None):
        """Compute totals grouped by category."""
        # TODO: Filter by type if specified, aggregate per category.
        pass

    def monthly_report(self, month):
        """Generate a formatted report for a specific month."""
        # TODO: Filter transactions, compute totals, display.
        pass

    def budget_status(self, month):
        """Show budget vs actual for each category."""
        # TODO: Display budget remaining per category.
        pass

    def save_data(self):
        """Save transactions and budgets to JSON."""
        # TODO: Write both files with try/except.
        pass

    def load_data(self):
        """Load transactions and budgets from JSON."""
        # TODO: Read files, handle missing/corrupt files.
        pass

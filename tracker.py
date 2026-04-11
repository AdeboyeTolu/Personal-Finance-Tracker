"""
FinanceTracker class for the Personal Finance Tracker.
"""

import json
import logging
import os

from exceptions import DuplicateTransactionError
from transaction import Transaction
from budget import Budget

logger = logging.getLogger("FinanceTracker")


class FinanceTracker:
    """Central class managing transactions and budgets."""

    def __init__(
        self, data_file="data/transactions.json", budget_file="data/budgets.json"
    ):
        self.transactions = []
        self.budgets = {}
        self.data_file = data_file
        self.budget_file = budget_file

        # TODO: Call load methods to restore saved data.
        self.load_data()

    # =======================================================================

    def add_transaction(self, transaction):
        """Add a transaction and check budget status."""
        # TODO: Append transaction, log it.
        if transaction in self.transactions:
            raise DuplicateTransactionError(
                "Transaction already exists."
            )  # This is a check to prevent duplicate transactions from being added to the tracker.

        else:
            self.transactions.append(transaction)
            logger.info(
                f"Added transaction: {transaction.description} - {transaction.amount} on {transaction.date} in category {transaction.category} as a {transaction.trans_type}."
            )

        # TODO: If expense, compute total spent for that category
        if transaction.trans_type == "expense":
            month = transaction.date[:7]  # Extract the date in "YYYY-MM"
            category = transaction.category
            spent = self._total_spent(month, category)

            # Check if there's a budget for this month and category.
            if month in self.budgets:
                budget = self.budgets[month]
                within_budget = budget.check(category, spent)

                if not within_budget:
                    logger.warning(
                        f"Budget exceeded for {category} in {month}. Spent: {spent}, Limit: {budget.limits.get(category, 'No limit set')}"
                    )
                else:
                    logger.info(
                        f"Within budget for {category} in {month}. Spent: {spent}, Limit: {budget.limits.get(category, 'No limit set')}"
                    )

    # =======================================================================

    def _total_spent(self, month, category):
        """Calculate total spent in a category for a month."""
        # TODO: Use a generator expression with sum().
        total = sum(
            t.amount
            for t in self.transactions
            if t.date.startswith(month)
            and t.category == category
            and t.trans_type
            == "expense"  # By default, expenses are the only transactions that count as money spent.
        )
        return total

    # =======================================================================

    def get_transactions_by_category(self, category):
        """Filter transactions by category."""
        # TODO: Return filtered list using a comprehension.
        return [t for t in self.transactions if t.category == category]

    # =======================================================================

    def summary_by_category(self, trans_type=None):
        """Compute totals grouped by category."""
        # TODO: Filter by type if specified, aggregate per category.
        summary = {}
        for t in self.transactions:
            if trans_type is None or t.trans_type == trans_type:
                summary[t.category] = summary.get(t.category, 0) + t.amount
        return summary

    # To explain the above code: It iterates through all transactions and checks if the transaction type matches the specified type (if provided).
    # If it does, it adds the transaction amount to the corresponding category in the summary dictionary.

    # =======================================================================

    def monthly_report(self, month):
        """Generate a formatted report for a specific month."""
        # TODO: Filter transactions, compute totals, display.
        monthly_transactions = [
            t for t in self.transactions if t.date.startswith(month)
        ]

        income_summary = sum(
            t.amount for t in monthly_transactions if t.trans_type == "income"
        )
        expense_summary = sum(
            t.amount for t in monthly_transactions if t.trans_type == "expense"
        )

        print(f"MONTHLY REPORT FOR {month}")
        print("=" * 50)
        print(f"Total Income: {income_summary}")
        print(f"Total Expenses: {expense_summary}")
        print(f"Net Savings: {income_summary - expense_summary}")
        print("-" * 50)
        print("Transactions:")
        for t in monthly_transactions:
            print(t)

    # =======================================================================

    def budget_status(self, month):
        """Show budget vs actual for each category."""
        # TODO: Display budget remaining per category.
        if month not in self.budgets:
            print(f"No budget set for {month}.")
            return

        budget = self.budgets[month]

        print(f"BUDGET STATUS FOR {month}")
        print("=" * 50)

        for category, limit in budget.limits.items():
            spent = self._total_spent(month, category)
            remaining = budget.remaining(category, spent)
            print(f"Category: {category}")
            print(f"Budget Limit: {limit}")
            print(f"Spent: {spent}")
            print(
                f"Remaining: {remaining if remaining is not None else 'No limit set'}"
            )
            print("-" * 50)

    # =======================================================================

    def save_data(self):
        """Save transactions and budgets to JSON."""
        # TODO: Write both files with try/except.

        try:
            dirname = os.path.dirname(self.data_file)
            if dirname:
                os.makedirs(dirname, exist_ok=True)  # Ensure the directory exists.
            # Not sure if it'll work without this line. #Still need to research this.

            with open(self.data_file, "w") as f:
                json.dump([t.to_dict() for t in self.transactions], f, indent=4)
            logger.info("Transactions saved successfully.")
        except Exception as e:
            logger.error(f"Failed to save transactions: {e}")
        # The above code attempts to save the transactions to a JSON file.
        # It first ensures that the directory for the data file exists, then writes the transactions to the file in JSON format.
        # If any errors occur during this process, they are logged.

        try:
            with open(self.budget_file, "w") as f:
                json.dump(
                    {month: budget.to_dict() for month, budget in self.budgets.items()},
                    f,
                    indent=4,
                )
            logger.info("Budgets saved successfully.")
        except Exception as e:
            logger.error(f"Failed to save budgets: {e}")
        # The above code attempts to save the budgets to a JSON file in a similar manner to the transactions.
        # It converts each budget to a dictionary and saves them in a JSON file.
        # If any errors occur during this process, they are logged.

    # =======================================================================

    def load_data(self):
        """Load transactions and budgets from JSON."""
        # TODO: Read files, handle missing/corrupt files.
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as f:
                    transactions_data = json.load(f)
                    self.transactions = [
                        Transaction.from_dict(td) for td in transactions_data
                    ]
                logger.info("Transactions loaded successfully.")
            except Exception as e:
                logger.error(f"Failed to load transactions: {e}")
                self.transactions = []
        else:
            logger.warning(f"Transactions file not found: {self.data_file}")
            self.transactions = []

        if os.path.exists(self.budget_file):
            try:
                with open(self.budget_file, "r") as f:
                    budgets_data = json.load(f)
                    self.budgets = {
                        month: Budget.from_dict(bd)
                        for month, bd in budgets_data.items()
                    }
                logger.info("Budgets loaded successfully.")
            except Exception as e:
                logger.error(f"Failed to load budgets: {e}")
                self.budgets = {}
        else:
            logger.warning(f"Budgets file not found: {self.budget_file}")
            self.budgets = {}

"""
Budget model for the Personal Finance Tracker.
"""

import logging
from datetime import datetime

logger = logging.getLogger("FinanceTracker")


class Budget:
    """Manages monthly spending limits per category."""

    def __init__(self, month, limits=None):
        """
        Initialise a Budget for a given month.

        Args:
            month (str): Month in "YYYY-MM" format.
            limits (dict, optional): Initial category limits.
        """
        # TODO: Validate month format.
        try:
            datetime.strptime(month, "%Y-%m")
        except ValueError:
            raise ValueError("Invalid month format. Use YYYY-MM.")

        # TODO: Assign attributes (empty dict if limits is None).
        self.month = month
        self.limits = limits
        if limits is None:
            self.limits = {}

    # =======================================================================

    def set_limit(self, category, amount):
        """Set or update the spending limit for a category."""
        # TODO: Validate amount > 0, set limit, log.
        # The code below valdates that a category is provided when setting a budget limit.
        category = category.strip()
        # The strip() method ensures that users cannot input just empty spaces as a category name.
        if not category:
            raise ValueError("A category must be provided.")

        # This next block of code validates that the amount is greater than zero.
        if amount <= 0:
            raise ValueError("Amount must be greater than Zero")

        # The next line of code sets the budget limit for the specified category in the limits dictionary.
        self.limits[category] = amount

        # Logging that the budget limit for a category has been set or updated.
        logger.info(f"Set budget limit for {category}: {amount}")

    # =======================================================================

    def check(self, category, spent):
        """Return True if within budget, False if over."""
        # TODO: Compare spent against limit. Return True if no limit set.
        # True means it is within the budget.
        # False means it is over the budget.

        if category not in self.limits:
            return True
        # If no limits is set for the category, we assume it is within budget.

        if spent <= self.limits[category]:
            return True
        else:
            return False
        # the above code compares the amount spent against the limit for the category.

    # =======================================================================

    def remaining(self, category, spent):
        """Return remaining budget, or None if no limit set."""
        # TODO: Compute limit - spent.
        if category not in self.limits:
            return None
        # Since no limit is set for the category, there is no remaining budget to work with.

        remaining_budget = self.limits[category] - spent
        # the above code calculates the remaining budget for the category using (Limit - Spent).
        if remaining_budget < 0:
            return 0  # If the user has already exceeded the budget, the remaining budget is 0.
        else:
            return remaining_budget
        # Remaining budget cannot be negative (Might Remove this code later).

    # =======================================================================

    def to_dict(self):
        # Converting to dictionary for JSON serialisation.
        return {
            "month": self.month,
            "limits": self.limits,
        }

    # =======================================================================

    @classmethod
    def from_dict(cls, data):
        # creating a budget instance from the above dictionary.
        return cls(month=data["month"], limits=data["limits"])
        # Placeholder code - Not yet sure why this is better: return cls(month=data["month"], limits=data.get("limits", {}))

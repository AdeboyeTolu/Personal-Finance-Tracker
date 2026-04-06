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
        # TODO: Assign attributes (empty dict if limits is None).
        pass

    def set_limit(self, category, amount):
        """Set or update the spending limit for a category."""
        # TODO: Validate amount > 0, set limit, log.
        pass

    def check(self, category, spent):
        """Return True if within budget, False if over."""
        # TODO: Compare spent against limit. Return True if no limit set.
        pass

    def remaining(self, category, spent):
        """Return remaining budget, or None if no limit set."""
        # TODO: Compute limit - spent.
        pass

    def to_dict(self):
        pass

    @classmethod
    def from_dict(cls, data):
        pass

"""
Test Suite for Project 2: Personal Finance Tracker
Run with: python -m unittest tests/test_tracker.py -v
"""

import unittest
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from transaction import Transaction
from budget import Budget
from tracker import FinanceTracker
from exceptions import InvalidTransactionError


class TestTransaction(unittest.TestCase):
    def test_create_valid_expense(self):
        pass
    def test_negative_amount_raises(self):
        pass
    def test_invalid_type_raises(self):
        pass
    def test_invalid_date_format_raises(self):
        pass
    def test_is_expense(self):
        pass
    def test_to_dict_and_from_dict(self):
        pass


class TestBudget(unittest.TestCase):
    def test_set_and_check_within_budget(self):
        pass
    def test_check_over_budget(self):
        pass
    def test_remaining_calculation(self):
        pass
    def test_no_limit_returns_true(self):
        pass


class TestFinanceTracker(unittest.TestCase):
    def test_add_transaction(self):
        pass
    def test_summary_by_category(self):
        pass
    def test_save_and_load(self):
        pass


if __name__ == "__main__":
    unittest.main()

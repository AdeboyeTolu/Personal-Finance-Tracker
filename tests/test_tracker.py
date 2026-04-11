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

# =======================================================================


class TestTransaction(unittest.TestCase):
    def test_create_valid_expense(self):
        t = Transaction(
            "2024-04-10", 5000.55, "FoodTest", "default description", "expense"
        )
        self.assertEqual(t.date, "2024-04-10")
        self.assertEqual(t.category, "FoodTest")
        self.assertEqual(t.amount, 5000.55)
        self.assertEqual(t.description, "default description")
        self.assertEqual(t.trans_type, "expense")

    # =======================================================================

    def test_create_valid_income(self):
        t = Transaction(
            "2024-04-10", 500000.0, "Freelance work", "default description", "income"
        )
        self.assertEqual(t.date, "2024-04-10")
        self.assertEqual(t.category, "Freelance work")
        self.assertEqual(t.amount, 500000.0)
        self.assertEqual(t.description, "default description")
        self.assertEqual(t.trans_type, "income")
        self.assertFalse(t.is_expense())

    # =======================================================================

    def test_negative_amount_raises(self):
        with self.assertRaises(InvalidTransactionError):
            Transaction(
                "2024-04-10",
                -100.50,
                "NegativeAmountTest",
                "default description",
                "expense",
            )
            # The "with self.assertRaises(InvalidTransactionError):" statement is used in unit testing to assert that a specific exception (in this case, InvalidTransactionError) is raised when executing the code block within the "with" statement.
            # It allows you to test that your code correctly handles error conditions by raising the expected exceptions when invalid input or situations occur.
            # In this test case, we are checking that creating a Transaction with a negative amount raises an InvalidTransactionError, which is the expected behavior for our finance tracker application.

    # =======================================================================

    def test_invalid_type_raises(self):
        with self.assertRaises(InvalidTransactionError):
            Transaction(
                "2024-04-10",
                100.50,
                "InvalidTypeTest",
                "default description",
                "invalid_type",
            )

    # =======================================================================

    def test_invalid_date_format_raises(self):
        with self.assertRaises(InvalidTransactionError):
            Transaction(
                "invalid_date",
                100.0,
                "InvalidDateTest",
                "default description",
                "expense",
            )

    # =======================================================================

    def test_is_expense(self):
        t1 = Transaction(
            "2024-04-10", 100.50, "ExpenseTest", "default description", "expense"
        )
        t2 = Transaction(
            "2024-04-10", 100.50, "IncomeTest", "default description", "income"
        )
        self.assertTrue(t1.is_expense())
        self.assertFalse(t2.is_expense())

    # =======================================================================

    def test_to_dict_and_from_dict(self):
        t1 = Transaction(
            "2024-04-10", 100.50, "TestDictionaries", "default description", "expense"
        )
        t_dict = t1.to_dict()
        expected_dict = {
            "date": "2024-04-10",
            "amount": 100.50,
            "category": "TestDictionaries",
            "description": "default description",
            "trans_type": "expense",
        }
        self.assertEqual(t_dict, expected_dict)

        # Testing that we can create a Transaction object from a dictionary and that the attributes are correctly set.

        t2 = Transaction.from_dict(t_dict)
        self.assertEqual(t2.date, t1.date)
        self.assertEqual(t2.category, t1.category)
        self.assertEqual(t2.amount, t1.amount)
        self.assertEqual(t2.trans_type, t1.trans_type)
        self.assertEqual(t2.description, t1.description)


# =======================================================================


class TestBudget(unittest.TestCase):
    def test_set_and_check_within_budget(self):
        t = Budget("2024-04")
        t.set_limit("Food", 1000)
        self.assertTrue(t.check("Food", 500))

    def test_check_over_budget(self):
        t = Budget("2024-04")
        t.set_limit("Food", 1000)
        self.assertFalse(t.check("Food", 1500))

    def test_remaining_calculation(self):
        t = Budget("2024-04")
        t.set_limit("Food", 1000)
        self.assertEqual(t.remaining("Food", 500), 500)

    def test_no_limit_returns_true(self):
        t = Budget("2024-04")
        self.assertTrue(t.check("Food", 500))


# =======================================================================


class TestFinanceTracker(unittest.TestCase):
    def test_add_transaction(self):
        tracker = FinanceTracker()
        t = Transaction(
            "2024-04-10", 100.50, "TestAddTransaction", "default description", "expense"
        )
        tracker.add_transaction(t)
        self.assertIn(t, tracker.transactions)

    # =======================================================================

    def test_summary_by_category(self):
        tracker = FinanceTracker(
            data_file="test_transactions.json", budget_file="test_budgets.json"
        )
        t1 = Transaction(
            "2024-04-10",
            100.50,
            "FoodCategorySumTest",
            "default description",
            "expense",
        )
        t2 = Transaction(
            "2024-04-11", 50.00, "FoodCategorySumTest", "default description", "expense"
        )
        t3 = Transaction(
            "2024-04-12",
            2000.00,
            "SalaryCategorySumTest",
            "default description",
            "income",
        )
        tracker.add_transaction(t1)
        tracker.add_transaction(t2)
        tracker.add_transaction(t3)
        summary = tracker.summary_by_category()
        expected_summary = {
            "FoodCategorySumTest": 150.50,
            "SalaryCategorySumTest": 2000.00,
        }
        self.assertEqual(summary, expected_summary)

    # =======================================================================

    def test_save_and_load(self):
        tracker = FinanceTracker(
            data_file="test_transactions.json", budget_file="test_budgets.json"
        )
        t = Transaction(
            "2024-04-10", 100.50, "TestSaveLoad", "default description", "expense"
        )
        tracker.add_transaction(t)
        tracker.save_data()

        # Creating a new tracker instance to load the data
        new_tracker = FinanceTracker(
            data_file="test_transactions.json", budget_file="test_budgets.json"
        )
        self.assertEqual(len(new_tracker.transactions), 1)
        loaded_transaction = new_tracker.transactions[0]

        self.assertEqual(loaded_transaction.date, t.date)
        self.assertEqual(loaded_transaction.category, t.category)
        self.assertEqual(loaded_transaction.amount, t.amount)
        self.assertEqual(loaded_transaction.description, t.description)
        self.assertEqual(loaded_transaction.trans_type, t.trans_type)

        # Clean up test files
        os.remove("test_transactions.json")
        os.remove("test_budgets.json")


# =======================================================================

if __name__ == "__main__":
    unittest.main()

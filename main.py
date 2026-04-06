"""
Project 2: Personal Finance Tracker
Entry point. Run with: python main.py
"""

import logging
import os

from transaction import Transaction
from budget import Budget
from tracker import FinanceTracker
from exceptions import InvalidTransactionError, BudgetExceededError

# TODO: Configure logging (console INFO + file DEBUG)
logger = logging.getLogger("FinanceTracker")


def display_menu():
    print("\n" + "=" * 50)
    print("   Personal Finance Tracker")
    print("=" * 50)
    print("1. Add a transaction")
    print("2. View all transactions")
    print("3. View transactions by category")
    print("4. Monthly report")
    print("5. Set a budget limit")
    print("6. Budget status")
    print("7. Summary by category")
    print("8. Save and exit")
    print("=" * 50)


def main():
    tracker = FinanceTracker()

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-8): ").strip()

        if choice == "1":
            # TODO: Prompt for date, amount, category, description, type
            # TODO: Create Transaction and add to tracker
            pass
        elif choice == "2":
            # TODO: Display all transactions
            pass
        elif choice == "3":
            # TODO: Filter by category
            pass
        elif choice == "4":
            # TODO: Monthly report
            pass
        elif choice == "5":
            # TODO: Set budget limit
            pass
        elif choice == "6":
            # TODO: Budget status
            pass
        elif choice == "7":
            # TODO: Summary by category
            pass
        elif choice == "8":
            tracker.save_data()
            print("\nData saved. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""
Created on Wed May  3 16:56:23 2023

@author: sarah
"""

import csvreader
import csv

def show_menu():
    print("\n===== Budget Management System =====")
    print("1. Expenses")
    print("2. Savings Goals")
    print("3. Budgets")
    print("4. Exit")

def expenses_menu():
    print("\n===== Expenses Menu =====")
    # Add your expenses-related options here
    csvreader.getExpCat()

def savings_goals_menu():
    print("\n===== Savings Goals Menu =====")
    # Add your savings goals-related options here
    csvreader.getSavGoal()
                
import csvreader
import csv

def show_menu():
    print("\n===== Budget Management System =====")
    print("1. Expenses")
    print("2. Savings Goals")
    print("3. Budgets")
    print("4. Exit")

def expenses_menu():
    print("\n===== Expenses Menu =====")
    # Add your expenses-related options here
    csvreader.getExpCat()

def savings_goals_menu():
    print("\n===== Savings Goals Menu =====")
    # Add your savings goals-related options here
    csvreader.getSavGoal()
                
def budgets_menu():
    print("\n===== Budgets Menu =====")
    csv_income = 'income.csv'
    with open(csv_income) as f:
        total_income = sum(int(r['Amount(Euro)']) for r in csv.DictReader(f))
            
    csv_expenses = 'expenses.csv'
    with open(csv_expenses) as f:
        total_expenses = sum(int(r['Amount(Euro)']) for r in csv.DictReader(f))

    if total_income is not None and total_expenses is not None:
        total_balance = total_income - total_expenses
        print("Your total income is:", total_income)
        print("Your total expenses are:", total_expenses)
        print("Your total balance is:", total_balance)

def create_custom_budget(total_balance):
    budget_name = input("Enter a name for your custom budget: ")
    budget_amount = input("Enter the amount to allocate for this budget: ")

    try:
        allocated_amount = float(budget_amount)
        remaining_balance = total_balance - allocated_amount
        print("Budget created successfully!")
        print(f"'{budget_name}' budget has been allocated {allocated_amount}.")
        print(f"Remaining balance: {remaining_balance}")
    except ValueError:
        print("Invalid input. Please enter a valid number for the allocated amount.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            expenses_menu()
        elif choice == "2":
            savings_goals_menu()
        elif choice == "3":
            budgets_menu()
        elif choice == "4":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


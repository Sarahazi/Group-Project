
import csv
from datetime import datetime

 


class User:
    def __init__(self, name, income_sources):
        self.name = name
        self.income_sources = income_sources
        self.savings_goal = 0

 

    def set_savings_goal(self, goal):
        self.savings_goal = goal

 

    def add_income_source(self, source):
        self.income_sources.append(source)

 

    def get_total_income(self):
        total_income = 0
        for source in self.income_sources:
            total_income += source.get_income()
        return total_income

 

    def track_savings_progress(self):
        if self.savings_goal == 0:
            return 0
        savings_progress = (self.get_total_income() / self.savings_goal) * 100
        return savings_progress

 


class IncomeSource:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

 

    def get_income(self):
        return self.amount

 


class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category

 

    def get_amount(self):
        return self.amount

 


class Budget:
    def __init__(self, user, expenses):
        self.user = user
        self.expenses = expenses

 

    def calculate_total_expenses(self):
        total_expenses = 0
        for expense in self.expenses:
            total_expenses += expense.get_amount()
        return total_expenses

 

    def generate_budget_report(self):
        total_income = self.user.get_total_income()
        total_expenses = self.calculate_total_expenses()
        savings = total_income - total_expenses

 

        report = f"Budget Report\n\nTotal Income: ${total_income}\nTotal Expenses: ${total_expenses}\nSavings: ${savings}"

 

        return report

 


def read_csv_file(file_path):
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        next(reader)
        data = []
        for row in reader:
            if 'Amount' in row:
                row['Amount'] = float(row['Amount'])
            data.append(row)
        return data

 

category_data = read_csv_file('categories.csv')
category_dict = {}
for row in category_data:
    category_dict[row['Description']] = row['Category']

 

transaction_data = read_csv_file('transactions.csv')
income_data = read_csv_file('incomes.csv')

 

# Create Expense and IncomeSource objects from transactions and incomes
expenses = []
for row in transaction_data:
    category = category_dict.get(row['Description'], '')
    expenses.append(Expense(row['Description'], row['Amount'], category))

 

income_sources = []
for row in income_data:
    income_sources.append(IncomeSource(row['Description'], row['Amount']))

 

# Create User and Budget objects
user = User("User Name", income_sources)
budget = Budget(user, expenses)

 


def console_interface():
    while True:
        print("\nSelect an option:")
        print("1. View Budget Report")
        print("2. View Savings Progress")
        print("3. Exit")
        user_input = input("\nEnter your choice: ")
        if user_input == "1":
            print(budget.generate_budget_report())
        elif user_input == "2":
            print(f"Savings Progress: {user.track_savings_progress()}%")
        elif user_input.upper() == "3" or user_input.upper() == "EXIT":
            break
        else:
            print("Invalid choice. Please try again.")

 

console_interface()

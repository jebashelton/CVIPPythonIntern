class Expense:
    def __init__(self, description, amount, paid_by, split_with):
        self.description = description
        self.amount = amount
        self.paid_by = paid_by
        self.split_with = split_with

class User:
    def __init__(self, name):
        self.name = name
        self.owes = {}
        self.owed_by = {}

class ExpenseManager:
    def __init__(self):
        self.users = {}

    def add_user(self, name):
        if name not in self.users:
            self.users[name] = User(name)

    def add_expense(self, description, amount, paid_by, split_with):
        expense = Expense(description, amount, paid_by, split_with)
        self.calculate_expense(expense)

    def calculate_expense(self, expense):
        amount_per_person = expense.amount / len(expense.split_with)
        
        for user in expense.split_with:
            if user != expense.paid_by:
                self.users[user].owes.setdefault(expense.paid_by, 0)
                self.users[user].owes[expense.paid_by] += amount_per_person
        
        self.users[expense.paid_by].owed_by.setdefault(expense.paid_by, 0)
        self.users[expense.paid_by].owed_by[expense.paid_by] += amount_per_person * (len(expense.split_with) - 1)

    def print_balance(self):
        print("Balance Summary:")
        for user in self.users.values():
            print(f"{user.name} owes:")
            for creditor, amount in user.owes.items():
                print(f"- {creditor}: {amount}")
            print(f"{user.name} is owed by:")
            for debtor, amount in user.owed_by.items():
                print(f"- {debtor}: {amount}")

def get_users():
    users = []
    while True:
        user_input = input("Enter user name (or 'done' to finish): ").strip()
        if user_input.lower() == 'done':
            break
        users.append(user_input)
    return users

def get_expense_details(users):
    description = input("Enter description of the expense: ").strip()
    amount = float(input("Enter the amount: "))
    paid_by = input("Enter the name of the person who paid: ").strip()
    while paid_by not in users:
        print("Invalid user. Please enter a valid name.")
        paid_by = input("Enter the name of the person who paid: ").strip()
    split_with = []
    while True:
        user_input = input("Enter the name of the person to split with (or 'done' to finish): ").strip()
        if user_input.lower() == 'done':
            break
        elif user_input not in users:
            print("Invalid user. Please enter a valid name.")
        else:
            split_with.append(user_input)
    return description, amount, paid_by, split_with

def main():
    manager = ExpenseManager()

    print("Welcome to the Expense Sharing App!")

    users = get_users()
    for user in users:
        manager.add_user(user)

    while True:
        choice = input("Enter 'a' to add an expense, 'p' to print balance, or 'q' to quit: ").strip().lower()
        if choice == 'a':
            expense_details = get_expense_details(users)
            manager.add_expense(*expense_details)
        elif choice == 'p':
            manager.print_balance()
        elif choice == 'q':
            print("Thank you for using the Expense Sharing App!")
            break
        else:
            print("Invalid choice. Please enter 'a', 'p', or 'q'.")

if __name__ == "__main__":
    main()

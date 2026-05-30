import os

class Expense:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description

    def __str__(self):
        return f"{self.amount},{self.category},{self.description}"


class ExpenseManager:
    FILE_NAME = "expenses.txt"

    def add_expense(self):
        amount = input("Enter Amount: ")
        category = input("Enter Category: ")
        description = input("Enter Description: ")

        expense = Expense(amount, category, description)

        with open(self.FILE_NAME, "a") as file:
            file.write(str(expense) + "\n")

        print("Expense Added Successfully!")

    def view_expenses(self):
        if not os.path.exists(self.FILE_NAME):
            print("No expenses found.")
            return

        with open(self.FILE_NAME, "r") as file:
            data = file.readlines()

        if not data:
            print("No expenses available.")
            return

        print("\n--- Expense List ---")
        for i, line in enumerate(data, start=1):
            amount, category, description = line.strip().split(",")
            print(f"{i}. Amount: ₹{amount}")
            print(f"   Category: {category}")
            print(f"   Description: {description}")
            print()

    def search_expense(self):
        category = input("Enter category to search: ")

        if not os.path.exists(self.FILE_NAME):
            print("No expenses found.")
            return

        found = False

        with open(self.FILE_NAME, "r") as file:
            for line in file:
                amount, cat, description = line.strip().split(",")

                if cat.lower() == category.lower():
                    print(
                        f"Amount: ₹{amount}, Category: {cat}, Description: {description}"
                    )
                    found = True

        if not found:
            print("No matching expense found.")

    def monthly_summary(self):
        if not os.path.exists(self.FILE_NAME):
            print("No expenses found.")
            return

        total = 0

        with open(self.FILE_NAME, "r") as file:
            for line in file:
                amount, _, _ = line.strip().split(",")
                total += float(amount)

        print(f"\nTotal Expenditure: ₹{total}")

    def delete_expense(self):
        if not os.path.exists(self.FILE_NAME):
            print("No expenses found.")
            return

        with open(self.FILE_NAME, "r") as file:
            expenses = file.readlines()

        self.view_expenses()

        try:
            index = int(input("Enter expense number to delete: ")) - 1

            if 0 <= index < len(expenses):
                expenses.pop(index)

                with open(self.FILE_NAME, "w") as file:
                    file.writelines(expenses)

                print("Expense Deleted Successfully!")
            else:
                print("Invalid Expense Number.")

        except ValueError:
            print("Please enter a valid number.")


def main():
    manager = ExpenseManager()

    while True:
        print("\n===== Personal Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expense")
        print("4. Monthly Summary")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            manager.add_expense()

        elif choice == "2":
            manager.view_expenses()

        elif choice == "3":
            manager.search_expense()

        elif choice == "4":
            manager.monthly_summary()

        elif choice == "5":
            manager.delete_expense()

        elif choice == "6":
            print("Thank You!")
            break

        else:
            print("Invalid Choice.")


if __name__ == "__main__":
    main()
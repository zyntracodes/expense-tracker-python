import datetime

def add_expense():
    item = input("Enter item name: ")
    amount = int(input("Enter amount: Rs. "))
    date = datetime.date.today()
    entry = f"{date} - {item} - Rs. {amount}\n"

    with open("expenses.txt", "a") as file:
        file.write(entry)

    print("Expense added successfully!\n")


def view_expenses():
    try:
        with open("expenses.txt", "r") as file:
            data = file.read()
        print("\n--- All Expenses ---")
        print(data)
    except FileNotFoundError:
        print("No expenses recorded yet!\n")


def total_expenses():
    try:
        with open("expenses.txt", "r") as file:
            lines = file.readlines()
            total = 0
            for line in lines:
                parts = line.strip().split(" - Rs. ")
                if len(parts) == 2:
                    total += int(parts[1])
            print(f"\nTotal Money Spent = Rs. {total}\n")
    except FileNotFoundError:
        print("No expenses found yet!")


while True:
    print("==== Expense Tracker ====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Clear All Expenses")
    print("4. Show Total Expenses")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_expense()
    elif choice == 2:
        view_expenses()
    elif choice == 3:
        open("expenses.txt", "w").close()
        print("All expenses cleared!\n")
    elif choice == 4:
        total_expenses()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.\n")

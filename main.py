# main.py
import menu
from expense import Expense
import file_manager
import reports
import utils

def handle_reports():
    """Handles the reports submenu."""
    while True:
        report_choice = menu.display_reports_menu()
        data = file_manager.load_all_expenses()
        if report_choice == '1':
            print(reports.generate_summary(data))
        elif report_choice == '2':
            print(reports.generate_category_chart(data))
        elif report_choice == '3':
            break
        else:
            print("Invalid choice, please try again.")

def main():
    while True:
        choice = menu.display_main_menu()
        
        if choice == '1': # Add Expense
            amt = input("Amount: ")
            if not utils.validate_amount(amt):
                print("Invalid amount!")
                continue
            
            cat = input("Category (e.g. Food, Rent): ")
            date = input("Date (YYYY-MM-DD): ")
            if not utils.validate_date(date):
                print("Invalid date format!")
                continue
                
            desc = input("Description: ")
            
            new_expense = Expense(amt, cat, date, desc)
            file_manager.save_expense(new_expense)
            print("Expense saved!")

        elif choice == '2': # View Reports
            handle_reports()

        elif choice == '3': # Manage Budgets
            print("Budget management feature coming soon!")

        elif choice == '4': # Export Data
            print("Data export feature coming soon!")

        elif choice == '5': # Backup Data
            if file_manager.create_backup():
                print("Backup created successfully.")
            else:
                print("No data to backup.")

        elif choice == '6': # Exit
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
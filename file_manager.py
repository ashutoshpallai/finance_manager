import csv
import os
import shutil

FILE_PATH = 'data/expenses.csv'
BACKUP_PATH = 'data/expenses_backup.csv'

def save_expense(expense):
    os.makedirs('data', exist_ok=True)
    
    with open(FILE_PATH, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["amount", "category", "date", "description"])
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(expense.to_dict())

def load_all_expenses():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, mode='r') as file:
        reader = csv.DictReader(file)
        # Check if header is missing (first row doesn't contain expected keys)
        if reader.fieldnames and "amount" not in reader.fieldnames:
            file.seek(0)
            reader = csv.DictReader(file, fieldnames=["amount", "category", "date", "description"])
        return list(reader)

def create_backup():
    if os.path.exists(FILE_PATH):
        shutil.copy(FILE_PATH, BACKUP_PATH)
        return True
    return False
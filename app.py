from flask import Flask, render_template, request, redirect, url_for
import file_manager
import reports
import utils
from expense import Expense

app = Flask(__name__)

@app.route('/')
def index():
    expenses = file_manager.load_all_expenses()
    summary = reports.get_summary_data(expenses)
    return render_template('index.html', expenses=expenses, summary=summary)

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        try:
            amount = request.form['amount']
            category = request.form['category']
            date = request.form['date']
            
            if not utils.validate_date(date):
                return "Invalid date format", 400

            description = request.form['description']
            
            new_expense = Expense(amount, category, date, description)
            file_manager.save_expense(new_expense)
            return redirect(url_for('index'))
        except ValueError:
            # Handle invalid float conversion for amount
            return "Invalid input", 400
            
    return render_template('add_expense.html')

if __name__ == '__main__':
    app.run(debug=True)
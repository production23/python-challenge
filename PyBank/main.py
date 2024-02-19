import csv
import os

# Define the file path
file_path = os.path.join("..", "Resources", "budget_data.csv")

# Variables
total_months = 0
total_profit_losses = 0
profit_losses_changes = []
months = []

# Read CSV file
try:
    with open(file_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader, None)

        if header is not None:
            for row in csvreader:
                if len(row) == 2:
                    total_months += 1
                    total_profit_losses += int(row[1])
                    profit_loss = int(row[1])

                    if months:
                        profit_losses_changes.append(profit_loss - previous_profit_loss)
                        months.append(row[0])
                    else:
                        months.append(row[0])

                    previous_profit_loss = profit_loss

            average_change = sum(profit_losses_changes) / len(profit_losses_changes) if profit_losses_changes else 0
            greatest_increase = max(profit_losses_changes) if profit_losses_changes else 0
            greatest_decrease = min(profit_losses_changes) if profit_losses_changes else 0

            greatest_increase_month = months[profit_losses_changes.index(greatest_increase)] if profit_losses_changes else None
            greatest_decrease_month = months[profit_losses_changes.index(greatest_decrease)] if profit_losses_changes else None

            print("Financial Analysis")
            print("-------------------------")
            print(f"Total Months: {total_months}")
            print(f"Total: ${total_profit_losses}")
            print(f"Average Change: ${average_change:.2f}")
            print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
            print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")
        else:
            print("Error: The file does not contain a header.")
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

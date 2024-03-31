import csv

def analyze_votes(csv_file):
    # Initialize variables to store data
    total_votes = 0
    candidate_votes = {}
    
    # Read the CSV file
    

    with open(csv_file,  newline="") as file:
        reader = csv.reader(file, delimiter=",")
        next(reader)  # Skip header row
        for row in reader:
            total_votes += 1
            candidate = row[2]  # Assuming candidate names are in the third column
            if candidate in candidate_votes:
                candidate_votes[candidate] += 1
            else:
                candidate_votes[candidate] = 1
    
    # Calculate percentages
    candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}
    
    # Find the winner
    winner = max(candidate_votes, key=candidate_votes.get)
    
    # Print results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate, votes in candidate_votes.items():
        print(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({votes})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

# Example usage:
analyze_votes("election_data.csv")
--------------------------------------------------------------------------------------
import csv


# Define file path
file_path = "budget_data.csv"

# Initialize variables
total_months = 0
total_profit_losses = 0
previous_profit_loss = 0
profit_loss_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

# Read the CSV file
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    next(csvreader)

    # Loop through rows in the CSV file
    for row in csvreader:
        # Calculate total number of months
        total_months += 1

        # Calculate total profit/losses
        total_profit_losses += int(row[1])

        # Calculate profit/loss change
        profit_loss_change = int(row[1]) - previous_profit_loss
        profit_loss_changes.append(profit_loss_change)
        previous_profit_loss = int(row[1])

        # Find greatest increase in profits
        if profit_loss_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = profit_loss_change

        # Find greatest decrease in profits
        if profit_loss_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = profit_loss_change

# Calculate the average of profit/loss changes
average_change = sum(profit_loss_changes) / len(profit_loss_changes)

# Output results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

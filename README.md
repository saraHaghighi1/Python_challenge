# Define file paths
input_file_path = "budget_data.txt"
output_file_path = "financial_analysis.txt"

# Initialize variables
total_months = 0
total_profit_losses = 0
previous_profit_loss = 0
profit_loss_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

# Read the text file
with open(input_file_path, 'r') as file:
    # Skip the header row
    next(file)

    # Loop through lines in the text file
    for line in file:
        # Split the line into parts
        parts = line.strip().split(",")

        # Extract month and profit/loss from parts
        month = parts[0]
        profit_loss = int(parts[1])

        # Calculate total number of months
        total_months += 1

        # Calculate total profit/losses
        total_profit_losses += profit_loss

        # Calculate profit/loss change
        profit_loss_change = profit_loss - previous_profit_loss
        profit_loss_changes.append(profit_loss_change)
        previous_profit_loss = profit_loss

        # Find greatest increase in profits
        if profit_loss_change > greatest_increase[1]:
            greatest_increase[0] = month
            greatest_increase[1] = profit_loss_change

        # Find greatest decrease in profits
        if profit_loss_change < greatest_decrease[1]:
            greatest_decrease[0] = month
            greatest_decrease[1] = profit_loss_change

# Calculate the average of profit/loss changes
average_change = sum(profit_loss_changes) / len(profit_loss_changes)

# Write analysis results to a text file
with open(output_file_path, 'w') as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months: {total_months}\n")
    outfile.write(f"Total: ${total_profit_losses}\n")
    outfile.write(f"Average Change: ${average_change:.2f}\n")
    outfile.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    outfile.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Output results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

print("Results have been saved to financial_analysis.txt")
--------------------------------------------------------------------------------------------------------
def analyze_votes(text_file, output_file):
    # Initialize variables to store data
    total_votes = 0
    candidate_votes = {}
    
    # Read the text file
    with open(text_file, 'r') as file:
        # Read lines from the file
        lines = file.readlines()
        
        # Iterate over each line
        for line in lines[1:]:  # Skip the header row
            # Split the line into parts based on delimiter (assuming it's a comma)
            parts = line.strip().split(",")
            
            # Extract candidate name from parts (assuming it's in the second part)
            candidate = parts[1]
            
            # Count total votes
            total_votes += 1
            
            # Update candidate votes
            if candidate in candidate_votes:
                candidate_votes[candidate] += 1
            else:
                candidate_votes[candidate] = 1
    
    # Calculate percentages
    candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}
    
    # Find the winner
    winner = max(candidate_votes, key=candidate_votes.get)
    
    # Write analysis results to a text file
    with open(output_file, 'w') as outfile:
        outfile.write("Election Results\n")
        outfile.write("-------------------------\n")
        outfile.write(f"Total Votes: {total_votes}\n")
        outfile.write("-------------------------\n")
        for candidate, votes in candidate_votes.items():
            outfile.write(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({votes})\n")
        outfile.write("-------------------------\n")
        outfile.write(f"Winner: {winner}\n")
        outfile.write("-------------------------\n")
    
    # Print results to the terminal
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
analyze_votes("election_data1.txt", "election_results.txt")



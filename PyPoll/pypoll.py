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

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

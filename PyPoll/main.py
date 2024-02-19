import csv
import os

# Define file path
file_path = os.path.join("..", "Resources", "election_data.csv")

# Variables
total_votes = 0
candidate_votes = {}

# Read the CSV file & calculate totals  
with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)  # Skip header
    for row in csvreader:
        total_votes = total_votes + 1
        candidate_votes[row[2]] = candidate_votes.get(row[2], 0) + 1

# Print results
print("Election Results")
print("_________________________________________")
print(f"Total Votes: {total_votes}")
print("_________________________________________")

# Find and print the winner
max_votes = max(candidate_votes.values())
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    if votes == max_votes:
        winner = candidate

print("_________________________________________")
print(f"Winner: {winner}")
print("_________________________________________")

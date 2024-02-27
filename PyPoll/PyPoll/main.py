import csv
import os

# Define the file path
file_path = os.path.join("Resources", "election_data.csv")

# Variables
total_votes = 0
candidates = {}
winner = ""
winner_count = 0

# Read CSV file
try:
    with open(file_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader, None)

        if header is not None:
            for row in csvreader:
                total_votes += 1
                candidate_name = row[2]

                if candidate_name in candidates:
                    candidates[candidate_name] += 1
                else:
                    candidates[candidate_name] = 1

            print("Election Results")
            print("-------------------------")
            print(f"Total Votes: {total_votes}")
            print("-------------------------")

            # Calculate and display the results for each candidate
            for candidate, votes in candidates.items():
                percentage = (votes / total_votes) * 100
                print(f"{candidate}: {percentage:.3f}% ({votes})")
                
                # Determine the winner
                if votes > winner_count:
                    winner_count = votes
                    winner = candidate

            print("-------------------------")
            print(f"Winner: {winner}")
            print("-------------------------")

            # Output to a text file
            output_file_path = "election_results.txt"
            with open(output_file_path, "w") as output_file:
                output_file.write("Election Results\n")
                output_file.write("-------------------------\n")
                output_file.write(f"Total Votes: {total_votes}\n")
                output_file.write("-------------------------\n")
                for candidate, votes in candidates.items():
                    percentage = (votes / total_votes) * 100
                    output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
                output_file.write("-------------------------\n")
                output_file.write(f"Winner: {winner}\n")
                output_file.write("-------------------------\n")

        else:
            print("Error: The file does not contain a header.")
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

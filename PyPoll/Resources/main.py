# Import os Module
import os

# Import csv for reading csv file
import csv

# Difining Variables
vote_count = 0
candidate_dict = {}

# Define resources path 
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# Reading csv file
with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

# Skipping header    
    header = next(csv_reader)

# For Loop 
    for row in csv_reader:

# Counts total vote counts
        vote_count += 1

# Get() method to return the values in dict
        candidate_dict[row[2]] = candidate_dict.get(row[2], 0) + 1

# Get() method to determine winner by finding the max value in dict
        winner = max(candidate_dict, key=candidate_dict.get)
        
print()
print(f'  Election Results')
print(f'  ----------------------------')
print(f'  Total Votes: {vote_count}')
print(f'  ----------------------------')

for candidate, vote in candidate_dict.items():

# Prints Candidates, votes divided by total votes x 100 using the format specifier % and total votes
    print(f'  {candidate}: {vote / vote_count * 100:.3f}% ({vote})')
        
print(f'  ----------------------------')
print(f'  Winner: {winner}')
print(f'  ----------------------------')


# Export a text.file and print PyBank results
output_path = "../analysis/PyPoll_Results.txt" 
with open(output_path, "w") as text_file: 
    text_file.write(" Election Results") 
    text_file.write("\n") 
    text_file.write(" ------------------------") 
    text_file.write("\n") 
    text_file.write(f" Total Votes: {vote_count}") 
    text_file.write("\n") 
    text_file.write(" ------------------------")
    text_file.write("\n") 
    for candidate, vote in candidate_dict.items():
        text_file.write(f" {candidate}: {vote / vote_count * 100:.3f}% ({vote})")
        text_file.write("\n")  
    text_file.write(" ------------------------")
    text_file.write("\n") 
    text_file.write(f" Winner: {winner}")
    text_file.write("\n")
    text_file.write(" ------------------------")
    text_file.write("\n")

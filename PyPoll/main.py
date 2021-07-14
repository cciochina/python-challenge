import os
import csv
from collections import Counter

poll_csv = os.path.join(".", "Resources", "election_data.csv")
total_votes = 0
candidates = None
total_candidates = []
total_count = []
winner = ""
dash_line = "--------------------"
total_results = ["Election Results ",
                 dash_line,
                 f"Total Votes: {total_votes}",
                 dash_line]
with open (poll_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    csv_header = next(csv_file)
    for row in csv_reader:
        total_votes +=1 
        total_candidates.append(row[2])
    max_percent = 0
    candidates = Counter(total_candidates)   
    for names,values in candidates.items():
        percent = (values/total_votes)*100
        if percent > max_percent:
            max_percent = percent
            winner = names
            
        result = f"{names}: {percent:.3f}% ({values})"
        total_results.append(result)
total_results.append(dash_line)
total_results.append(f"Winner: {winner}")        
total_results.append(dash_line)  

def terminal_print():
    for line in total_results:
        print(line)

terminal_print()
    
def write_analysis():    
    poll_analysis = os.path.join(".", "analysis", "analysis.txt")        
    with open (poll_analysis, "w") as txt_file:
        for line in total_results:
            txt_file.write(line + "\n")
write_analysis()   
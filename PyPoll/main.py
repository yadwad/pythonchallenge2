import os
from collections import Counter

csvpath = os.path.join("PyPoll", "election_data.csv") 

import csv
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None)

    voterid = []
    county = []
    candidates = []
    
    for hold in csvreader:
        voterid.append(hold[0])
        county.append(hold[1])
        candidates.append(hold[2])
    
    candidate_set = set(candidates)    
    total_vote = len(voterid)
    cnt = Counter(candidates)

    candidate_names = []
    
    for row in candidate_set:  
        candidate_names.append(row)

    print("Election Results")
    print("----------------------------------------")
    print(f"Total votes {total_vote}")
    print("----------------------------------------")

    candidate_count = 0
    for row in candidate_names:
        candidate_name = str(candidate_names[candidate_count])
        votes = candidates.count(candidate_name)
        votes = int(votes)
        percentage = round(votes / total_vote * 100, 2)
        dictionary_can.update({ candidate_name : votes})
        print(f"{candidate_name}: {percentage}%  ({votes} votes)" )
        candidate_count = candidate_count + 1


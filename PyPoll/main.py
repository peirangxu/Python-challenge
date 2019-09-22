import csv

with open("/Users/peirangxu/Desktop/Python-challenge/PyPoll/election_data.csv", 
          newline = "") as csvfile2:
    csvreader2 = csv.reader(csvfile2, delimiter=",")
    next(csvreader2)
    
    #create empty dictionary/list and set up counter
    total_votes = 0
    candidates = {}
    voter_percentage = []
    
    for row in csvreader2:
        total_votes = total_votes + 1
        
        if row[2] not in candidates.keys():
            candidates[row[2]]=0
        candidates[row[2]]=candidates[row[2]]+1  #count total votes for each candidate
        
    print(total_votes)  #total votes casted

#Write results in txt file
with open("/Users/peirangxu/Desktop/Python-challenge/PyPoll/Election_Results_Summary.txt","w") as text:
    text.write("Election Results \n")
    text.write("--------------------------\n")
    text.write("Total Votes:" + str(total_votes) + "\n")
    text.write("---------------------------\n")
    
    winning_count = 0  #Initial value for winning_count
    for i,j in candidates.items():
        if j > winning_count:
            winning_count = j
            winner_candidate = i #winner candidate corresponding to winning_count
            text.write(f'winner:{winner_candidate} {winning_count} votes \n')
            text.write("------------------------\n")
        votes = float(j)
        votes_percentage = votes/total_votes * 100  #percentage of votes got for each candidate
        text.write(f'{i}:{round(votes_percentage, 3)} % ({votes}) \n')
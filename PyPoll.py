import csv
import os
#Assign a variable to load a file from a path
file_to_load=os.path.join("Resources","election_results.csv")
#Assign a variable to save the file to a path
file_to_save=os.path.join("analysis","election_analysis.txt")

#Create accumulator variable and set it to 0
total_votes=0
#Create candidate list
candidate_options=[]
#Create dictionary to hold candidate name and votes
candidate_votes={}
#Winning candidate and winning count tracker
winning_candidate=""
winning_count=0
winning_percentage=0

#Open the results and read the file
with open(file_to_load,"r") as election_data:
    #To do: perform analysis
    file_reader=csv.reader(election_data)
    #Read and print the header row
    headers=next(election_data)
    print(headers)

    #Loop through all the rows
    for row in file_reader:
        #Add to the total vote count
        total_votes+=1
        #Get the candidate name
        candidate_name=row[2]
        #Check if the candidate is nos registered
        if candidate_name not in candidate_options:
            #add its name to the list
            candidate_options.append(candidate_name)
            #Beggin tracking the candidate´s vote count
            candidate_votes[candidate_name]=0
        #Add a vote to that candidate´s count
        candidate_votes[candidate_name]+=1
        #Save the results to a txt file
    with open(file_to_save,"w") as txt_file:
        election_results=(
            f"\nElection Results\n"
            f"---------------------\n"
            f"Total Votes:{total_votes:,}\n"
            f"---------------------\n")
        print(election_results,end="")
        #Save the final vote count to the txt file
        txt_file.write(election_results)
        #Iterate through the candidate list
        for candidate_name in candidate_options:
            #Get the votes of that candidate
            votes=candidate_votes[candidate_name]
            #Calculate the % of that candidate votes
            pvotes=float(votes) / float(total_votes) * 100
            #Print the candidates votes %
            candidate_results=f"{candidate_name}:{round(pvotes,1)}% ({votes:,})\n"
            print(candidate_results)
            #Add the candidate results to the txt file
            txt_file.write(candidate_results)

            #Check if the candidate has the greatest ammount of votes and %
            if (votes>winning_count) and (pvotes>winning_percentage):
                #Set his votes as the winning votes
                winning_count=votes
                #Set his % as the winning %
                winning_percentage=pvotes
                #Set the candidate as the current winning candidate
                winning_candidate=candidate_name
        winning_candidate_summary=(
            f"---------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"---------------------------\n")
        #Print the winning message
        print(winning_candidate_summary)
        #Add the winning message to the txt_file
        txt_file.write(winning_candidate_summary)
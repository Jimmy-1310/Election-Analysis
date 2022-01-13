# Election-Analysis
## Overview of the Project

In this project I was charged with calculating the results of the elections for U.S. Congressional precinct in Colorado. A python code was created to certify and calculate the results. This code calculated the total votes cast, the total votes each candidate got, and the percentage of the total votes they obtained. Additionally, an improvement was made to the code in which it also calculated the ammount of votes each county casted. With this we were able to output the calculations in a text file, making them easier to read and identify wathever data we were looking for. The data was given in a .csv file in which each row was an individual vote. This code can be used to analyze other elections, but it might need some changes. Some recommendations were added in order for it to work on other elections.

For this project, the skills that were developed and used weere opening and reading .csv files with python code, making calculations with the data obtained through the file and then outputting the calculations in a text file. I also implemented some critical thinking in order to identify opportunities to make the code usable in other elections. 


## Election-Audit Results.

- Total Votes Cast

Each row in the .csv was an individual vote. The method to get the total ammount was to get the total ammount of rows. The problem was is that we need to skip the first row because it is the header row, so it does not contain a vote.  The code that calculates this loops through all the rows and each time it loops, it adds 1 to a variable that holds the total ammount of votes. The code that does this is:

![Total_votes_ss](https://user-images.githubusercontent.com/95836718/149398267-ba11d66c-c8ef-4eb9-997e-0dd8efc15814.png)

**Comments**: The total_votes variable was created before with *total_votes=0*. the *reader* variable contains the piece of code *reader=csv.reader(election_data)* which reads the csv file.

The results were:

![Total_votes_results](https://user-images.githubusercontent.com/95836718/149400270-9548ff2f-da06-4e1e-bf40-f393d31650a7.png)

- County Statistics 

To calculate the total ammount of votes each county casted can be calculated by adding some lines of code to the previous *for-loop*. Each time we iterate through a row, we can take out the county where it was casted with *county_name=row[1]* (Because the county is the second element in the row, we get this value out by specifing the index inside the brackets) After this we need to check if we have already registered the county in our county list, if not we need to add it to the list. After this we can add the value to a key in a dictionarie that increments by 1. Once we had this information, to calculate the percentage of votes the code devides this number by the total ammount of votes and multiplies it by 100. The code that does this is: 

 ![County_stats_ss](https://user-images.githubusercontent.com/95836718/149398398-534a81dc-c6a6-4f21-99d7-330fd5d0e2f0.png)

**Comments**: *county_options* is a list that was created to autommaticaly identify the counties that were present, instead of adding them by hand. *County_votes* is a dictionary in which the key is the county name and the value was the ammount each county casted. *County_name* was the variable that contained the name of the county by the line of code: *County_name=row[1]* 

The results were:

![County_stats_results](https://user-images.githubusercontent.com/95836718/149398438-fcec6b16-6065-40dd-84f8-529d894842fb.png)

- County with largest ammount of votes

To calculate this I needed to create an *if-statement* that compared each ammount of votes and determined the largest. The if-statement was:

![Largest_county_ss](https://user-images.githubusercontent.com/95836718/149398501-5e2797d5-20b2-486d-87c1-b4e93fc16ca2.png)

**Comments** The variables votes and pvotes contain the ammount of votes and the percentage of votes. At first, the variables *larges_count* and *largest_percentage* were created to hold 0. The variable *largest_county* was created as an empty string with =""

The county with the largest turnout was:

![Largest_county_results](https://user-images.githubusercontent.com/95836718/149398532-5d6cea98-feee-47d5-a397-34905f884b56.png)

- Candidate Statistics

The logic behind getting the ammount of votes of each candidate is pretty much the same as getting the ammount for the counties. So what I did was to copy the structure of that piece code, and changed the variables in order to match candidate names.

![Candidate_statistics_ss](https://user-images.githubusercontent.com/95836718/149398598-9c07e5ce-a195-49d0-977b-e69b49c2479a.png)

**Comments**: The candidates name for which that vote was casted for, is the 3rd value in each row with index 3. To get this value I used *candidate_name=row[2]*

The results for each candidate votes and percentage was:

![Candidate_statistics_results](https://user-images.githubusercontent.com/95836718/149416513-909dd032-55c8-4656-b10a-8a64a5c5b231.png)

- Election winner

For getting the election winner, the same structure for getting the county with the most ammount of vote cast was applied. The main difference with this is that now the code also writes the percentage and total votes they had to win the election.

![Winner_ss](https://user-images.githubusercontent.com/95836718/149398659-bdc37733-132b-4a4e-8f2e-21e4442ddfaa.png)

The winner of the election and her stats was:

![Winner_results](https://user-images.githubusercontent.com/95836718/149398684-2db711f3-116b-4a33-a80a-f1f9906fa912.png)

## Election-Audit Summary
This code makes the job of autting the elections pretty easy. The automatization makes a job that could take hours only take a few seconds. The logical step is to use it in other elections as well. To this, some modifications are needed. For an election of the senate, we need to also take into account the party that each candidate represents. In a state senate election, multiple districts need to be calculated. We can devide the votes by distric and calculate the winner of each distric. To do this we can create another dictionary in which the key is the county and the value is the winning candidate.  Then we can count and calculate how many senatorial seats will each party have. An if-statement can be use to determine which party the candidate was in, after that we add 1 to a variable that store the ammounts of seats a party has. 
Another improvement to the code is a why to identify duplicated ballots. First we need to create a list that will store the ballots ID. Inside the for-loop that runs through all the rows we can add an if statement to check if the ID of that row is in the list, if not we can add it. If the ID is in the list we skip that block of code and add a 1 to variable that holds the ammount of duplicated ballots it had. Once we have this information, we can print it and see if there were any duplicated ballots.

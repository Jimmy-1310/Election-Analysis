# Election-Analysis
## Overview of the Project

In this project I was charged with calculating the results of the elections for U.S. Congressional precinct in Colorado. A python code was created to certify and calculate the results. This code calculated the total votes cast, the total votes each candidate got, and the percentage of the total votes they obtained. Additionally, an improvement was made to the code in which it also calculated the ammount of votes each county casted. With this we were able to output the calculations in a text file, making them easier to read and identify wathever data we were looking for. The data was given in a .csv file in which each row was an individual vote. This code can be used to analyze other elections, but it might need some changes. Some recommendations were added in order for it to work on other elections.

For this project, the skills that were developed and used weere opening and reading .csv files with python code, making calculations with the data obtained through the file and then outputting the calculations in a text file. I also implemented some critical thinking in order to identify opportunities to make the code usable in other elections. 


## Election-Audit Results.

### Total Votes Cast

Each row in the .csv was an individual vote. The method to get the total ammount was to get the total ammount of rows. The problem was is that we need to skip the first row because it is the header row, so it does not contain a vote.  The code that calculates this loops through all the rows and each time it loops, it adds 1 to a variable that holds the total ammount of votes. The code that does this is:

**Add photo of code**

**Comments**: The total_votes variable was created before with *total_votes=0*. the *reader* variable contains the piece of code *reader=csv.reader(election_data)* which reads the csv file.
The results were:

**Add photo of results**

### County Statistics 

To calculate the total ammount of votes each county casted can be calculated by adding some lines of code to the previous *for-loop*. Each time we iterate through a row, we can take out the county where it was casted with *county_name=row[1]* (Because the county is the second element in the row, we get this value out by specifing the index inside the brackets) After this we need to check if we have already registered the county in our county list, if not we need to add it to the list. After this we can add the value to a key in a dictionarie that increments by 1. Once we had this information, to calculate the percentage of votes the code devides this number by the total ammount of votes and multiplies it by 100. The code that does this is: 

**Add photto of code**

**Comments**: *county_options* is a list that was created to autommaticaly identify the counties that were present, instead of adding them by hand. *County_votes* is a dictionary in which the key is the county name and the value was the ammount each county casted. *County_name* was the variable that contained the name of the county by the line of code: *County_name=row[1]* 
The results were:

**Add photo of results**

### County with largest ammount of votes

To calculate this I needed to create an *if-statement* that compared each ammount of votes and determined the largest. The if-statement was:

**add image of code**

**Comments** At first, the variables *larges_count* and *largest_percentage* were created to hold 0. The variable *largest_county* was created as an empty string with =""

The county with the largest turnout was:

**Add image of results** 

### Candidate Statistics

The logic behind getting the ammount of votes of each candidate is pretty much the same as getting the ammount for the counties. So what I did was to copy the structure of that piece code, and changed the variables in order to match candidate names.

!**Add image of code** 

**Comments**: The candidates name for which that vote was casted for, is the 3rd value in each row with index 3. To get this value I used *candidate_name=row[2]*

The results for each candidate votes and percentage was:

**Add image of results**

### Election winner

For getting the election winner, the same structure for getting the county with the most ammount of vote cast was applied. The main difference with this is that now the code also writes the percentage and total votes they had to win the election.

**Add image of code**

The winner of the election and her stats was:

**add image of code**

**Comments**: 

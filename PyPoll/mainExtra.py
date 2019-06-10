# PyPoll project

# input file has over three million rows of data
# each row has voter ID, county,
# and candidate they voted for

# import os module, which will
# allow us to create file paths
# across operating systems
import os

# import csv module for reading CSV files
import csv

# create path to csv file
csvpath = os.path.join('election_data.csv')

# to read using CSV module
with open(csvpath, newline='') as csvfile:

   # create CSV reader, speciofying variable
   # to hold contents and delimiter
   csvreader = csv.reader(csvfile, delimiter=',')

   # print for testing purposes
   print(csvreader)

   # Read the header row first
   csv_header = next(csvreader)
   print(f"CSV Header: {csv_header}")

   # initialize variables
   count = 0
   tot_by_cand = dict()  
   tot_by_cand_cty = dict()  

   # Read each row of data after the header
   for row in csvreader:

   #'summarize in dictionasry with candidate key
      # calculations for esvh row
      count += 1
      cand = row[2]

      # extra - create second dictionary
      tot_by_cand[cand] = tot_by_cand.get(cand,0) + 1

      # extra - also summarize in dictionasry
      # with 2-tuple candidate-county key 
      county = row[1]
      myKey = (cand, county)
      tot_by_cand_cty[myKey] = tot_by_cand_cty.get(myKey,0) + 1

# create list with lines of output 
candList = list(tot_by_cand.keys())
numCand = len(candList)
output = list()
output.append("Election Results")
output.append("------------------")
output.append("Total Votes  " + str(count))
output.append("------------------")
winCand = ""
winVotes = 0
for cand in candList:
   numVotes = tot_by_cand[cand]
   votePercent = round(100 * numVotes / count,3)
   output.append(cand + ":  " + str(votePercent) + "% (" + str(numVotes) + ")")
   if (numVotes > winVotes):
      winVotes = numVotes
      winCand = cand
output.append("------------------")
output.append("Winner:  " + winCand)
output.append("------------------")
   
# print each line of text
for out in output:
   print(out)

# outtput to text file
outputFile = open("output.txt","w")
for out in output:
   outputFile.write(out + "\n")

# extra - print second dictionary
print(tot_by_cand_cty)

# rest of code below is extra

# output csv file with second dictionary
listKeys = list(tot_by_cand_cty.keys())

# Specify the file to write to
output_path = os.path.join("outputExtra.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

   # Initialize csv.writer
   csvwriter = csv.writer(csvfile, delimiter=',')

   # Write the first row (column headers)
   csvwriter.writerow(["candidate","county","votes"])

   # Write the second row
   for key in listKeys:
      csvwriter.writerow([key[0], key[1],
      tot_by_cand_cty[key]])

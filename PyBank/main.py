# PyBank project

# input file has 87 rows of data
# with profit or loss for January 2010 
# through Febuary 2017
# each row has month-year key (ex, "Jam-10")
# and profit(+) or loss (-)

# import os module, which will
# allow us to create file paths
# across operating systems
import os

# import csv module for reading CSV files
import csv

# create path 6o csv file
csvpath = os.path.join('budget_data.csv')

# to read using CSV module
with open(csvpath, newline='') as csvfile:

   # create CSV reader, specifying variable
   # to hold contents and delimiter
   csvreader = csv.reader(csvfile, delimiter=',')

   # print for testing purposes
   print(csvreader)

   # read header row first
   csv_header = next(csvreader)
   print(f"CSV Header: {csv_header}")

   # initialize some variAbles
   count = 0
   totProf = 0
   totLoss = 0
   maxProf = 0
   maxProfDate = " "
   maxLoss = 0
   maxLossDate = " "

   # Read each row of data after the header
   for row in csvreader:

      # calculations for esvh row
      count += 1
      prof = int(row[1])
      if (prof > 0):
         totProf += prof
      else:
         totLoss += prof
      if (count == 0):
         maxProfDate = row[0]
         maxProf = prof 
         maxLossDate = row[0]
         maxLoss = prof
      elif (prof > maxProf):
         maxProfDate = row[0]
         maxProf = prof 
      elif (prof < maxLoss):
         maxLossDate = row[0]
         maxLoss = prof 
        
# create list with lines of output 
output = [ "", "", "", "", "", "", ""]
output[0] = "Financial Analysis"
output[1] = "------------------"
output[2] = "Total Months:  " + str(count)
tot = totProf + totLoss
output[3] = "Total:  $" + str(tot)
output[4] = "Average Change:  $" +  str(round(tot / count,2))
output[5] = "Greatest Increase in Profits:  " + maxProfDate + " ($" + str(maxProf) + ")"
output[6] = "Greatest Decrease in Profits:  " + maxLossDate + " ($" + str(maxLoss) + ")"

# print each line of text
for out in output:
   print(out)

# outtput to text file
outputFile = open("output.txt","w")
for out in output:
   outputFile.write(out + "\n")

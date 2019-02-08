# Filename:  main.py    PYBOSS challenge
# EXTRA ASSIGNMENT
# Used to analyze Tuna 2.0 ddevelopment as the Boss
# Eric Staveley   MWSa

# import the os module...to create file paths across operating systems
import os

# Module for reading CSV files
import csv

#csv file will be in Resources dir at our script level
csvpath = os.path.join('.', 'employee_data.csv')

'''
The dataset is composed of five columns: 
Emp ID,Name,DOB,SSN,State
214,Sarah Simpson,1985-12-04,282-01-8166,Florida

#import this file and convert and export the data to this format:
Emp ID,First Name,Last Name,DOB,SSN,State
214,Sarah,Simpson,12/04/1985,***-**-8166,FL

'''

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        EmployeeID = row[0]
        FullName = row[1]
        DOB = row[2]
        SSN = row[3]
        State = row[4]

        #split up FullName to first and last name per the output request
        TempSplit =  FullName.split(" ")
        FirstName = TempSplit[0]
        LastName = TempSplit[1]

        #convert date format from 1985-12-04  to  12/04/1985
        TempSplit = DOB.split("-")
        NewDOB = TempSplit[1] + "/" + TempSplit[2] + "/" + TempSplit[0]

        #The SSN data should be re-written such that the first five numbers are hidden from view.
        # ie 282-01-8166 to ***-**-8166
        TempSplit = SSN.split(-)
        NewSSN = "***-**-" + TempSplit[2]

        # rewrite the state data as a two digit abbreviation:  rec using a dictionary at
        # https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5

        us_state_abbrev = {
            'Alabama': 'AL',
            'Alaska': 'AK',
            'Arizona': 'AZ',
            'Arkansas': 'AR',
            'California': 'CA',
            'Colorado': 'CO',
            'Connecticut': 'CT',
            'Delaware': 'DE',
            'Florida': 'FL',
            'Georgia': 'GA',
            'Hawaii': 'HI',
            'Idaho': 'ID',
            'Illinois': 'IL',
            'Indiana': 'IN',
            'Iowa': 'IA',
            'Kansas': 'KS',
            'Kentucky': 'KY',
            'Louisiana': 'LA',
            'Maine': 'ME',
            'Maryland': 'MD',
            'Massachusetts': 'MA',
            'Michigan': 'MI',
            'Minnesota': 'MN',
            'Mississippi': 'MS',
            'Missouri': 'MO',
            'Montana': 'MT',
            'Nebraska': 'NE',
            'Nevada': 'NV',
            'New Hampshire': 'NH',
            'New Jersey': 'NJ',
            'New Mexico': 'NM',
            'New York': 'NY',
            'North Carolina': 'NC',
            'North Dakota': 'ND',
            'Ohio': 'OH',
            'Oklahoma': 'OK',
            'Oregon': 'OR',
            'Pennsylvania': 'PA',
            'Rhode Island': 'RI',
            'South Carolina': 'SC',
            'South Dakota': 'SD',
            'Tennessee': 'TN',
            'Texas': 'TX',
            'Utah': 'UT',
            'Vermont': 'VT',
            'Virginia': 'VA',
            'Washington': 'WA',
            'West Virginia': 'WV',
            'Wisconsin': 'WI',
            'Wyoming': 'WY',
        }

        #loop through this dictionary to find the long state name and retrieve the abbreviation value pair

        fav_numbers = {'eric': 17, 'ever': 4}
        for long_state_name, abbrev in us_state_abbrev.items():    #loop thru the dict tp find the long state name match
            if state = long_state_name:   #when the given state name matches the dict long state name
                state_abbrev = abbrev   # assign that state's abbrvaition to our abbreviation variable
                break   #break out of the loop, we found the state
        for name, number in fav_numbers.items(): print(name + ' loves ' + str(number))


                
        
        

print("\nFinancial Analysis") 
print("-----------------------") 
print("Total Months: " + str(i))
print("Total: $" + str(sumPandL))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + str(max_pos_change_month) + " ($" + str(max_pos_change) + ")")
print("Greatest Decrease in Profits: " + str(max_neg_change_month) + " ($" + str(max_neg_change) + ")")
print("")
foutname = "fin_analysis_budget_data.txt"
print("Printing this financial analysis to: " + str(os.getcwd()) + "/" + foutname)

#write the Financial Analysis to a file, a text file, not a csv file
with open(foutname, 'w') as file_object:
    file_object.write("Financial Analysis\n")
with open(foutname, 'a') as file_object:
    file_object.write("-----------------------\n")
    file_object.write("Total Months: " + str(i) + "\n")
    file_object.write("Total: $" + str(sumPandL) + "\n")
    file_object.write("Average Change: $" + str(average_change) + "\n")
    file_object.write("Greatest Increase in Profits: " + str(max_pos_change_month) + " ($" + str(max_pos_change) + ")\n")
    file_object.write("Greatest Decrease in Profits: " + str(max_neg_change_month) + " ($" + str(max_neg_change) + ")\n")
    file_object.write("\n")
print("\nFinished!")   
        
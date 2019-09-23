import datetime

with open("/Users/peirangxu/Desktop/Python-challenge/PyBoss/employee_data.csv", 
          newline = "") as csvfile3:
    csvreader3 = csv.reader(csvfile3, delimiter=",")
    next(csvreader3)
    
    Emp_ID = []
    first_name = []
    last_name = []
    DOB =[]
    States = []
    SSN_final = []
    for row in csvreader3:
        Emp_ID.append(row[0]) #Extract emp id
        
        # Split names and store first and last name in seperate lists
        name = row[1].split(" ")
        first_name.append(name[0])
        last_name.append(name[1])
        
    #Change the format of DOB and put in a list
        date = datetime.datetime.strptime(row[2], '%Y-%m-%d').strftime('%m/%d/%y')
        DOB.append(date)
        
    #State abbrev.
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
        States.append(us_state_abbrev[row[4]])
        
        #Change the format of SSN
        SSN= list(row[3])
        SSN[0:3]=("*","*","*")
        SSN[4:6]=("*","*")
        join_SSN = "".join(SSN)
        SSN_final.append(join_SSN)   

#Write a new csv file
emd = zip(Emp_ID,first_name,last_name,DOB,SSN_final,States)
with open("/Users/peirangxu/Desktop/Python-challenge/PyBoss/employee_data_Adjusted.csv", 
          "w",newline = "") as csvfile3:
    csvwriter3 = csv.writer(csvfile3, delimiter=",")
    csvwriter3.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN","State"])
    csvwriter3.writerows(emd)
    
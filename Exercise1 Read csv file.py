# Exercise 1
"""
1/Create csv file(Name, Id, GPA)
2/Read the csv file in python
3/Store the GPA in list ---> variable GPA = [ ]
4/Calculate the average of GPA from the list
5/Read the information of new-student---> input from user Name, Id, GPA
6/Insert new GPA in 3rd place in the list
"""

#import the csv module.
import csv

#Read the CSV file and store GPA in a list:
GPA = []
with open('GPA_csvFile.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        GPA.append(float(row['GPA']))

print("the GPA list : ",GPA)

# Calculate the average GPA:
average_gpa = sum(GPA) / len(GPA)
print("Average GPA:", average_gpa)

# Read information of a new student, ask ti input:
new_name = input("Enter the new student's name: ")
new_id = int(input("Enter the new student's ID: "))
new_gpa = float(input("Enter the new student's GPA: "))

# Insert the new GPA in the 3rd place in the list:
GPA.insert(2, new_gpa)
print("Updated GPA list:", GPA)


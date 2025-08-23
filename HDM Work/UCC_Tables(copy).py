# -*- coding: utf-8 -*-
"""Spyder Editor


This is a temporary script file.
"""
#This script helps distributes the amount of work for the team. It even allows comparison between an old excel file and a new excel file to determine 
#if deal are repeated or not.
import sys
from datetime import date
import os
import pandas as pd
import numpy as np
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
Today = date.today().isoformat()
# Open dialog
# Show all columns
pd.set_option("display.max_columns", None)

# Optional: also show all rows if needed
pd.set_option("display.max_rows", None)

# Optional: widen the column display
pd.set_option("display.width", 1000)

# Open dialog
print("Selecciona los documentos de excel que vas a comparar. El primero debe ser el más reciente y el segundo la lista anterior")
path1 = askopenfilename(title="Select a file", filetypes=[("Excel files", "*.xlsx *.xls")])
path2 = askopenfilename(title="Select a file", filetypes=[("Excel files", "*.xlsx *.xls")])
# Show result
New_UCC= pd.read_excel(path1)
old_ucc= pd.read_excel(path2)
old_ucc.columns = old_ucc.columns.str.strip()
New_UCC.columns = New_UCC.columns.str.strip()
New_UCC= New_UCC.sort_values(by='Deal Name', ascending=True)
old_ucc= old_ucc.sort_values(by='Deal Name', ascending=True)
pd.set_option("display.max_columns", None)

print("First column is deal names, second is UCC Filing status from the latest list and the third column is from the oldest list")
#This works because "inner"looks for instances which are  in both dataframes and nothing more.
#New_UCC= left & old_ucc=right. Use the suffixes to avoid any clash between the two columns since they are named the same.
Repeated_Deals =New_UCC.merge(old_ucc, on='Deal Name', suffixes=("_new","_old"),how="inner")[['Deal Name', 'UCC Filed_new', 'UCC Filed_old']]
new_deals = set(New_UCC['Deal Name'])
old_deals = set(old_ucc['Deal Name'])
intersection = new_deals.intersection(old_deals)
print(f"Deals in both lists: {len(intersection)}")
print(Repeated_Deals)
mask = New_UCC['Deal Name'].isin(Repeated_Deals['Deal Name'])
print("The previous list will be dropped from the latest excel file since they are dups.")
New_UCC = New_UCC.loc[~mask]
New_UCC.reset_index(drop=True, inplace=True)
print(New_UCC)
while True:
    try:
        # Ask the user for input
        choice = int(input("Type 1 to distribute evenly, or 2 for a specific amount: "))
        
        # Check if the input is 1 or 2
        if choice in [1, 2]:
            break  # Valid input, exit the loop
        else:
            # If the number isn’t 1 or 2, prompt again
            print("Please enter either 1 or 2.")
    
    except ValueError:
        # If they typed something that isn’t a number, handle the error
        print("That wasn't a number. Please enter 1 or 2.")
# After the loop, 'choice' will be guaranteed to be 1 or 2
names_list=[]
i=0
counter=0

if choice == 1:
    #lets ask the user how many persons wil be working with the list
    number_of_employees= int(input("How many employees will be working? "))
    while i < number_of_employees:
        name = input("\nType the name of the person: ")
        names_list.append(name) #this appends the name to the list.   
        i += 1
    names= names_list
    names_list= np.array_split(New_UCC, number_of_employees) #this is now a dataframe, each containing an even amount of rows
    #from the dataframe New_UCC
    print("Select the directory that will later be used to save your excel files: ")
    Directory = askdirectory(title="Select export folder: ")
    print(Directory)
    for person,chunk in zip(names, names_list): #use zip() to iterate over the items separetely. 
    #This avoids conflicts with the iterations.
        file_destination= os.path.join(Directory, f"{person}_UCC_{Today}.xlsx")
        chunk.to_excel(file_destination, index=False)
else:
    print("Select the directory that will later be used to save your excel files: ") #folder where the excel files will be stored
    Directory = askdirectory(title="Select export folder: ")
    try: 
        number_of_employees= int(input("How many employees will be working? "))
    except ValueError:
        print("\n Try again, an error ocurred. Please type in a whole number") #check if they typed other things.
    while True: 
        try:
            print("\nPlease type the specific amount of rows for each excel, example: 100, 150, 200... ")
            rows_per_person= int(input("\nType here:"))
            if rows_per_person>0:
                break
        except ValueError: #checks if the rows per person is greater than zero and not a float number
                print("\n Try again, an error ocurred. Please type in a whole number")
    while i < number_of_employees:
        name = input("\nType the name of the person: ")
        names_list.append(name) #this appends the name to the list.   
        i += 1
    for name in names_list: #loops over the names within the list of names
        while True:
            if New_UCC.empty: 
                break
            remaining = min(rows_per_person, len(New_UCC))
            chunk = New_UCC.iloc[0:remaining]
            print(chunk.head())
            confirm = input(f"\nIs the result correct? {name}'s Excel will have {len(chunk)} rows. Type y/yes/n/no to continue: ").lower().strip()
            if confirm== "no" or confirm== "n" :
                print("Aborting distribution. No files saved.")
                sys.exit()
            New_UCC = New_UCC.drop(index=range(0, len(chunk))) #drops from 0 to rows_per_person
            New_UCC.reset_index(drop=True, inplace=True) #resets index to continue with the next person
            file_destination= os.path.join(Directory, f"{name}_UCC_{Today}.xlsx") #creates the path for the new files
            chunk.to_excel(file_destination, index=False) #creating the excel files
remainder_path = os.path.join(Directory, "Remainder_uccs.xlsx")    #what is left to not overwrite the original excel
New_UCC.to_excel( remainder_path,index=False) #the final excel containing the remaining deal names.
                
    #3-select the destination where the files will go.
    #4-Open a for loop. Iterate over the list to store a chunk of the dataframe and pass the name of the person to the 
    #Excel file that will be created
    #5-Open a while loop to make sure everything runs smooh inside the for loop. If the dataframe is not to the users 
    #liking, he can break out and run the program once again. Maybe they wanted a different distribution.
    #6-Use DF.iloc[0:rows_per_person] and store it in a DataFrame. Show the result in the screen
    #7-Ask if the result is ok and proceed with the next one. If not, break the loop and go back to line 82.
    #8If the answer was yes, continue, eliminate the n-rows from the original excel path o avoid conflict.
    #9-Start returning excel files one by one in the desired folder destination.
    #10-Finally, print to the screen that all excel files were created.
    #Congratulations, the process was completed!
    
    
            
        

        

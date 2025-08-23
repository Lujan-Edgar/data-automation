# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 16:01:49 2025

@author: Dell
"""
#This script takes a .txt and an excel file from UCC filing to automate the process of updating the excel. Deals that appear in the .txt are supposed to change their status from sent
#to done.
import pandas as pd
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
import sys
import os
pd.set_option("display.max_columns", None)

# Optional: also show all rows if needed
pd.set_option("display.max_rows", None)

# Optional: widen the column display
pd.set_option("display.width", 1000)
print("\nPlease select the excel file for the UCC automate process.")
path = askopenfilename(title="Select a file", filetypes=[("Excel files", "*.xlsx *.xls")])
print("\nNow Select the .txt file you wish to open that contains your deal names.")
List_path= askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt")])
print("\nFinally, select the folder where the files will show upon excuting the code.")
Directory= askdirectory(title="Select directory")
 
# just use read_excel from pd and it will make the work easier

UCC = pd.read_excel(path)
UCC = UCC.sort_values(by='Deal Name', ascending=True)  # If ascending=False, it's the same as typing 'descend' in MATLAB.
UCC_Deal = UCC.copy()  # Create a copy to ensure no overwriting.
 
deal_list = []  # create the deal name List to work with.

with open(List_path, "r+") as deals:
    deals.seek(0)
    for deal in deals:
        deal_list.append(deal.strip())  # do not set the result back to deal_list, it is incorrect syntax.

length = len(deal_list)

i = 0
not_found = []

for deal in deal_list:
    # if any(UCC_Deal.loc[UCC_Deal['Deal Name'] == deal]):
    # It "works" but not for the reason you might expect—it’s not truly checking “does at least one row match my condition,”
    # but rather “is there any truthy value in these columns,”
    # which just happens to align with your goal in this case.
    if not UCC_Deal.loc[UCC_Deal['Deal Name'] == deal].empty:  # This approach is more adequate since it actually follows my logic.
        UCC_Deal.loc[UCC_Deal['Deal Name'] == deal, 'UCC Filed'] = 'Done'
        i += 1
    else:
        not_found.append(deal)
if i != length:
    print("It appears that not all deals were found")
else:
    print("All deals were found")
UCC_Deal.to_excel(path, index=False) 
#Now that we are getting closer to the end, lets pass the information from UCC_Deal to the original excel.
# index=False prevents Pandas from writing an additional column containing the indexes.
# Don’t get scared if your excel format gets lost in the process. At this point, you are mostly just going to be uploading it.

output_path = os.path.join(Directory, "not_found.txt") #el resultado es la dirección de guardado de tu archivo.
#por ejemplo C:/Users/TuNombre/Documents/not_found.txt
not_found
not_found_deal = []
try: 
    with open(output_path, "x") as missing_list: #this will attempt to create a new file, if non exists, no issue will show.
        for name in not_found: 
            not_found_deal.append(f"{name}\n")
        missing_list.writelines(not_found_deal)
        print("\nMissing deals have been written to 'not_found.txt'")

except FileExistsError: #If the file is in your directory then this will execute. Please make sure to check the content of your file.
    print(f"\nThe file already exists. Make sure it has the right information. check in: {Directory}")
    choice = int(input("\nIs the content of the file correct? Type 1 for yes and 2 for no: "))
    if choice == 1: #by typing 1 you are saying that the existent file contains the correct information.
        sys.exit()
    else:
        with open(output_path, "w") as missing_list: #This will rewrite to the file.
            for name in not_found: 
                not_found_deal.append(f"{name}\n")
            missing_list.writelines(not_found_deal)
# Try looking first by the address and then continue with the name. Usually the address is fine.

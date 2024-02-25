#Renaming after checking whether it exists
import os

old_name = r"E:\demos\files\reports\details.txt"
new_name = r"E:\demos\files\reports\new_details.txt"

if os.path.isfile(new_name):
    print("File name already exists. Cannot rename")
else:
    os.rename(old_name, new_name)
    
#Rename Multiple Files 
import os

folder = r'E:\demos\files\reports\\'
count = 1

for file_name in os.listdir(folder)
    source = folder + file_name

    destination = folder + "sales_" + str(count) + ".txt"

    os.rename(source, destination)
    count += 1
print('All Files Renamed')

print('New Names are')
res = os.listdir(folder)
print(res)

#Renaming only a list of files in a folder
import os

files_to_rename = ['sales_1.txt', 'sales_4.txt']
folder = r"E:\demos\files\reports\\"

for file in os.listdir(folder):
    if file in files_to_rename:
        old_name = os.path.join(folder, file)
        
        only_name = os.path.splitext(file)[0]

        new_base = only_name + '_new' + '.txt'

        new_name = os.path.join(folder, new_base)
        
#Renaming files with a timestamp
import os
from datetime import datetime

# adding date-time to the file name
current_timestamp = datetime.today().strftime('%d-%b-%Y')
old_name = r"E:\demos\files\reports\sales.txt"
new_name = r"E:\demos\files\reports\sales" + current_timestamp + ".txt"
os.rename(old_name, new_name)

#Renaming the Extension of the Files
import os

folder = r"E:\demos\files\reports\\"
print('Before rename')
files = os.listdir(folder)
print(files)

for file_name in files:
    old_name = os.path.join(folder, file_name)

    new_name = old_name.replace('.txt', '.pdf')
    os.rename(old_name, new_name)

print('After rename')
print(os.listdir(folder))


        os.rename(old_name, new_name)

res = os.listdir(folder)
print(res)

#Renaming and then moving a file to a new location
import glob
import os

old_folder = r"E:\demos\files\reports\\"
new_folder = r"E:\demos\files\new_reports\\"

old_name = old_folder + "expense.txt"
new_name = new_folder + "expense.txt"


os.rename(old_name, new_name)
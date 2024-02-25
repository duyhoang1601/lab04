#write to a new file
text = "This is new content"
fp = open("write_demo.txt", 'w')
fp.write(text)
print('Done Writing')
fp.close()
fp = open("write_demo.txt", 'r')
print(fp.read())
fp.close()

#writing to an existing file
file_path = r"E:\demos\files\write_demo.txt"
fp = open(file_path, 'r')
print(fp.read())
fp.close()
fp = open(file_path, 'w')
fp.write("This is overwritten content")
fp.close()
fp = open(file_path, 'r')
print("Opening file again..")
print(fp.read())
fp.close()

#Write a list of lines to a file
person_data = ['Name: Duy', '\nAddress: 39 Phu Huu village', '\nCity: thac that']
fp = open("write_demo.txt", "w")
fp.writelines(person_data)
fp.close()
fp = open("write_demo.txt", "r")
print(fp.read())
fp.close()
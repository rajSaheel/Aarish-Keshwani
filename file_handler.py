'''
r-reading
w-writing
a-append
x-create new file
'''
file=open("content.txt","r")
content=file.readlines()
file.close()
file2=open("data.txt", "w")
file2.write("This is a new file created using python.\n")
file2.close()
file3=open("data.txt", "a")
file3.write("This file is edited using append mode.\n")
file3.writelines(["apple","cat","dog"])
file4=open("new_data.txt", "x")

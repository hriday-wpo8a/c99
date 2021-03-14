import os
import shutil

#take the input of the directory which needs to be sorted
path = input("enter the name of the directory to be sorted : ")

#to get list of files in the directory
list_of_files = os.listdir(path)

#go through eacch and every file in thast directory
for file in list_of_files: 
    name,ext=os.path.splitext(file)

    #this is going to store the extension type 
    ext=ext [1:]

    #this forces the next loop if it is a directory
    if ext=='':
        continue

    #move the file to the directory where the name 'ext ' already  exists
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)

    #creates a new directory if the directory doesnt exist
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)

from pathlib import Path #
import os 
# Path: Used to manage file and folder paths.
# os: Used to interact with the operating system, such as deleting files.

def readfielandfolder():
    path = Path('') #jis directory ke andr ho uska path mil ajyega 
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1}  : {items} ")
# def: Defines a function.
# Path(''): Represents the current directory.
# rglob('*'): Finds files and folders recursively.
# list(): Converts the results into a list.
# enumerate(): Provides an index and each item.
# print(): Displays numbered file and folder names.

def createfile():
    try:
        readfielandfolder()
        name = input("please tell your file name :- ")
        p = Path(name)
        if not p.exists():
            with open(p,"w") as fs:  #with automatically closes the file after the operation, even if an error occurs inside the block.
                data = input("what you want to write in this file :- ")
                fs.write(data)
            
            print(F"FILE CREATED SUCCESSFULLY")
        else:
            print("this file already exist")
        
    except Exception as err:
        print(f"An error occured as {err}")
# try: Runs code that might cause an error.
# readfielandfolder(): Displays existing files.
# input(): Takes the filename and content from the user.
# Path(name): Creates a path object.
# exists(): Checks whether the path exists.
# open(p, "w"): Opens a file in write mode or creates it.
# as fs: Stores the file object in fs.
# write(data): Writes content into the file.
# else: Runs if the path already exists.
# except: Handles errors.

def readfile():
    try:
        readfielandfolder()
        name = input("which file you want to read")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
            
            print("Readed successfully ")
        else:
            print("the file doesnot exist")
    except Exception as err:
        print(f"An error occured as {err}")
# input(): Takes the filename.
# exists(): Checks whether the path exists.
# is_file(): Checks whether the path is a file.
# "r": Opens the file in read mode.
# read(): Reads the entire file content.
# print(data): Displays the content.
# except: Handles errors.

def updatefile():
    try:
            
        readfielandfolder()
        name = input("tell which file you want to update :- ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing the name of your file :- ")
            print("press 2 for overwriting the data of your file ")
            print("press 3 for appending some content in your file ")

            res = int(input("tell your response :- "))

            if res == 1:
                name2 = input("tell  your new file name :- ")
                p2 = Path(name2)
                p.rename(p2)
            if res == 2:
                with open(p, 'w') as fs:
                    data = input("tell what you want to write this is overwrite the data :- ")
                    fs.write(data)
        
            if res == 3:
                with open(p, 'a') as fs:
                    data = input("tell what you want to append :- ")
                    fs.write(" "+data)

    except Exception as err:
        print(f"An error occured as {err}")


def deletefile():
    try:

        readfielandfolder()
        name = input("whuich file you want to delete :- ")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(name)
        
            print("file removes suiccessfully ")
    
        else:
            print("No such file exist")
    
    except Exception as err:
        print(f"An error occured as {err}")

# input(): Takes the filename.
# Path(name): Creates a path object.
# exists(): Checks whether the path exists.
# is_file(): Checks whether it is a file.
# os.remove(name): Deletes the file.
# except: Handles errors.  


print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deletion a file")

check = int(input("please tell your response :- "))

if check == 1:
    createfile()

if check == 2:
    readfile()

if check == 3:
    updatefile()

if check == 4:
    deletefile()
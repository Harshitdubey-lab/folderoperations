import os 
from pathlib import Path

def creatfolder():
    name = input("tell you folder nmae :- ")
    p=Path(name)
    if not p.exists():
        p.mkdir()
    else:
        print("folder name is alreay exist ")

def listingfolderandfiles():
    p= Path('')
    items = list(p.rglob('*'))
    for i,v in enumerate (items):
        print(f"{i+1}:{v}")

def updatefolder():
    listingfolderandfiles()
    oname = input("eneter the filr name = ")
    old_p = Path(oname)
    if old_p.exists():
        n_name = input("tell folder new name ")
        new_p = Path(n_name)
        if not new_p.exists():
            old_p.rename(new_p)
        else:
            print("folder already exist")
    else:
        print("no such folder exist")

def deletfolder():
    listingfolderandfiles()
    name = input("which folder you want to delet == ")
    p= Path(name)
    if p.exists():
        p.rmdir()
    else:
        print("no such folder exist")

def createfile():
    name = input("tell your file name with extension:-")
    p = Path(name)
    if not p.exists():
        with open(p,"w") as file:
            data = input("what you want to write inside:-")
            file.write(data)
            print("create successfully")
    else:
        print("this file already exist")


def readfile():
    listingfolderandfiles()
    name = input("which folder you want to read with extension :-")
    p=Path(name)
    if p.exists and p.is_file():
        with open(p,'r')as file:
            data = file.read()
            print(file.read())
        print("file read successful")
    else:
        print("no such file exist")


def updatefile():
    listingfolderandfiles()
    name = input("enter the which file do you want to update ")
    p =Path(name)
    if p.exists()and p.is_file():
        print("press 1 for creating a folder ")
        print("press 2 for listing files and folder ")
        print("press 3 upadting the folder ")
        check =int(input("tell your respond :- "))
        if check == 1:
            new_name = input("tell your new name :-")
            new_p = Path(new_name)
            if not new_p.exists():
                p.rename(new_p)
                print("name update successfully ")
            else:
                print("this name already exist ")
        if check ==2:
            with open(p,'w') as file:
                data = input("what you want to overwrite ")
                file.write(data)
                print("update succesfull")
        if check == 3:
            with open(p,'a') as file:
                data = input("what you want to append")
                file.write(""+data)
                print("update succesfull")
    else:
        print("no file exist")

def deletfile():
    listingfolderandfiles()
    name = input("which file you want to delet == ")
    p= Path(name)
    if p.exists() and p.is_file():
        os.remove(p)

        print("file delete succesfully")
    else:
        print("no such folder exist")


while True:

    print("press 1 for creating a folder ")
    print("press 2 for listing files and folder ")
    print("press 3 upadting the folder ")
    print("press 4 deleting the folder ")
    print("press 5 for creating the file  ")
    print("press 6 for reading a file ")
    print("press 7 for upadting the file  ")
    print("press 8 for deleting the file  ")
    print("press 0 to exit the application ")
    res =int(input("tell your response :- "))

    if res == 1:
        creatfolder()

    if res == 2:
        listingfolderandfiles()

    if res ==3:
        updatefolder()

    if res == 4:
        deletfolder()

    if res == 5:
        createfile()

    if res ==6:
        readfile()

    if res == 7:
        updatefile()

    if res == 8:
        deletfile()
    if res == 0:
        break
        







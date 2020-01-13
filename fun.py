import os
import shutil
from zipfile import ZipFile

def create_File(name):
    open(name,'w')

def create_Folder(name):
    os.mkdir(name)

def list_Directories():
    for a in os.listdir():
            print(a)

def list_Dir_Detials():
    os.system("dir")

def delete_file(name):
    os.remove(name)

def delete_dir(name):
    shutil.rmtree(name)

def rename_dir(name,new_name):
    os.rename(name,new_name)

def rename_file(name,new_name):
    os.rename(name,new_name)

def change_dir(path):
    os.chdir(path)

def current_dir():
    print(os.getcwd())

def open_file(name):
    f=open(name,mode="r")
    for i in f:
        print(i)

def edit_file(name):
    os.system("notepad "+name)

# def create_multiple_files(initial,increment):
#     temp = initial.split("-")
#     start = temp[0]
#     temp2 = temp[1].split(".")
#     last = temp2[1]
#     temp = increment.split("=")
#     inc=temp[1]
#     cmd='for /l %a in ('+start+inc+last+') do type nul > "%a.txt"'
#     os.system(cmd)

def move_file(source,destination):
    shutil.move(source,destination)

def check_exists(filename,path):
    flag=False
    for a in os.listdir():
            if(a==filename):
                flag=True

    if(flag==True):
        print(filename)
    elif(flag==False):
        print("file not found")

def copy_file(filename,path):
    shutil.copy(filename,path)

def copy_dir(dirname,path):
    shutil.copy(dirname,path)


def check_usage(path):
    print(shutil.disk_usage(path))

def extract_zip(name_of_archive):
    with ZipFile(name_of_archive, 'r') as zip:
        # printing all the contents of the zip file
        zip.printdir()

        # extracting all the files
        print('Extracting all the files now...')
        zip.extractall()
        print('Done!')


def make_zip(a,b,c,zipname):
    # create a ZipFile object
    zipObj = ZipFile(zipname, 'w')

    # Add multiple files to the zip
    zipObj.write(a)
    zipObj.write(b)
    zipObj.write(c)

    # close the Zip File
    zipObj.close()



def search_inside(target,filename):
    a = target
    count = 0
    flag = False
    f = open(filename, "r").read().split("\n")
    for i in f:
        count = count + 1
        v = i.split()

        if (a in i):
            flag = True
            break
        elif ((a in v)):
            flag == True
            break

    if flag == False:
        print("text not found")
    else:
        print("found at line ", count)



#def create_multiple_files_simple(initial):
 #   temp = initial.split("-")
  #  start = temp[0]
   # temp2 = temp[1].split(".")
    #last = temp2[1]
    #inc=1
    #cmd='for /l %a in (',start,inc,last,') do type nul > "%a.txt"'
    #os.system(str(cmd))

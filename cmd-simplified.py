import os
import fun
import helps
import time



print("""
-------------------------------------------------------------------------
                    WELCOME TO CMD-SIMPLIFIED         
-------------------------------------------------------------------------
COPYRIGHT(C) 2020 SHAIKH AQUIB
         """)
print("Loading...")
print("")



time.sleep(2)

print("ENTER ' help ' to see the command manual and 'exit' to exit program")

#for storing the initial working directory path
store=os.getcwd()


while(True):
        try:
            prompt = input(">> ")

            meaning = prompt.split()

# 1. file creation
            if (meaning[0] == 'cr'):
                if (meaning[1] == '-fi'):
                    if(len(meaning)>3):
                        for i in range(2,len(meaning)):
                            fun.create_File(meaning[i])
                    else:
                        fun.create_File(meaning[2])

                elif (meaning[1] == '-fo'):
                    if (len(meaning) > 3):
                        for i in range(2, len(meaning)):
                            fun.create_Folder(meaning[i])
                    else:
                        fun.create_Folder(meaning[2])
# 2. listing files and directories in current folder
            elif (meaning[0] == 'ls'):
                if(len(meaning)>1 and meaning[1]=='details'):
                    fun.list_Dir_Detials()
                else:
                    fun.list_Directories()

# 3. deleting files and directories
            elif (meaning[0] == 'delete'):
                if (meaning[1] == '-fi'):
                    if (len(meaning) > 3):
                        for i in range(2, len(meaning)):
                            fun.delete_file(meaning[i])
                    else:
                        fun.delete_file(meaning[2])
                elif (meaning[1] == '-fo'):
                    if (len(meaning) > 3):
                        for i in range(2, len(meaning)):
                            fun.delete_dir(meaning[i])
                    else:
                        fun.delete_dir(meaning[2])

# 4. renaming files and directories
            elif (meaning[0] == 'rename'):
                if (meaning[1] == '-fi'):
                    fun.rename_file(meaning[2], meaning[3])
                elif (meaning[1] == '-fo'):
                    fun.rename_dir(meaning[2], meaning[3])

# 5. for opening help
            elif (prompt == 'help'):
                helps.Help()

# 6. changing the current working directory
            elif (meaning[0] == "cd"):
                if (len(meaning) == 1):
                    fun.change_dir(store)
                else:
                    fun.change_dir(meaning[1])

# 7. printing the current working directory
            elif (meaning[0] == "location"):
                fun.current_dir()

# 8. for printing the contents of a file
            elif (meaning[0] == "show"):
                fun.open_file(meaning[1])

# 9. editing files with notepad
            elif(meaning[0]=="edit"):
                fun.edit_file(meaning[1])

# 10. moving file
            elif(meaning[0]=="move"):
                if(meaning[1]=="-fi"):
                    if (len(meaning) > 3):
                        for i in range(2, len(meaning)):
                            fun.move_file(meaning[i],meaning[len(meaning)-1])
                    else:
                        fun.move_file(meaning[2],meaning[3])
                if (meaning[1] == "-fo"):
                    if (len(meaning) > 3):
                        for i in range(2, len(meaning)):
                            fun.move_file(meaning[i], meaning[len(meaning) - 1])
                    else:
                        fun.move_file(meaning[2], meaning[3])

# 11. searching for a file
            elif(meaning[0]=="search"):
                if(len(meaning)==3):
                    fun.check_exists(meaning[1],meaning[2])
                else:
                    fun.check_exists(meaning[1],fun.current_dir())

# 12. exiting form the program
            elif(meaning[0]=="exit"):
                break

# 13. copy file to a destination
            elif(meaning[0]=="copy"):
                if(meaning[1]=="-fi"):
                    fun.copy_file(meaning[2],meaning[3])
                elif(meaning[1]=="-fo"):
                    fun.copy_dir(meaning[2],meaning[3])

# 14. checking disk usage
            elif(meaning[0]=="stats"):
                fun.check_usage(meaning[1])

# 15. searching for a text inside txt file
            elif(meaning[0]=="searchf"):
                fun.search_inside(meaning[1],meaning[2])









    
        except FileNotFoundError:
            print("File Not Found... !")
            print("Check the file name and enter again")
        except PermissionError:
            print("Looks like u have opened the same folder in other programs")
            print("close them for deleting")
        except FileExistsError:
            print("The file or folder that u are trying to create, it already exists")
        except IndexError:
            print("You have entered an incomplete command,")
            print("check your command and try again")
            print("ENTER ' help ' to view the command manual")
        except:
            print("Something is wrong, please try again")
            print("ENTER 'help' for command manual")
import time
def Help():
        print("""
    	ENTER NUMBER ACCORDING TO THE LISTINGS BELOW AND YOU WILL BE SHOWN THE MANUAL ACCORDINGLY.
    	******************************************************************************************
    	note: you have to exit the help section to continue with the command line

    		1)Creating Files and Directories
    		2)Renaming Files and Directories
    		3)Deleting Files and Directories
    		4)Editing Files with Notepad
    		5)Listing Files and Directories
    		6)Copying Files
    		7)Moving Files and Directories
    		8)Navigating Through Directories
    		9)Searching for Files inside a directory or disk
    		10)Searching for a particular word inside a text file.
    		11)Checking the disk space for a disk or a directory
    		12)Printing the contents of a text file
            	13)For Getting the Current Directory or Path name
    		14)To Exit Help Section and Return To Main Section

    """)
        while(True):

            ask=int(input("help>> "))
            time.sleep(1)
	
            if(ask==1):
                    print("""
                for creating use          ' cr '   command
                for specifying file use   '-fi'    option
                for specifying folder use '-fo'    option

                further also include the name of the file or folder that u want to create

                Example: Creating a file named hello.txt
                        cr -fi hello.txt

                Example: Creating a folder name myfolder
                        cr -fo myfolder

                    """)
                    print("-x-x-x-x-x-x--x-x-xx-x--x--x-x-x-x--x-x-x-x--x-x--x-x--x-x-x-x--x-x")

            if(ask==2):
                    print("""
                for renaming use          ' rename '   command
                for specifying file use   '-fi'        option
                for specifying folder use '-fo'        option

                further also include the name of the file to be renamed and the name to it must be renamed.
                i.e [name] [new_name]
                

                Example: renaming a file named hello.txt to world.txt
                        rename -fi hello.txt world.txt

                Example: renaming a folder named myfolder to yourfolder
                        rename -fo myfolder yourfolder

                    """)
                    print("-x-x-x-x-x-x--x-x-xx-x--x--x-x-x-x--x-x-x-x--x-x--x-x--x-x-x-x--x-x")

            if(ask==3):
                    print("""
                for deleting use          ' delete '   command
                for specifying file use   '-fi'        option
                for specifying folder use '-fo'        option

                Example: *deleting a file named hello.txt*
                        delete -fi hello.txt

                Example: *deleting a folder name myfolder*
                        delete -fo myfolder

                    """)
                    print("-x-x-x-x-x-x--x-x-xx-x--x--x-x-x-x--x-x-x-x--x-x--x-x--x-x-x-x--x-x")

            if (ask == 4):
                    print("""
                                for editing use          ' edit '   command

                                further include the name of the file that u want to edit

                                Example: for editing hello.txt in notepad
                                            edit hello.txt


                                    """)
                    print("-x-x-x-x-x-x--x-x-xx-x--x--x-x-x-x--x-x-x-x--x-x--x-x--x-x-x-x--x-x")

            if(ask==5):
                    print("""
                for listing all the files and folders in current folder use  ' ls ' command

                Example: listing files and directories
                        ls

                    """)
                    print("-x-x-x-x-x-x--x-x-xx-x--x--x-x-x-x--x-x-x-x--x-x--x-x--x-x-x-x--x-x")

            if(ask==6):
                    print("""
                for copying use          ' copy '   command
                for specifying file use   '-fi'    option
                for specifying folder use '-fo'    option

                further also include the name of the file/files that u want to copy and atlast destination 
                of the folder that you want to copy in

                Example: *Copying files hello.txt mellow.txt zellow.txt to Myfolder*
                        copy -fi hello.txt mellow.txt zellow.txt hi.txt MyFolder


                    """)
                    print("-x-x-x-x-x-x--x-x-xx-x--x--x-x-x-x--x-x-x-x--x-x--x-x--x-x-x-x--x-x")

            if(ask==7):
                    print("""
                for moving use          ' move '   command
                for specifying file use   '-fi'    option
                for specifying folder use '-fo'    option

                further also include the name of the file/files that u want to move and atlast destination 
                of the folder that you want to move in

                Example: Moving files named hello.txt mellow.txt zellow.txt to Myfolder
                        move -fi hello.txt mellow.txt zellow.txt MyFolder

                Example: Moving a folder named myfolder and yourFolder to NewFolder
                        move -fo myfolder yourFolder NewFolder

                    """)
                    print("-x-x-x-x-x-x--x-x-xx-x--x--x-x-x-x--x-x-x-x--x-x--x-x--x-x-x-x--x-x")


            if (ask == 8):
                    print("""
                            for navigation use    ' cd '   command

                            further include the path of the directory to which you want to move in 

                            Example: changing the working directory to B:\Programs present on the disk B
                                    cd B:\Programs

                            Example: changing the working directory to the Assignments having relative path 
                                     on disk
                                     
                                    cd Assignments

                                """)
                    print("-x-x-x-x-x-x--x-x-xx-x--x--x-x-x-x--x-x-x-x--x-x--x-x--x-x-x-x--x-x")


            if (ask == 9):
                    print("""
                            for searching use          'search'   command
                           
                            further include the name of the file that you want to search and then include
                            the name of the target directory that you want to search in

                            Example: searching hello.txt inside directory B:\programs\
                                    search hello.txt B:\programs\

                                """)
                    print("-x-x-x-x-x-x--x-x-xx-x--x--x-x-x-x--x-x-x-x--x-x--x-x--x-x-x-x--x-x")

            if (ask == 10):
                    print("""
                                 for searching inside a file  use   ' searchf '   command

                                 further include the word or line that you want to search and then include
                                 the name of the target file that you want to search in

                                 Example: searching " world " inside file hello.txt
                                         searchf world B:\programs\hello.txt

                                     """)
                    print("-x-x-x-x-x-x--x-x-xx-x--x--x-x-x-x--x-x-x-x--x-x--x-x--x-x-x-x--x-x")

            if (ask == 11):
                    print("""
                            for checking use   ' stats '   command
                            
                            further include the name of the disk that u want to check
                            
                            Example: for checking the local disk B
                                        stats B:\
 

                                """)
                    print("-x-x-x-x-x-x--x-x-xx-x--x--x-x-x-x--x-x-x-x--x-x--x-x--x-x-x-x--x-x")

            if (ask == 12):
                    print("""
                                for printing use   ' show '   command

                                further include the name of the text file that u want to show content of
                                if file is in different directory or disk then path that must also be included with name
                                
                                Example: for printing contents of hello.txt present in local disk b: 
                                            show B:\myprograms\hello.txt


                                    """)
                    print("-x-x-x-x-x-x--x-x-xx-x--x--x-x-x-x--x-x-x-x--x-x--x-x--x-x-x-x--x-x")

            if (ask == 13):
                    print("""
                            for getting the name or path of the current location or present working directory
                            use ' location ' command
                            
                            Example: location
                            """)
            if(ask==14):
                    break;


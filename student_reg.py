
# create exam registration function
# initialise while statment to handle file i/o with error checks
# create name count for file entry & create log file for file handling 
def exam_reg():
    while True:
        try:
            name_count = int(input(" Please enter number of students : "))
            if name_count < 2:
                print("\nError need more students please retry!\n")
                with open("error_log.txt", 'a') as file:
                    file.write (str(f"\n 'var' name_count : {ValueError} = requirement not satisfied "))
                exam_reg()
            break
        except ValueError:   
            print("\n invalid response please retry with a number: \n")
            with open("error_log.txt", 'a') as file:
                file.write (str(f"\n 'var' name_count : {ValueError} = {name_count} "))
## O(m) 

# create var for student id input & run for count given
# handle & store data given into file for student signing & error handle inputs 
    while True:
        try:
            student_input = int(input(" please enter your student number : "))
            with open("reg_form.txt", 'a') as file:
                file.write (str(f"Student_Id : {student_input}\nplease sign here : .................\n"))
            while name_count != 0:
                name_count -= 1
                break
        except ValueError:   
            print("\n invalid response please retry with a valid student id: \n")
            with open("error_log.txt", 'a') as file:
                file.write (str(f"\n 'var' student_input : {ValueError} = non int "))
        if name_count == 0:
            break
## O(1) 
    
# create an options list for user convenience
# use file handling for user input  
        def options():
            print("\n1 : open reg_form.txt file \n2 : clear reg_form.txt file \n3 : open error_log.txt file \n4 : clear error_log.txt file\n5 : reload student id register")
            
            while True:
                try:
                    option_sel = int(input("\nEnter an option number from above : "))
                    if option_sel == 1:
                        with open("reg_form.txt", 'r', encoding='utf-8') as file:
                            lines = file.read()
                            print(lines)
                    if option_sel == 2:
                        with open("reg_form.txt", 'w', encoding='utf-8') as file:
                            file.write (str(" "))
                            print("reg_form deleted!")                       
                    if option_sel == 3:
                        with open("error_log.txt", 'r', encoding='utf-8') as file:
                            lines = file.read()
                            print(lines)                           
                    if option_sel == 4:
                        with open("error_log.txt", 'w', encoding='utf-8') as file:
                            file.write (str(" "))
                            print("error_log deleted!")
                    if option_sel == 5:
                        exam_reg()                           
                    if option_sel  < 1:
                        print("\ninvalid response please retry with a valid option number : 1 - 5\n")
                        with open("error_log.txt", 'a') as file:
                            file.write (str(f"\n 'var' option_sel : {ValueError} = invalid option number "))
                        options()
                    if option_sel > 5:
                        print("\ninvalid response please retry with a valid option number : 1 - 5\n")
                        with open("error_log.txt", 'a') as file:
                            file.write (str(f"\n 'var' option_sel : {ValueError} = invalid option number "))        
                        options()    
                    break
                except ValueError:   
                    print("\ninvalid response please retry with a number 'int': \n")
                    with open("error_log.txt", 'a') as file:
                        file.write (str(f"\n 'var' option_sel : {ValueError} = invalid selection "))           

## O(k) where "k" is the total number of characters in the files being read or written ##
                    
            reload = input(" would you like to continue y/n : ").lower()
            if reload == 'y':
                options()
            if reload == 'n':
                print(" Good Bye!")
                quit()
                
    options()                    
exam_reg()
            
#  #=================== Big O Notation ========================#        #====================== pseudo code ===========================#
#  # the overall time complexity of the code                   #        #Begin                                                         #
#  # can be expressed as O(m + n + k), where "m"               #        #    get user input for class size                             #                                                       
#  # depends on the initial user input                         #        #    handle user i\o                                           #                                                                                                               
#  # "n" depends on user input within the options()function    #        #    Provide multiple functions related to exam registration   #
#  # "k" depends on the file sizes involved in file operations #        #    (student name,id)                                         #
#  #===========================================================#        #    store data into file with signing dots for later use      #
#                                                                       #    error handle user input                                   #
#                                                                       #    user options for files to be displayed, cleared           #
#                                                                       #    reload option                                             #
#                                                                       #    error handle user input                                   #
#                                                                       #End                                                           #
#                                                                       #==============================================================#
#                                                                       
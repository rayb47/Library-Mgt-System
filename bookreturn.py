from tkinter import *

def ReturnButtons():
    '''
    In this function, we create the buttons that are displayed on the screen after clicking the 'Return' button located at the top, on executing the code.
    '''
    global Book_ID_Entry_2
    global ButtonAdd

    #Creating a label saying 'Book Checkout'
    ForReturn = Label(OtherFrame, text = 'Book Return :')
    ForReturn.config(font=("Comic Sans",15))
    ForReturn.grid(row = 0 , column = 0,  padx = 0)

    #Disabling the on-screen buttons to force the user to hit reset after return is carried out.
    Button1.config(state = 'disabled')
    Button2.config(state = 'disabled')
    Button3.config(state = 'disabled')
    Button4.config(state = 'disabled')

    #Creating a label and an entry box for the Book ID 
    Book_ID_2 = Label(OtherFrame, text = 'Book ID :')
    Book_ID_Entry_2 = Entry(OtherFrame, width = 10, bg = '#dae69e')
    Book_ID_2.grid(row = 1, column = 0, padx = 0, sticky = 'e')
    Book_ID_Entry_2.grid(row = 1, column = 1, pady = 10, sticky = 'w')

    #Adding a 'Continue' button which when hit, calls the main 'Return' function.
    ButtonAdd = Button(OtherFrame, text = 'Continue', command = Return)
    ButtonAdd.grid(row = 1, column = 2, padx = 10)

def Return():
    '''
    This function carries out the return of a singular book depending on the Book ID that has been entered into the entry boxes.
    '''

    #These commands deny the user from re-using either the entry box or the continue button without hitting 'Reset'.
    Book_ID_Entry_2.config(state='readonly')
    ButtonAdd.config(state = 'disabled')

    
    file1 = open('logfile.txt')
    file2 = open('database.txt')
    Bk_ID = str(Book_ID_Entry_2.get())

    '''
        List3 is the list of records in the log file, which is being updated as the return takes place
        List4 is the list of records in the database file, which is being updated as return takes place
        List5 contains the heading for the table, along with the details of the book that has been returned
    '''
    List3 = []
    List4 = []
    List5 = [['Book ID','Date Borrowed','Date Returned']]
    returned = 0
    book_found = 0
    try:
        for line in file1:
            line = line.strip()
            line1 = line.split(",")

            #A record which basically represents a line from the log text file.
            Forlog = line1[0]+","+line1[1]+","+line1[2]+"\n"

            #To check whether the entered book ID matches and also whether there is no return date present in the log file for the same book.
            if line1[0] == str(Bk_ID) and line1[2] == '':
                
                #Updating return date in the log file for the specific book/record.
                line1[2] = today
                Forlog = line1[0]+","+line1[1]+","+str(line1[2])+"\n"
                List3.append(Forlog)
                Forlog = Forlog.split(",")
                List5.append(line1)
                returned = 1


            #To check whether book has been returned already
            elif line1[0] == str(Bk_ID) and line1[2] != '':
                List3.append(Forlog)
            else:
                List3.append(Forlog)
        file1.close()
        file4 = open('logfile.txt','w')
        file4.writelines(List3)
        file4.close()

        #Writing of records into the database based on whichever book was returned.  (i.e: Member ID goes to 0 again)
        if returned == 1:
            for line in file2:
                line = line.strip()
                line1 = line.split(",")
                rec = line1[0]+","+line1[1]+","+line1[2]+","+line1[3]+","+line1[4]+","+line1[5]+"\n"
                if int(line1[0])==int(Bk_ID):
                    line1[5]='0'
                    rec = line1[0]+","+line1[1]+","+line1[2]+","+line1[3]+","+line1[4]+","+line1[5]+"\n"
                    List4.append(rec)
                else:
                    List4.append(rec)
            file5 = open('database.txt','w')
            file5.writelines(List4)
            file5.close()
        else:
            for line in file2:
                line = line.strip()
                line1 = line.split(",")
                rec = line1[0]+","+line1[1]+","+line1[2]+","+line1[3]+","+line1[4]+","+line1[5]+"\n"
                if int(line1[0])==int(Bk_ID):
                    book_found = 1
            if book_found == 0:
                Error_Message = Label(ErrorFrame,text = '*** ERROR  Invalid book ID entered. ***')
            else:
                 Error_Message = Label(ErrorFrame,text = '*** ERROR  Book is not issued. ***')
            Error_Message.grid()
            
                
            
            
        file2.close()
        #file5 = open('database.txt','w')
        #file5.writelines(List4)
        #file5.close()
        width = len(List5[0])
        height = len(List5)
        for i in range(height):
            for j in range(width): #Columns
                if i == 0:
                    b = Entry(TableFrame, text="", bg = '#b0b8bf', justify = 'center')
                else:
                    b = Entry(TableFrame, text="",  justify = 'center')
                b.grid(row=i, column=j)
                b.insert(END, List5[i][j])
    except:
        Error_Message = Label(ErrorFrame,text = '*** ERROR  Incorrect book ID entered. ***')
            
        Error_Message.grid()

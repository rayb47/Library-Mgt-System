from tkinter import *

def searchbuttons():
    '''
    In this function, we create the buttons that are displayed on the screen after clicking the 'Search' button located at the top, on executing the code.
    '''
    global Entry1

    #Creating a label saying 'Book Search'
    ForSearch = Label(OtherFrame, text = 'Book Search :')
    ForSearch.config(font=("Comic Sans",15))
    ForSearch.grid(row = 0, column = 0)

    #Disabling the on-screen buttons to force the user to hit reset after search is carried out.
    Button1.config(state = 'disabled')
    Button2.config(state = 'disabled')
    Button3.config(state = 'disabled')
    Button4.config(state = 'disabled')
    
    #Creating a Label and an entry box where the book title is entered and stored as a string.
    Lbl1 = Label(OtherFrame, text = 'Book Title : ')
    Lbl1.grid(row = 1, column = 0, sticky='e')
    Entry1 = Entry(OtherFrame, width = 40, bg = '#b8e0cb')
    Entry1.grid(row = 1, column =1)

    #Adding a 'Continue' button which when hit, calls the main 'search' function.
    ButtonAdd = Button(OtherFrame, text = 'Continue', command = search, width = 8, height = 1 )
    ButtonAdd.grid(row = 1, column = 2, padx = 15, pady = 15)


def search():
    '''
    This function carries out the book search based on whatever book title is entered into the entry box
    '''

    #The following command prevents the user from re-using the entry box without hitting 'Reset' 
    Entry1.config(state='readonly')
    
    book_title = str(Entry1.get())

    #The list below contains the heading for the table to be displayed. Later in the function, all the necessary records are appended to this list inorder to be displayed.
    MainList = [['Book ID','ISBN Number','Book Title','Author Name','Date Purchased','Member ID']]
    
    file1 = open('database.txt','r')
    book_found = 0

    #Reading every line in the database file
    for line in file1:
        line = line.strip()
        line1 = line.split(",")
        if (line1[2]).lower()==(book_title).lower():        
            MainList.append(line1)
            book_found = 1

    #Displaying an error message for when a non existent book is entered.    
    if book_found == 0:
        Error_Message = Label(ErrorFrame,text = '*** ERROR  This book does not exist. ***')
        Error_Message.grid()
        
    file1.close()

    #Defining the height and list for the table to be displayed
    height = len(MainList)
    width = len(MainList[0])
    for i in range(height): #Rows
        for j in range(width): #Columns
            if i == 0:
                b = Entry(TableFrame, text="", bg = '#b0b8bf')
            else:
                b = Entry(TableFrame, text="")
            b.grid(row=i, column=j)
            b.insert(END, MainList[i][j])






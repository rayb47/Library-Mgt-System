'''
Raynell Braganza
Program Name : Python Library Management System
Developed By : Raynell Braganza
Student ID   : F013601
Date	     : Nov-Dec 2020
'''

from tkinter import *
from datetime import date
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #new
from matplotlib.figure import Figure #new
today = date.today()


    
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
           
                

def checkoutbuttons():
    '''
    In this function, we create the buttons that are displayed on the screen after clicking the 'Checkout' button located at the top, on executing the code.
    '''
    global Member_ID_Entry
    global Book_ID_Entry
    global Label1

    #Creating a label saying 'Book Checkout'
    ForCheckout = Label(OtherFrame, text = 'Book Checkout :')
    ForCheckout.config(font=("Comic Sans",15))
    ForCheckout.grid(row = 0, column = 2, padx = 5)

    #Disabling the on-screen buttons to force the user to hit reset after checkout is carried out.
    Button1.config(state = 'disabled')
    Button2.config(state = 'disabled')
    Button3.config(state = 'disabled')
    Button4.config(state = 'disabled')

    #Creating a label and an entry boxes for the Book ID and Member ID respectively
    Book_ID = Label(OtherFrame, text = 'Book ID :')
    Book_ID_Entry = Entry(OtherFrame, width = 15, bg = '#eddab4')
    Member_ID = Label(OtherFrame, text = 'Member ID :')
    Member_ID_Entry = Entry(OtherFrame, width = 15, bg = '#eddab4')
    Book_ID.grid(row = 1, column = 2, pady = 10, sticky = 'e')
    Book_ID_Entry.grid(row = 1, column = 3, padx = 0)
    Member_ID.grid(row = 2, column = 2, sticky = 'e')
    Member_ID_Entry.grid(row = 2, column = 3, padx = 0, sticky = 'e')

    #Adding a 'Continue' button which when hit, calls the main 'checkout' function.
    Label1 = Button(OtherFrame, text = 'Continue', command = checkout)
    Label1.grid(row = 2, column = 4, padx = 17, sticky = 'e')


def checkout():
    '''
    This function carries out the checkout of a singular book depending on the Book ID and Member ID that have been entered into the entry boxes.
    '''

    #These commands deny the user from re-using either of the entry boxes without hitting 'Reset'.
    Book_ID_Entry.config(state='readonly')
    Member_ID_Entry.config(state='readonly')
    Label1.config(state = 'disabled')
    
    try:
        On_Loan = 0
        Wrong_Book_ID = 1
        file1 = open('database.txt')
        '''
        List1 is the list of records in the database file, which is being updated as checkout takes place
        List2 contains the heading for the table, along with the details of the book that has been checked out
        List3 is the list of records in the log file, which is being updated as checkout takes place
        '''
        List1 = []
        List2 = [['Book ID','ISBN Number','Book Title','Author Name','Date Purchased','Member ID']]
        List3 = []
        file3 = open('logfile.txt','a')
        ID_Member = str(Member_ID_Entry.get())

        #To check if inputted member ID is valid or not.
        if int(ID_Member) < 1000 or int(ID_Member) > 9999:
            Error_Message = Label(ErrorFrame,text = '***ERROR. ID must be a numeric value in range 1000-9999***')
            Error_Message.grid()
        else:
            ID_Book = str(Book_ID_Entry.get())
            for line in file1:
                line = line.strip()
                line1 = line.split(",")
                #MainList.append(line1)
                #A record which basically represents a line from the database text file
                rec = line1[0]+","+line1[1]+","+line1[2]+","+line1[3]+","+line1[4]+","+line1[5]+"\n"

                #To check whether book being checked out is already available in the library
                if int(line1[0])==int(ID_Book):
                    Wrong_Book_ID = 0

                #To check if book is on loan to someone else
                if int(line1[5])!=0 and int(line1[0])==int(ID_Book) :      
                    On_Loan = 1
                    Error_Message = Label(ErrorFrame,text = '*** ERROR  Book has already been checked out. ***')
            
                    Error_Message.grid()

                #To check if book is available for borrowing
                if int(line1[5])==0 and int(line1[0])==int(ID_Book):
                    rec = line1[0]+","+line1[1]+","+line1[2]+","+line1[3]+","+line1[4]+","+str(ID_Member)+"\n"
                    Forlog = line1[0]+","+str(today)+","+""+"\n"
                    List1.append(rec)
                    rec = rec.split(",")
                    List2.append(rec)
                    List3.append(Forlog)
                else:
                    List1.append(rec)
                    
            file1.close()
            file3.writelines(List3)
            file3.close()

            #Defining height and width for the table to be displayed
            height = len(List2)
            width = len(List2[0])
            for i in range(height):
                for j in range(width): 
                    if i == 0:
                        if j==0:
                            b = Entry(TableFrame, text="", bg = '#b0b8bf', justify = 'center')
                        else:
                            b = Entry(TableFrame, text="", bg = '#b0b8bf')
                    elif j ==0:
                        b = Entry(TableFrame, text="", justify = 'center')
                    else:
                        b = Entry(TableFrame, text="")
                    b.grid(row=i, column=j)
                    b.insert(END, List2[i][j])
            file2 = open('database.txt','w')
            file2.writelines(List1)
            file2.close()
            
    except ValueError:
        Error_Message = Label(ErrorFrame,text = '*** ERROR  Book ID must be a numeric value. ***')
            
        Error_Message.grid()
    except IndexError:
        Error_Message = Label(ErrorFrame,text = '*** ERROR  Book is not in database. ***')
            
        Error_Message.grid()
        
        

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
        

# take fifth element for sort
def SortArray(List1):
    return List1[4]



def WeedingButtons():
    '''
    In this function, we create the buttons that are displayed on the screen after clicking the 'Weeding' button located at the top, on executing the code.
    '''
    
    global Weeding_Label_Entry
    global Weeding_Continue

    #Disabling the on-screen buttons to force the user to hit reset after weeding is carried out.
    Button1.config(state = 'disabled')
    Button2.config(state = 'disabled')
    Button3.config(state = 'disabled')
    Button4.config(state = 'disabled')
    
    #Creating a label and an entry box for the number of days not borrowed
    Weeding_Label = Label(OtherFrame, text = 'Days not borrowed : ')
    Weeding_Label.grid(row = 0, column = 0)
    Weeding_Label_Entry = Entry(OtherFrame, width = 10, bg = '#f5e4f7')
    Weeding_Label_Entry.grid(row = 0, column = 2)

    #Adding a 'Continue' button which when hit, calls the main 'Weeding' function.
    Weeding_Continue = Button(OtherFrame, text = 'Continue', command = Weeding)
    Weeding_Continue.grid(row = 0 , column = 3, padx = 10, pady = 15)

def Weeding():
    '''
    This function carries out the weeding of books based on the 'days not borrowed' entered into the entry box.   
    '''

    #These commands denies the user from re-using either the entry box or the continue button without hitting 'Reset'.
    Weeding_Continue.configure(state = 'disable')
    DisplayList = [['Book Title','Book Copies','Average Age (Days)','Issued in <365 days','Issued in >365 days']]
    Borrowed_Days = str(Weeding_Label_Entry.get())

    #Validation for number of days borrowed entered.
    if int(Borrowed_Days) < 30 or int(Borrowed_Days) > 180:
        Error_Message = Label(ErrorFrame,text = '*** ERROR  Days range must be between 30 - 180 ***')
        Error_Message.grid()
    else:
        file1 = open('database.txt')
        file2 = open('logfile.txt')
        List1 = []

        #Reading the database file
        for line in file1:
            line = line.strip()
            line1 = line.split(",")
            Book_ID = line1[0]

            #Getting date of when book was borrowed
            Date = line1[4]
            year = int(Date[:4])
            month = int(Date[5:7])
            day = int(Date[8:])
            
            t_date= str(today)
            
            
            today_year = t_date[:4]
            today_month = t_date[5:7]
            today_day = t_date[8:]
            f_date = date(year,month,day)
            
            l_date = date(int(today_year),int(today_month),int(today_day))
            age = l_date - f_date

            days1,days2,days3 = 0,0,0
            file2.seek(0)
            found = 0

            #Reading the text file
            for Line in file2:
                Line = Line.strip()
                Line1 = Line.split(",")
                
                #Checking for matching Book ID
                if int(Line1[0]) == int(Book_ID):

                    #Number of days borrowed (Today's Date - Borrowed Date)
                    Date = Line1[1]
                    year = int(Date[:4])
                    month = int(Date[5:7])
                    day = int(Date[8:])
            
                    t_date= str(today)
            
                    today_year = t_date[:4]
                    today_month = t_date[5:7]
                    today_day = t_date[8:]
                    f_date = date(year,month,day)

                    l_date = date(int(today_year),int(today_month),int(today_day))
                    diff = l_date - f_date
                    
                    if diff.days < int(Borrowed_Days):
                        days1+=1
                    elif diff.days < 365:
                        days2+=1
                    else:
                        days3+=1
                
            for x in range(len(List1)):
                
                if line1[2] == List1[x][0]:
                    count = int(List1[x][1]) + 1
                
                    age_days = int(List1[x][2]) + age.days
                    days1 = days1 + int(List1[x][3]) 
                    days2 = days2 + int(List1[x][4]) 
                    days3 = days3 + int(List1[x][5])
                    avg_days = age_days//count
                    
                    rec = line1[2]+","+str(count)+","+str(age_days)+","+str(days1)+","+str(days2)+","+str(days3)+","+str(avg_days)
                    rec = rec.split(",")
                    List1[x] = rec
                    found = 1
                    break
            if found == 0:
                rec = line1[2]+","+'1'+","+str(age.days)+","+str(days1)+","+str(days2)+","+str(days3)+","+str(age.days)
                rec = rec.split(",")
                List1.append(rec)
           
        sizes = [0,0,0]

        width = 5
        height = 0
        
        for l in range(len(List1)):
            if int(List1[l][3])!=0:
                sizes[0]+=1
            elif int(List1[l][4])!=0:
                sizes[1]=1
            else:
                sizes[2]+=1


        List1.sort(key=SortArray)

        #Finding height of the grid
        for i in range(len(List1)):
            if int(List1[i][3])==0:
                height+=1
                DisplayList.append([List1[i][0],List1[i][1],List1[i][6],List1[i][4],List1[i][5]])
        #Displaying the grid        
        for i in range(height):
            for j in range(width): #Columns
                if i == 0:
                    if i==0 and j==0:
                        b = Entry(TableFrame, text="", bg = '#b0b8bf', width = 51)
                    else:
                        b = Entry(TableFrame, text="", bg = '#b0b8bf', width = 17, justify = 'center')
                else:
                    if j==0:
                        b = Entry(TableFrame, text="", width = 51)
                    else:
                        b = Entry(TableFrame, text="", width = 17, justify = 'center')
                b.grid(row=i, column=j)
                b.insert(END, DisplayList[i][j])
                
                
        labels = '<{0} days'.format(Borrowed_Days), '<365 days', '>365 days'

        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        explode = (0, 0, 0.1)  # only "explode" the 2nd slice

       
        fig1, ax1 = plt.subplots()
        plt.title('BOOK MOVEMENT')
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.show()


        
        

def reset():
    #Destroys all widgets from frame
    Button1.config(state = 'normal')
    Button2.config(state = 'normal')
    Button3.config(state = 'normal')
    Button4.config(state = 'normal')
    for widget in OtherFrame.winfo_children():
       widget.destroy()
    OtherFrame.pack_forget()
    for widget in TableFrame.winfo_children():
       widget.destroy()
    TableFrame.pack_forget()
    for widget in ErrorFrame.winfo_children():
       widget.destroy()
    ErrorFrame.pack_forget()
   
   
def exitprog():
    #Exits the program
    window.destroy()



#Creating the tkinter window
window = Tk()
window.title('LIBRARY MANAGEMENT SYSTEM   v2020.001')
window.geometry('760x480')

ButtonFrame = Frame(window, relief='sunken', borderwidth = 1, bg='#968d8d', width = 40)
ButtonFrame.grid(row = 0, column = 0, columnspan = 7, sticky = 'w')


#Creating the buttons for the operations
Button1 = Button(ButtonFrame, text = 'Search', bg='#b8e0cb', command = searchbuttons, relief = 'groove', width = 9)
Button2 = Button(ButtonFrame, text = 'Checkout', bg='#eddab4', command = checkoutbuttons, relief = 'groove', width = 10)
Button3 = Button(ButtonFrame, text = 'Return', bg='#dae69e', command = ReturnButtons, relief = 'groove', width = 10)
Button4 = Button(ButtonFrame, text = 'Weeding', bg='#f5e4f7', command = WeedingButtons, relief = 'groove', width = 10)
Button5 = Button(ButtonFrame, text = 'Reset', bg='#bbb5eb', command = reset, relief = 'groove', width = 9)
Button6 = Button(ButtonFrame, text = 'Exit', bg='#99cbf7', command = exitprog, relief = 'groove', width = 9)

#Positioning the buttons
Button1.grid(row = 0, column = 0, padx = 25, pady = 15)
Button2.grid(row = 0, column = 1, padx = 25, pady = 15)
Button3.grid(row = 0, column = 2, padx = 25, pady = 15)
Button4.grid(row = 0, column = 3, padx = 25, pady = 15)
Button5.grid(row = 0, column = 4, padx = 25, pady = 15)
Button6.grid(row = 0, column = 5, padx = 25, pady = 15)

#Creating the other frames to display the grid, entry boxes and error messages, if necessary.
OtherFrame = Frame(window, borderwidth = 1)
OtherFrame.grid(row = 1, column = 0, columnspan = 7 , sticky ='w', pady = 10)

TableFrame = Frame(window, borderwidth = 2)
TableFrame.grid(row = 2, column = 0, columnspan = 7, sticky = 'w', pady = 25)

ErrorFrame = Frame(window, borderwidth = 4)
ErrorFrame.grid(row = 3, column = 1, columnspan = 5, pady = 0)


window.mainloop()




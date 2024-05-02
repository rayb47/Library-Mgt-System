from tkinter import *

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


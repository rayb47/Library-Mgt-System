Features:
Program is developed in Tkinter with GUI features and has the following Menu options buttons:
Book Search, Issue, Return, Weeding, Reset & Exit 

1) Book Search
Allows user to search for a book by entering the complete Book name. The search here is NOT case sensitive.
Program will display all matched records from the Database file in a grid the Book ID, ISBN, Book Title, Author, Purchase date and Member ID (If the book is loaned)
Incase no match is found program will display an Error Message.

2) Book Checkout
User needs to enter Book ID and Member ID. The following validations are performed,
Book ID entered must be a valid Book ID; Customer ID must be in the range of 1000 to 9999 and finally the book must not already be loaned.
If validation is successful a grid will display all the fields from the database for the book that is being checked out.
The Master database record will be updated with Customer ID & a new record will be created in the Log file with Book ID, Todays date as issue date & return date set to 0 

3) Book Return
User needs to Enter Book ID. The following validations are performed,
Book ID must be valid; the book must already be loaned. If validation is successful a grid will display all fields from the logfile for the book that is being returned.
The record from the database will be updated with Customer ID set to 0 & and the Log Record for the loaned book will be updated with Book return date as todays date.

4) Weeding
Here we have the book info summarized by titles that have not been issued in the last "N" days, which is inputted by user. The day’s range is validated for being between 30 to 180 days.
A grid will display Book Title, Number of Book copies, Average age of book(s) ((Purchase date - Today's date) / Number of copies), Number of times the book has been issued in the last 12 months & in the last 12+ months.
The information displayed is sorted in ascending order of count of books issued in the last 365 days, which is will show least moving books at the top of the list.
The program will also display a pie chart with count of books not moved in the last "N" days, moved in the last 12 months & 12+ months

5)Reset
After execution of each of the above-mentioned features, the user will need to click on Reset Button & then select the next option to be executed.

6)Exit
Takes you out of the program.

I encountered a few issues while trying to import my individual files into the menu file. Hence, my menu file contains the complete code.
Which has run successfully and been fully tested by me.




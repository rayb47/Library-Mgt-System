

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
    Weeding_Continue.configure(state = 'disable')
    DisplayList = [['Book Title','Book Copies','Average Age (Days)','Issued in <365 days','Issued in >365 days']]
    Borrowed_Days = str(Weeding_Label_Entry.get())
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





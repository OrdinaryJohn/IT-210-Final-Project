# import modules
from tkinter import *
from tkinter import messagebox
import sqlite3
# connect to the databse.
conn = sqlite3.connect('database.db')
# cursor to move around the databse
c = conn.cursor()
# empty list to later append the ids from the database
ids = []
# tkinter window
class Application:
    def __init__(self, master):
        self.master = master

        # creating the frames in the master
        self.left = Frame(master, width=800, height=720, bg='purple')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=400, height=720, bg='steelblue')
        self.right.pack(side=RIGHT)

        #Label for window       
        self.heading = Label(self.left, text="Mankato State Tutor Center", font=('arial 40 bold'), fg='black', bg='gold')
        self.heading.place(x=0, y=0)


        #Student Id
        self.studentid = Label(self.left, text="Student's ID", font=('arial 18 bold'), fg='black', bg='gold')
        self.studentid.place(x=0, y=100)
    
        #Student's name
        self.name = Label(self.left, text="Student's Name", font=('arial 18 bold'), fg='black', bg='gold')
        self.name.place(x=0, y=140)

        #Major
        self.major = Label(self.left, text="Major", font=('arial 18 bold'), fg='black', bg='gold')
        self.major.place(x=0, y=180)

        #Appointment time
        self.scheduled_time = Label(self.left, text="Appointment Time", font=('arial 18 bold'), fg='black', bg='gold')
        self.scheduled_time.place(x=0, y=220)

        #Phone Number
        self.phone = Label(self.left, text="Phone Number", font=('arial 18 bold'), fg='black', bg='gold')
        self.phone.place(x=0, y=260)

        # Entries for all labels-----------------------------------------------
        self.studentid_ent = Entry(self.left, width=30)
        self.studentid_ent.place(x=250, y=105)

        self.name_ent = Entry(self.left, width=30)
        self.name_ent.place(x=250, y=145)

        self.major_ent = Entry(self.left, width=30)
        self.major_ent.place(x=250, y=185)

        self.scheduled_time_ent = Entry(self.left, width=30)
        self.scheduled_time_ent.place(x=250, y=230)

        self.phone_ent = Entry(self.left, width=30)
        self.phone_ent.place(x=250, y=275)

        #Button to perform a command
        self.submit = Button(self.left, text="Add Appointment", width=20, height=2, bg='steelblue', command=self.add_appointment)
        self.submit.place(x=300, y=340)
    
        #Getting the number of appointments fixed to view in the log
        sql2 = "SELECT ID FROM appointments "
        self.result = c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)
        
        #Ordering the ids
        self.new = sorted(ids)
        self.final_id = self.new[len(ids)-1]
        #Displaying the logs in our right frame
        self.logs = Label(self.right, text="Logs", font=('arial 28 bold'), fg='white', bg='steelblue')
        self.logs.place(x=1, y=1)

        self.box = Text(self.right, width=50, height=40)
        self.box.place(x=20, y=60)
        self.box.insert(END, "Number of appointments today:  " + str(self.final_id))
    #Funtion to call when the submit button is clicked
    def add_appointment(self):
        #Getting the user inputs
        self.var1 = self.studentid_ent.get()
        self.var2 = self.name_ent.get()
        self.var3 = self.major_ent.get()
        self.var4 = self.scheduled_time_ent.get()
        self.var5 = self.phone_ent.get()

        #Checking if the user input is empty
        if self.var1 == '' or self.var2 == '' or self.var3 == '' or self.var4 == '' or self.var5 == '':
            messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        else:
            #Adding to database
            sql = "INSERT INTO 'appointments' (studentid, name, major, scheduled_time, phone) VALUES(?, ?, ?, ?, ?)"
            c.execute(sql, (self.var1, self.var2, self.var3, self.var4, self.var5))
            conn.commit()
            messagebox.showinfo("Success", "Appointment for " +str(self.var2) + " has been created" )
            

            self.box.insert(END, '\nAppointment fixed for ' + str(self.var2) + ' at ' + str(self.var4))

# creating the object
root = Tk()
b = Application(root)

# resolution of the window
root.geometry("1200x720+0+0")

# preventing the resize feature
root.resizable(False, False)

# end the loop
root.mainloop()



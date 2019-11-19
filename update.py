# update the appointments
from tkinter import *
from tkinter import messagebox 
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

class Application:
    def __init__(self, master):
        master.title("Update")
        master.configure(background='purple')
        self.master = master
        # heading label
        self.heading = Label(master, text="Update Appointments",  fg='black', bg='gold', font=('arial 40 bold'))
        self.heading.place(x=0, y=0)

        # search criteria -->student id 
        self.studentid = Label(master, text="Enter Student ID", bg='gold', font=('arial 18 bold'))
        self.studentid.place(x=0, y=80)

        # entry for  the student id
        self.studentidnet = Entry(master, width=30)
        self.studentidnet.place(x=280, y=90)

        # search button
        self.search = Button(master, text="Search", width=12, height=1, bg='steelblue', command=self.search_db)
        self.search.place(x=350, y=120)
    # function to search
    def search_db(self):
        self.input = self.studentidnet.get()
        # execute sql 

        sql = "SELECT * FROM appointments WHERE studentid LIKE ?"
        self.res = c.execute(sql, (self.input,))
        for self.row in self.res:
            self.studentid = self.row[1]
            self.name = self.row[2]
            self.major = self.row[3]
            self.time = self.row[4]
            self.phone = self.row[5]

        # creating the update form
        self.uname = Label(self.master, text="Student's Name", bg='gold', font=('arial 18 bold'))
        self.uname.place(x=0, y=160)

        self.umajor = Label(self.master, text="Major", bg='gold', font=('arial 18 bold'))
        self.umajor.place(x=0, y=200)

        self.uscheduled_time = Label(self.master, text="Appointment Time", bg='gold', font=('arial 18 bold'))
        self.uscheduled_time.place(x=0, y=240)

        self.uphone = Label(self.master, text="Phone Number", bg='gold', font=('arial 18 bold'))
        self.uphone.place(x=0, y=280)

        # entries for each labels==========================================================
        # ===================filling the search result in the entry box to update
        self.ent1 = Entry(self.master, width=30)
        self.ent1.place(x=300, y=170)
        self.ent1.insert(END, str(self.name))

        self.ent2 = Entry(self.master, width=30)
        self.ent2.place(x=300, y=210)
        self.ent2.insert(END, str(self.major))

        self.ent3 = Entry(self.master, width=30)
        self.ent3.place(x=300, y=250)
        self.ent3.insert(END, str(self.time))

        self.ent4 = Entry(self.master, width=30)
        self.ent4.place(x=300, y=290)
        self.ent4.insert(END, str(self.phone))

        # button to execute update
        self.update = Button(self.master, text="Update", width=20, height=2, bg='lightblue', command=self.update_db)
        self.update.place(x=400, y=380)

        # button to delete
        self.delete = Button(self.master, text="Delete", width=20, height=2, bg='red', command=self.delete_db)
        self.delete.place(x=150, y=380)
    def update_db(self):
        # declaring the variables to update
        self.var1 = self.ent1.get() #updated name
        self.var2 = self.ent2.get() #updated major
        self.var3 = self.ent3.get() #updated scheduled_time
        self.var4 = self.ent4.get() #updated phone

        query = "UPDATE appointments SET name=?, major=?, scheduled_time=?, phone=? WHERE studentid LIKE ?"
        c.execute(query, (self.var1, self.var2, self.var3, self.var4, self.studentidnet.get(),))
        conn.commit()
        messagebox.showinfo("Updated", "Successfully Updated.")
    def delete_db(self):
        # delete the appointment
        sql2 = "DELETE FROM appointments WHERE studentid LIKE ?"
        c.execute(sql2, (self.studentidnet.get(),))
        conn.commit()
        messagebox.showinfo("Success", "Deleted Successfully")
        self.ent1.destroy()
        self.ent2.destroy()
        self.ent3.destroy()
        self.ent4.destroy()

# creating the object
root = Tk()
b = Application(root)
root.geometry("1200x720+0+0")
root.resizable(True, True)
root.mainloop()

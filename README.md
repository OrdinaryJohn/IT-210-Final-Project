# IT-210-Final-Project
Modules required to run program
- tkinter, mainly messagebox
- sqlite3 is needed to store information on the computer
- SQLite Manager was used on the raspberry pi to read the SQLite data.

For this project you want to open up the Appointment.py file first and 
put in all the necessary information in the boxes. If you do not fill in all boxes a message box will pop up to inform you to fill in all the boxes. Student ID can be whatever you want but it is intended to store the barcode information on the back of the MAV cards using the scanner. After filling in all the text boxes you hit the "Add Appointment" button. After that you can close the window and once you open it up you will see that the box in the right side will update. With that, you can head over to the Update.py file and change any information you need to by using your Student ID barcode and scanning it. After changing/deleting your info you can close out and see it updated in the update.py file when you search yourself, as well in the database file. We also intended that after students finished with their appointments, they would go to the Update.py file and delete their info since this is meant to be just used for that day. So it wouldn't say that the number of appointments is at 25 when most were already taken care of.

Hardware
- HP Keyboard
- Mouse
- Honeywell Voyager 1202G Scanner
  - You do not need any module to make the scanner work. Just scann the barcode of the MAV Card and it will read it.
- Monitor with HDMI port

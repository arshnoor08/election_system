from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os

candname = ""

def message():
    messagebox.showinfo('Vote counted', 'Response recorded')
    app.after(1000)

def save_info():
    message()
    student = studentemail.get()
    cand = candname
    print(student, cand)
    file = open("image_code_data.txt", "a")
    file.write("Student email: " + student)
    file.write("\n")
    file.write(cand)
    file.write("\n")
    file.close()

def cand1_calc():
    global candname
    candname="person 1"

def cand2_calc():
    global candname
    candname="person 2"

def cand3_calc():
    global candname
    candname="person 3"

def check_email():
    student = studentemail.get()
    cand = candname
    email_found = False

    # CHECKING IF EMAIL EXISTS IN DATABASE- ALREADY VOTED OR NOT- AND REMOVING EMAIL FROM DATABASE IF NOT VOTED
    with open("email_database.txt", "r") as input:
        with open("temp_database.txt", "w") as output:
            # iterate all lines from file
            for line in input:
                # if text matches then don't write it
                if line.strip("\n") != student:
                    email_found=True
                    output.write(line)
    # replace file with original name
    os.replace('temp_database.txt', 'email_database.txt')

    if(email_found):
        button = Button(app, text="Submit Data", command=save_info, width="30", height="2", bg="grey")
        button.place(x=90, y=350)
    else:
        button = Button(app, text="Submit Data", command=save_info, width="30", height="2", bg="grey", state=DISABLED)
        button.place(x=90, y=350)
        messagebox.showinfo('Invalid', 'Enter valid email')


app = Tk()
app.geometry("500x500")
app.title("School Captain Elections")

heading = Label(text="School Captain Elections", fg="black", bg="yellow", width="500", height="3", font="10")
heading.pack()

canvas = Canvas()
canvas.pack()

student = Label(text="Enter your SFHS email:")
# cand = Label(text="Candidate name :")

student.place(x=15, y=70)
# cand.place(x=15, y=140)

studentemail = StringVar()
candname = StringVar()

student_name_entry = Entry(textvariable=studentemail, width="30")
# cand_name_entry = Entry(textvariable=candname, width="30")

email_button = Button(app, text="Check email", command=check_email, width="15", height="1", bg="grey")
email_button.place(x=15, y=130)


student_name_entry.place(x=15, y=100)
# cand_name_entry.place(x=15, y=180)

buttonc1=Button(app,text='person 1', command=cand1_calc)
buttonc1.place(x=40, y=300)

buttonc2=Button(app,text='person 2', command=cand2_calc)
buttonc2.place(x=200, y=300)

buttonc3=Button(app,text='person 3', command=cand3_calc)
buttonc3.place(x=375, y=300)




# IMAGE- PERSON 1
person1 = Image.open("person1.jpeg")
person1 = person1.resize((100, 110), Image.ANTIALIAS)
img_per1 = ImageTk.PhotoImage(person1)
my_img = Label(image = img_per1).place(x=40,y=180)

# IMAGE- PERSON 2
person2 = Image.open("person2.jpeg")
person2 = person2.resize((100, 110), Image.ANTIALIAS)
img_per2 = ImageTk.PhotoImage(person2)
my_img = Label(image = img_per2).place(x=200,y=180)

# IMAGE- PERSON 2
person3 = Image.open("person3.jpeg")
person3 = person3.resize((100, 110), Image.ANTIALIAS)
img_per3 = ImageTk.PhotoImage(person3)
my_img = Label(image = img_per3).place(x=370,y=180)


mainloop()

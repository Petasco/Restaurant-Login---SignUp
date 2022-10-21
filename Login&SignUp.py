from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import Image, ImageTk
import tkinter as tk



class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("LOGIN & SIGN UP")
        self.root.geometry('1366x700+0+0')
        self.root.resizable(False, False)
        self.loginform()

    def loginform(self):
        LoginFrame = Frame(self.root, bg='white')
        LoginFrame.place(x=0, y=0, height=700, width=1366)
        self.img = ImageTk.PhotoImage(file='en75-hero.jpg')
        img = Label(LoginFrame, image=self.img)
        img.place(x=0, y=0, width=1366, height=700)
        frame_input = Frame(self.root, bg='white')
        frame_input.place(x=320, y=130, height=450, width=350)

        loginlbl = Label(frame_input, text='LOGIN', font=('impact', 30, 'bold'), fg='black', bg='white')
        loginlbl.place(x=120, y=20)
        usernamelbl = Label(frame_input, text='Username', font=('Goudy old style', 18, 'bold'), fg='orangered',
                            bg='white')
        usernamelbl.place(x=30, y=95)
        self.UsernameEntry = Entry(frame_input, font=('times new roman', 15, 'bold'), bg='lightgray')
        self.UsernameEntry.place(x=30, y=145, width=270, height=35)

        Passwwordlbl = Label(frame_input, text='Password', font=('Goudy old style', 18, 'bold'), fg='orangered',
                             bg='white')
        Passwwordlbl.place(x=30, y=195)
        self.password = Entry(frame_input, font=('times new roman', 16, 'bold'), bg='lightgray', show='.')
        self.password.place(x=30, y=245, width=270, height=35)

        def Checkfxn():
            try:
                if CheckBtnVar.get() == 1:
                    self.password.config(show='')
                else:
                    self.password.config(show='.')
            except Exception as es:
                messagebox.askretrycancel('Oops!',f'Error due to {str(es)}! Please try again')

        CheckBtnVar = IntVar()
        self.CheckBtn = Checkbutton(frame_input, text='Show Password', font=('times new roman', 10, 'bold'), bd=0,
                                    bg='white', command=Checkfxn, onvalue=1, offvalue=0, variable=CheckBtnVar)
        self.CheckBtn.place(x=30, y=280)

        loginbtn = Button(frame_input, text='Login', font=('times new roman', 15), command=self.login, cursor='hand2',
                          fg='white', bg='orangered', bd=0, width=15, height=1)
        loginbtn.place(x=90, y=340)

        btn1 = Button(frame_input, text='Forget Password?', cursor='hand2', font=('calibri', 10), bg='white',
                      fg='black', bd=0)
        btn1.place(x=125, y=305)

        signupbtn = Button(frame_input, text='New Here? Sign Up', command=self.Register, font=('calibri', 10),
                           bg='white', fg='black', bd=0, cursor='hand2')
        signupbtn.place(x=110, y=390)

    def login(self):
        if self.UsernameEntry.get() == "" or self.password.get() == "":
            messagebox.showerror("Error!", "All fields Required!", parent=self.root)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='Rock1844', database='python')
                cur = con.cursor()
                username = self.UsernameEntry.get()
                password = self.password.get()
                sql = "select * from register where username = %s and password =%s"
                cur.execute(sql, [(username), (password)])
                results = cur.fetchall()

                if results:
                    messagebox.showinfo('Success', 'Login Successful')
                    self.gallery()
                    # self.appscreen()
                    con.close()
                else:
                    messagebox.showerror('Error', 'Incorrect Password or Username')

            except Exception as es:
                messagebox.showerror('Error', f'Error due to : {str(es)}', parent=self.root)

    def Register(self):

        Frame_login1 = Frame(self.root, bg='white')
        Frame_login1.place(x=0, y=0, height=700, width=1366)

        self.img = ImageTk.PhotoImage(file='en75-hero.jpg')
        Label(Frame_login1, image=self.img).place(x=0, y=0, height=700, width=1366)

        frame_input2 = Frame(self.root, bg='white')
        frame_input2.place(x=320, y=130, height=450, width=630)

        label1 = Label(frame_input2, text='Register Here', font=('impact', 32, 'bold'), fg='black', bg='white')
        label1.place(x=180, y=20)

        Usernamelabel2 = Label(frame_input2, text='Useranme', font=('Goudy old style', 20, 'bold'), fg='orangered',
                               bg='white')
        Usernamelabel2.place(x=30, y=95)
        self.UsernameEntry = Entry(frame_input2, font=('times new roman', 15, 'bold'), bg='lightgray')
        self.UsernameEntry.place(x=30, y=145, width=270, height=35)

        Passwordlabel3 = Label(frame_input2, text='Email', font=('Goudy old style', 20, 'bold'), fg='orangered',
                               bg='white')
        Passwordlabel3.place(x=30, y=195)
        self.PasswordEntry2 = Entry(frame_input2, font=('times new roman', 15, 'bold'), bg='lightgray')
        self.PasswordEntry2.place(x=30, y=245, width=270, height=35)

        label4 = Label(frame_input2, text='Password', font=('Goudy old style', 20, 'bold'), fg='orangered', bg='white')
        label4.place(x=330, y=95)
        self.entry3 = Entry(frame_input2, font=('times new roman', 15, 'bold'), bg='lightgray', show='*')
        self.entry3.place(x=330, y=145, width=270, height=35)

        label5 = Label(frame_input2, text='Confirm Password', font=('Goudy old style', 20, 'bold'), fg='orangered',
                       bg='white')
        label5.place(x=330, y=195)
        self.entry4 = Entry(frame_input2, font=('times new roman', 15, 'bold'), bg='lightgray', show='*')
        self.entry4.place(x=330, y=245, width=270, height=35)

        def ReShow_Password():
            try:

                if checkvar.get() == 1:
                    self.entry3.config(show='')
                    self.entry4.config(show='')
                else:
                    self.entry4.config(show='.')
                    self.entry3.config(show='.')
            except Exception as es:
                messagebox.askretrycancel('Oops!',f'Error due to {str(es)}! Please try again')

        checkvar = IntVar()
        checkbtn = Checkbutton(frame_input2, font=('times new roman', 10, 'bold'), text='Show Password',
                               command=ReShow_Password, onvalue=1, offvalue=0, variable=checkvar, bd=0, bg='white')
        checkbtn.place(x=330, y=280)

        SignUpbtn2 = Button(frame_input2, command=self.register, text='Sign Up', cursor='hand2',
                            font=('times new roman', 15), fg='white', bg='orangered',
                            bd=0, width=15, height=1)
        SignUpbtn2.place(x=250, y=340)

        btn3 = Button(frame_input2, command=self.loginform, cursor='hand2', font=('calibri', 10),
                      text='Already Register? Login', fg='black', bg='white', bd=0)
        btn3.place(x=260, y=390)

    def register(self):
        if self.UsernameEntry.get() == '' or self.PasswordEntry2.get() == '' or self.entry3.get() == '' or self.entry4.get() == '':
            messagebox.showerror("Error", 'All fields required!', parent=self.root)
        elif self.entry3.get() != self.entry4.get():
            messagebox.showerror("Error", "Passwords Mismatch!", parent=self.root)
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='Rock1844', database='python')
                cur = con.cursor()
                cur.execute('select * from Register where email=%s', self.entry3.get())
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", 'User already exist! Please try with different email')
                else:
                    cur.execute('insert into Register values(%s,%s,%s,%s)', (
                        self.UsernameEntry.get(), self.PasswordEntry2.get(), self.entry3.get(), self.entry4.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success!", 'Registration Successful', parent=self.root)
                    self.gallery()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root)



    def gallery(self):
        Frame_login = Frame(self.root, bg='white')
        Frame_login.place(x=0, y=0, height=700, width=1366)

        lbl1 = Label(Frame_login, text='Code With Petasco', font=('algerian', 20), fg='black', bg='white')
        lbl1.place(x=375, y=100)
        logoutbtn = Button(Frame_login, text='Logout->', command=self.loginform, cursor='hand2',
                           font=('times new roman', 15), fg='white', bg='orangered',
                           bd=0, width=15, height=1)
        logoutbtn.place(x=1000, y=10)

        self.img = ImageTk.PhotoImage(file='pple.jpg')
        Label(Frame_login, image=self.img).place(x=50, y=0, height=200, width=300)
        self.img1 = ImageTk.PhotoImage(file='Restaurant.jpg')
        Label(Frame_login, image=self.img1).place(x=400, y=0, height=200, width=300)
        self.img2 = ImageTk.PhotoImage(file='South-Africa-restaurants-level-1-Covid-19.jpg')
        Label(Frame_login, image=self.img2).place(x=50, y=250, height=200, width=300)
        self.img3 = ImageTk.PhotoImage(file='The-Most-Expensive-Restaurants-In-The-World.jpg')
        Label(Frame_login, image=self.img3).place(x=400, y=250, height=200, width=300)
root = Tk()
ob = Login(root)
root.mainloop()

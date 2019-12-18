from tkinter import *
from tkinter import messagebox
import getpass
import os
import re
import smtplib, ssl

win = Tk()
win.geometry("1500x1000")
label = Label(win,text = "Login",font=("arial bold",50))
u_email = Label(win,text = "Email-ID:")
u_email.place(x=645,y=235)
label.place(x=675,y=150)
txt = Entry(win,width = 20)
txt1 = Entry(win,width = 20)
txt.place(x=700,y=235)
txt1.place(x=700,y=265)
password = Label(win,text = "password:")
password.place(x=645,y=265)

def email_validation(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showinfo("Email error","Please enter correct email id!")
        return False
    else:
        return True
def pass_validation(passw):
    if len(passw) < 6:
        messagebox.showinfo("Password error","Password should not be less than 6 characters!")
        return False
    else:
        return True
def login():
    e_v_res = email_validation(txt.get())
    p_res = pass_validation(txt1.get())
    if e_v_res and p_res == True:
        messagebox.showinfo("Sucssesful","Logged in succesfully")
        
def create_new_account():
    def account_creation_check():
        def con_pass_check(n_pass,n_cpass):
            if n_pass != n_cpass:
                messagebox.showinfo("Confirmation error","The passwords that you entered didn't matched!")
                return False
            else:
                return True
        
        def email_validation(email):
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                messagebox.showinfo("Email error","Please enter correct email id!")
                return False
            else:
                return True
        def pass_validation(passw):
            if len(passw) < 6:
                messagebox.showinfo("Password error","Password should not be less than 6 characters!")
                return False
            else:
                return True
        def login():
            e_v_res = email_validation(n_email1.get())
            p_res = pass_validation(n_pass1.get())
            pass_check = con_pass_check(n_pass1.get(),n_cpass1.get())
            if e_v_res and p_res and pass_check == True:
                messagebox.showinfo("Sucssesful","Logged in succesfully")
        login()
        
    cna = Tk()
    cna.geometry("1500x1000")
    u_name = Label(cna,text = "user name:")
    u_name.place(x = 700,y = 100)
    u_name1 = Entry(cna,width = 20)
    u_name1.place(x = 770,y = 100)
    n_email = Label(cna,text = "Email:")
    n_email.place(x = 726,y=130)
    n_email1 = Entry(cna,width = 20)
    n_email1.place(x = 770,y = 130)
    n_pass = Label(cna,text = "password:")
    n_pass.place(x = 706,y = 160)
    n_pass1 = Entry(cna,width = 20)
    n_pass1.place(x = 770,y = 160)
    n_cpass = Label(cna,text = "confirm password:")
    n_cpass.place(x = 660,y = 190)
    n_cpass1 = Entry(cna,width = 20)
    n_cpass1.place(x = 770,y = 190)
    sub1 = Button(cna,text = "Submit",command = account_creation_check)
    sub1.place(x = 770,y = 220)
    cna.mainloop()
    
def password_alternative():
    pa = Tk()
    pa.geometry("1500x1000")
    otp_notice = Label(pa,text = "You will recieve an email with an otp\nDo not share the otp with anyone\nThe otp will be availabel only for 3 minutes.")
    otp_notice.place(x = 650,y = 100)
    otp_email = Entry(pa,width = 20)
    otp_email.place(x = 725,y = 170)
    otp_email1 = Label(pa,text = "Enter email:")
    otp_email1.place(x = 650,y = 170)
    def otp(v_mail):
        otp = otp_email.get()[0:7]
        otp = map(str,[ord(c) for c in otp])
        otp = "".join(otp)
        otp = otp[0:6]
        return otp
    def vms():
        otp1 = otp(otp_email.get())
        def verification_mail_sending(otp1,v_email):
            port = 587  
            smtp_server = "smtp.gmail.com"
            sender_email = "emailtesting78459@gmail.com"  
            receiver_email = v_email 
            password = "emailtest123"
            message ="\
            Subject: Hi there\nLooks like you have forgotten your password.\nUse this"+otp1+" otp to log in alternatively do not share this otp with anyone."

            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_server, port) as server:
                server.ehlo()  
                server.starttls(context=context)
                server.ehlo()  
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
        verification_mail_sending(otp1,otp_email.get())
    get_otp = Button(pa,text = "Get OTP",command = vms)
    get_otp.place(x = 750, y = 200)
    pa.mainloop()
    
sub = Button(win,text = "Submit",command = login)
sub.place(x = 730,y=295)
c_n_a = Button(win,text = "Create new account",command = create_new_account)
fg_pass = Button(win,text = "Forgot your password?",command = password_alternative)
c_n_a.place(x = 600,y = 400)
fg_pass.place(x = 800,y = 400)
win.mainloop()

#Python
import smtplib, sqlite3


def sendMailUpdate():
    frUsr = str(input("please input your username!     "))
    pswd = str(input("please input your password!     "))
    toUsr = str(input("please input your the desired recipient!     "))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(frUsr, pswd)

    msg = "You Have Mail!!"
    server.sendmail(frUsr, toUsr, msg)
    server.quit()

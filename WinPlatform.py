import smtplib
import wmi
import time
import os
import webbrowser
import socket

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
c = wmi.WMI()
date = time.strftime("%d_%b_%Y | %H:%M:%S")
file = "Daftar Nama Karyawan.xlxs"
usb = "USB Satu"
my_system = c.Win32_ComputerSystem()[0]
hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname)   
print("Your Computer Name is: " + hostname)   
print("Your Computer IP Address is: " + IPAddr)  
print(f"Name: {my_system.Name}")
print(f"IP Local: {IPAddr}")
print(f"Flashdisk yang di dicolok: {usb}")
print(f"File yang di klik: {file}")
print(f"Di klik pada tanggal: {date}")

mail_content1=(f"Name: {my_system.Name}\n")
mail_content2=(f"SystemUsername: {os.getlogin()}\n")
mail_content3=(f"IP Local: {IPAddr}\n")
mail_content4=(f"Flashdisk yang di dicolok: {usb}\n")
mail_content5=(f"File yang di klik: {file}\n")
mail_content6=(f"Di klik pada tanggal: {date}")

#The mail addresses and password
sender_address = 'sender@gmail.com' #Enter email sender
sender_pass = 'passemailsender' #Enter the password email sender
receiver_address = ['receiver@gmail.com'] #Enter the recipient's email
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = ", ".join(receiver_address)
message['Subject'] = 'Flashdisk baru saja terdeteksi'   #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content1, 'plain'))
message.attach(MIMEText(mail_content2, 'plain'))
message.attach(MIMEText(mail_content3, 'plain'))
message.attach(MIMEText(mail_content4, 'plain'))
message.attach(MIMEText(mail_content5, 'plain'))
message.attach(MIMEText(mail_content6, 'plain'))
#Create SMTP session for sending the mail
# session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls() #enable security
smtpserver.ehlo()
smtpserver.login(sender_address,sender_pass)
#session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
smtpserver.sendmail(sender_address, receiver_address, text)
smtpserver.quit()
print('Mail Sent')

url='https://i.ibb.co/CMwcKdj/Screenshot-20230223-152155.png(url)'
webbrowser.open(url)

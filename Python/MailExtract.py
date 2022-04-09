# Extract Mail
import imaplib
import email
from datetime import date


username = "fsattacker247@gmail.com"
password = "FS123456789"

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(username, password)

mail.select("inbox")

result, data = mail.uid('search', None, "ALL")

inbox_item = data[0].split()

for log in inbox_item:
    result2, email_data = mail.uid('fetch', log, '(RFC822)')
    raw_email = email_data[0][1].decode("utf-8")
    email_message = email.message_from_string(raw_email)
    from_ = email_message['From']
    if from_ == username:
        email_string = str(email_message)
        email_split = email_string.split("\n")
        with open("log.txt", "a") as f:
            f.write(str(email_split[11:-1]))
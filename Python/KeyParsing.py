import json
from operator import contains

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
    for i in range(len(data)):
        for char in data[i]:
            if char in numList:
                print (f"POSSIBLE PW: {data[i]}")
                for n in range(1,trail + 1):
                    print (f"n - {n}", data[i - n])           
import pandas
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
load_dotenv()

appPassword = os.getenv("appPassword")
print(appPassword)

formResponses = pandas.read_csv("Secret Santa | Section B ONLY!.csv")

names = formResponses['Name'].tolist()
emails = formResponses['Username'].tolist()


# EMAIL SERVER
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login('system.growpal@gmail.com', appPassword)
    print("Successfully Connected To SMTP Gmail Server")

except:
    print("EMAIL SERVER PROBLEM")




# allocating santa
shuffledNames = names.copy()
continu = 0
recipient = []
while(continu == 0):
    redo = False
    shuffledNames = names.copy()
    for i in range(0, len(names)):
        recip = random.randint(0, len(shuffledNames) - 1)
        x = 0
        while(x == 0):
            if(names[i] == shuffledNames[recip]):
                if(len(shuffledNames) == 1):
                    redo = True
                    x = 1
                else:
                    recip = random.randint(0, len(shuffledNames) - 1)
            else:
                x = 1
        if(redo != True):
            recipient.append(shuffledNames[recip])
            shuffledNames.pop(recip)
            continu = 1
        else:
            continu = 0







for i in range(len(emails)):
    nameToSend = recipient[i]
    emailToSendTo = emails[i]
    msg = "\r\n".join([
                "From: system.growpal@gmail.com",
                f"To: {emailToSendTo}",
                "Subject: Your Secret Santa Name!",
                "",
                f'''Hi! Here's the name you got for secret santa: {nameToSend}. The Maximum Budget is 200 rupees. Happy Gifting!
                '''
                ])
    try:
        server.sendmail('system.growpal@gmail.com', emailToSendTo, msg)
        print(f"Sent mail to {emailToSendTo}!")
    except:
        print("trying to send mail again...")
        try: 
            server.sendmail('system.growpal@gmail.com', emailToSendTo, msg)
        except:
            print(f"Failed to send mail to {emailToSendTo}. They got the name {nameToSend}. Inform Them Please")
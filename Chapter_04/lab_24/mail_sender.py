import smtplib as mailto
import random

message_schema = '''
From: {}
Subcject: {}
-------------------------------------
Content: "{}"
-------------------------------------
Email from mail sender by Kamil
'''


def create_new_message (_from="", _subcject="", _body=""):
    message = str(message_schema).format(_from, _subcject, _body)
    return message


def send_to_gmail(user, password, _to, message):
    
    id = random.randint(0, 10000000)
    
    try:
        server = mailto.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, _to, message)
        server.close()
        print("Mail id: {} is sent !\n {}".format(id, message))
    except:
        print("Error ! mail id: {} is not send !\n {}".format(id, message))


#! Don't forget ! Code in your account must be secret
message = create_new_message("Kamil", "Invitation", "Hello guys.")
send_to_gmail("kamil.cecherz@gmail.com", "*******", ['kamil.cecherz@gmail.com'], message)
    
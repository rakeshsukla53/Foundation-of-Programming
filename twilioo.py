__author__ = 'rsukla'


from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account

account_sid = "AC976f8a49a80efa6b3080e7316a43376e"

auth_token = "e6104b2455da83f764bf4b48565374e6"

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Happy New Year",

to="+13024385450", # Replace with your phone number

from_="+13024070522") # Replace with your Twilio number

print message.sid


import client
import time

#instantiaion
the_server = client.Server()

print('Welcome, to the chat client sender!')

#registering for a username
while True:
    user = input('your name: ')
    if the_server.check_user(user):
        break
    print('sorry! already taken')
  
while True:
    content = input('> ')
    the_server.send_message(user, content)
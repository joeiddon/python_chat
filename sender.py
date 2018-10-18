import client
import time

SERVER_ADDR = 'http://10.1.129.49:12345/'

#instantiaion
the_server = client.Server(SERVER_ADDR)

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
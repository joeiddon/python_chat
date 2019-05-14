import client
import time

#https://docs.python.org/3.0/library/urllib.request.html
#"the HTTP request will be a POST instead of a GET when the data parameter is provided"

SERVER_ADDR = 'http://10.1.130.6:12345/'

#instantiaion
the_server = client.Server(SERVER_ADDR)

print('Welcome, to the chat client reciever!')

num_recieved_messages = 0
while True:
    messages = the_server.get_messages()
    for message in messages[num_recieved_messages:]:
        print(f'{message.user}: {message.content}')
    num_recieved_messages = len(messages)
    time.sleep(1)
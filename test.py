from send import send
from receive import receive


def handle_message(ch, method, properties, body):
    global password
    password = body.decode('utf-8')


send()


receive(handle_message)


print(password)

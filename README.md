A. How to REQUEST data from this microservice:
- To request data from this microservice, make sure to clone this respository into your project.
- Then, import the 'send' function from send.py into the file for which you are calling the microservice from.
- Then, call the 'send' function like this: send()
- This will send the request to the microservice and begin the process of generating your password.

B. How to RECEIVE data from this microservice:
- To receive data from this microservice, import the 'receive' function from receive.py into the file in which you would like to receive the data.
- Then, declare a callback function that you will call the receive function with as an argument.
  - For example:
    def handle_message(ch, method, properties, body):
      global password
      password = body.decode('utf-8')
  - In this callback function, we are receiving the data that is sent back from the microservice and assigning it to the password variable.
  - We have to decode the password from binary to utf-8 so that the data is readable.
- The generated password will be available in the password variable.

C. UML Sequence Diagram:
<img width="837" alt="Screenshot 2024-02-26 at 8 34 55 PM" src="https://github.com/brantsai/password-recovery/assets/91583948/86921865-d620-4aa5-b0a4-21e3e3c9798d">

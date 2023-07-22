# Client Server
This is the end module assignment for the CSCK541 Software Development in Practice module
The application is a simple client/server network that is able to:

 - Create a dictionary, populate it, serialize it and send it to a server.
 - Create a text file and send it to a server.
 - With the dictionary, the user should be able to set the pickling format to one of the following: binary, JSON and XML. Also, the user will need to have the option to encrypt the text in a text file.
 
The server should have a configurable option to print the contents of the sent items to the screen and or to a file. Also, the server will need to be able to handle encrypted contents.

## Generate your Encryption Key
`import base64
import os

base64.urlsafe_b64encode(os.urandom(32))`

## Usage
Open a terminal or command prompt.
Navigate to the directory where you saved the server.py file.
Run the server script by executing the following command:

`python server.py`

This will start the server and it will start listening for incoming connections on the specified port.

Open another terminal or command prompt.
Navigate to the directory where you saved the client.py file.
Run the client script by executing the following command:

`python client.py`

This will start the client program.

The client will prompt you with options to send a dictionary or a text file to the server. Follow the prompts and enter the required information to send the data to the server.
You can run the server and client on the same machine by opening two separate terminals or command prompts and following the steps above in each terminal.
If you want to run the server and client on different machines, make sure you update the HOST variable in both scripts with the appropriate IP address or hostname of the machine where the server is running. Additionally, you may need to adjust any firewall settings to allow communication between the machines on the specified port.

Remember to adjust the PORT variable in both scripts if you want to use a different port for communication.

## Running Unit Tests


## Running Performance Tests


## TODO
 - Enable encryption / decryption
 - Write unit tests
 - fix bugs 


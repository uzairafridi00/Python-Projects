# python3 !
# method_2.py - This code snippet simply By Pass the Antivirus Software 

# This technique is used for hacking and other malicious purposes to avoid anti-virus
# software detecting as a malware.

# <----- USE IT FOR EDUCATIONAL PURPOSES ----->

from cryptography.fernet import Fernet
import base64

# 'b' denotes Byte data
code = b"""   

# All your code goes in here.  

import socket 
import threading
import pickle
import os
import ..........

a = 5
b = c
c = a + b

# Continue your code...

"""

# It will generate an encrypted key
key = Fernet.generate_key()
# Get the encrypted key
encryption_type = Fernet(key)
# Encrypt Your code
encrypted_message = encryption_type.encrypt(code)

# Now decrypt your code
decrypted_message = encryption_type.decrypt(encrypted_message)

# Now execute it
exec(decrypted_message)
# Python3 !
# passwordChecker.py - This Code snippet check validity of Strong Password

import re


def passwordChecker(password):
    reg = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$'

    # Compile Regex
    p = re.compile(reg)

    # searching regex
    mat = re.search(p, password)

    # validating condition
    if mat:
        print("Password is Valid.")
    else:
        print("Password is Invalid.")


# Driver Code
if __name__ == "__main__":
    passwordChecker('Dummy12@')  # Valid
    passwordChecker('dummy12')   # Invalid


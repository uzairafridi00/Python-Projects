# python3 !
# emailChecker.py - This code snippet simply check the validation of email addresses

import re  # Using regex library


def validateEmail(email):
    regex_email = re.compile(r'''
                             ^([a-z0-9_\.-]+)    # local part
                             @                   # single @ sign
                             ([0-9a-z\.-]+)      # Domain name
                             \.                  # single dot
                             ([a-z{2,6}])$       # Top level domain
                             ''', re.VERBOSE | re.IGNORECASE)

    # RegexObject is matched with the desired pattern
    # string using fullmatch function
    # In case a match is found, search()
    # returns a MatchObject Instance
    res = regex_email.fullmatch(email)

    if res:
        print("{} is VALID Email Address".format(email))
    else:
        print("{} is InValid Email Address".format(email))


# Main Function to run the program
if __name__ == "__main__":
    validateEmail("dummy@email.com")  # Valid Email Address Format
    validateEmail("dummy@.com")       # Invalid Email Address Format
    validateEmail("dummy@email.com@") # Invalid Email Address Format

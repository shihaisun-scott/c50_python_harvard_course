# goal is to check if the email is valid or not

email = input("What's your email? ").strip()

# this is okay but need to check a lot of arguments
# username, domain = email.split("@")
# if username and "." in domain:
#     print("Valid")
# else:
#     print("Invalid")

# this is a better version using re (regular expression)
import re

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
# notes:
# r is for raw string; good practice to use
# ^ is the start; $ is the end
# \w is for all word characters and numbers and _: same as [a-zA-Z0-9_]
# ? is optional; can or cannot be there
# + is 1 or more of that thing
# @ for the 
# \. for the raw . (else it would be none or more of that character)


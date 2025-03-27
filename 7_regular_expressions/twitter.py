# get username from twitter url

import re

url = input("URL: ").strip()

# the non preferred version
# username = url.removeprefix("https://twitter.com/", "")

# version 1 using sub
# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "") # sub for substitute
# print(f"Username: {username}")

# version 2 using search to capture the username
if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE): # sub for substitute
    print(f"Username: {matches.group(1)}")

# notes
# no $ for the end because we do not want the end
# ? by itself is to make it optional
# ?: is to not extract
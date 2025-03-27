# format input name into name then last name
import re

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$"): # everything in the parenthesis will be extracted into matches.group
    last, first = matches.groups()
    name = f"{first} {last}"
    # can also do:
    # name = matches.group(1) + " " + matches.group(2)
print(f"Hello, {name}")

# notes for matches := re.search(r"^(.+), *(.+)$"):
# := is for the if statement and also assigning the value
# ' *' is to remove the whitespaces

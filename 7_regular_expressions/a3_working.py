# convert 12-hour time to 24-hour time

import re
import sys

# 9:00 AM to 5:00 PM
# 9 AM to 5 PM
# 9:00 AM to 5 PM
# 9 AM to 5:00 PM

def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^(\d+(?::\d+)?) (\w+) to (\d+(?::\d+)?) (\w+)$", s):
        x, xx, y, yy = matches.groups()
        if ":" in x:
            xhh, xmm = x.split(":")
            xhh = int(xhh)
            xmm = int(xmm)
        else:
            xhh = int(x)
            xmm = 0
        if ":" in y:
            yhh, ymm = y.split(":")
            yhh = int(yhh)
            ymm = int(ymm)
        else:
            yhh = int(y)
            ymm = 0
        if not 1 <= xhh <= 12 or not 1 <= yhh <= 12 or not 0 <= xmm <= 59 or not 0 <= ymm <= 59:
            return "ValueError"
        if xhh == 12 and xx == "AM":
            xhh = 0
        if yhh == 12 and yy == "AM":
            yhh = 0
        
        # now convert the time
        if xx == "AM":
            time1 = f"{xhh:02}:{xmm:02}"
        elif xx == "PM":
            time1 = f"{xhh+12:02}:{xmm:02}"
        if yy == "AM":
            time2 = f"{yhh:02}:{ymm:02}"
        elif yy == "PM":
            time2 = f"{yhh+12:02}:{ymm:02}"

        return f"{time1} to {time2}"
            
    else:
        return "ValueError"


...


if __name__ == "__main__":
    main()
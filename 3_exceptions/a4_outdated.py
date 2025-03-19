def main():
    date = convert_date("Date: ")
    print(date)

def convert_date(prompt):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    while True:
        text = input(prompt).strip().title()
        if "/" in text:
            mm, dd, yy = text.split("/")
            mm = int(mm)
            dd = int(dd)
            yy = int(yy)
            if 1 <= mm <= 12 and 1 <= dd <= 31:
                return f"{yy}/{mm:02}/{dd:02}"        
        else:
            mm, dd, yy = text.split(" ")
            if "," in dd:
                if mm in months:
                    mm = months.index(mm.title()) + 1
                    dd = int(dd.removesuffix(","))
                    yy = int(yy)
                    if 1 <= mm <= 12 and 1 <= dd <= 31:
                        return f"{yy}/{mm:02}/{dd:02}"   
                
main()


        
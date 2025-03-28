# print DOB in minutes

from datetime import date, timedelta
import inflect
import sys

def main():
    print(date_minutes(input("Enter your DOB (YYYY-MM-DD): ")))
    


def date_minutes(s):
    try: 
        dob = date.fromisoformat(s)
        today = date.today()

        diff = today - dob
        days = diff.days
        minutes = days * 24 * 60
        p = inflect.engine()
        s = p.number_to_words(minutes, andword="")
        return f"{s.capitalize()} minutes"
    
    except ValueError:
        sys.exit()



if __name__ == "__main__":
    main()
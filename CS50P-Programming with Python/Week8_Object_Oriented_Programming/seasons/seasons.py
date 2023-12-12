from datetime import date
import sys
import re
import inflect


def main():
    dob = getting_date()
    minutes_alive = getting_minutes(dob)
    minutes_to_words_result = minutes_to_words(minutes_alive)
    print(f"{minutes_to_words_result}")


def getting_date():
    date_of_birth = input("Date of birth: ")
    if re.search(r"^\d{4}-\d{2}-\d{2}$",date_of_birth):
        date_of_birth = date_of_birth.split("-")
        dob = date(int(date_of_birth[0]), int(date_of_birth[1]), int(date_of_birth[2]))
        return dob
    else:
        sys.exit("Invalid date")


def getting_minutes(dob):
    date_of_today = date.today()
    days_alive = date_of_today - dob
    minutes_alive = days_alive.days * 24 * 60
    return (minutes_alive)

def minutes_to_words(minutes):
    p = inflect.engine()
    minutes_str = p.number_to_words(int(minutes),andword = "")
    return minutes_str.capitalize() + " minutes"

if __name__ == "__main__":
    main()

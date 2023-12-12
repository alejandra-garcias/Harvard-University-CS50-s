from seasons import getting_date, getting_minutes,minutes_to_words
import pytest
from datetime import date

def main():
    test_getting_minutes()


def test_getting_minutes():
    dob = date(2023, 12, 12)
    minutes = getting_minutes(dob)
    assert minutes == 0



if __name__ == "__main__":
    main()

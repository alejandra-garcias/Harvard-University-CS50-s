from working import convert
import pytest

def main():
    test_format()
    test_time()
    test_wrong_hour()

def test_format():
    assert convert("10:30 AM to 02:45 PM") == "10:30 to 14:45"
    with pytest.raises(ValueError):
        convert('10AM - 10PM')
    with pytest.raises(ValueError):
        convert('10:60 AM to 18 PM')

def test_time():
    assert convert("10:30 AM to 02:45 PM") == "10:30 to 14:45"

def test_wrong_hour():
    with pytest.raises(ValueError):
        convert('17 PM to 18 PM')




if __name__ == "__main__":
    main()

from numb3rs import validate

def main():
    test_validate()

def test_validate():
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("10.255.1.4") == True
    assert validate("-4.255.255.255") == False
    assert validate("265.265.265.265") == False
    assert validate("24.265.265.265") == False
    assert validate("2554,5.255,15.25,5.2,55") == False



if __name__ == "__main__":
    main()

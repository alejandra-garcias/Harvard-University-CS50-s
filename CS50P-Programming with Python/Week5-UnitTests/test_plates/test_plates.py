from plates import is_valid

def main():
    test_length()
    test_start_with_2_letters()
    test_numbers_together()
    test_zero()
    test_symbols()

def test_length():
    assert is_valid("AA") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

def test_start_with_2_letters():
    assert is_valid("A4") == False
    assert is_valid("2A") == False
    assert is_valid("11") == False

def test_numbers_together():
    assert is_valid("AAA111") == True
    assert is_valid("AA1A11") == False

def test_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_symbols():
    assert is_valid("AG5.97") == False



if __name__ == "__main__":
    main()


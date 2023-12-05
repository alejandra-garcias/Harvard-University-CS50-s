from bank import value

def main():
    test_value()

def test_value():
    assert value("h") == 20
    assert value("hello") == 0
    assert value("What's up") == 100
    assert value("It's Friday 3rd") == 100
    assert value("Hello 3") == 0
    assert value("Hiya") == 20
    assert value("HELLO") == 0




if __name__ == "__main__":
    main()

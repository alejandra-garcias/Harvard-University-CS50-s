from jar import Jar


def test_init():
    jar_default = Jar()
    assert jar_default.capacity == 12
    assert jar_default.size == 0
    jar_custom_capacity = Jar(capacity=8)
    assert jar_custom_capacity.capacity == 8


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
     jar = Jar(capacity=10)
     assert jar.size == 0
     jar.deposit(5)
     assert jar.size == 5

def test_withdraw():
    jar = Jar(capacity=7)
    assert jar.size == 0
    jar.deposit(4)
    assert jar.size == 4

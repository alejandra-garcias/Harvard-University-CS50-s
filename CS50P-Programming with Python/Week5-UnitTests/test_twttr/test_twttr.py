from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten("hola") == "hl"
    assert shorten("twitter") == "twttr"
    assert shorten("como estas") == "cm sts"
    assert shorten("Hola que tal estas") == "Hl q tl sts"
    assert shorten("llevo 2 dias trabajando") == "llv 2 ds trbjnd"
    assert shorten("Hola, mundo") == "Hl, mnd"
    assert shorten("SI") == "S"





if __name__ == "__main__":
    main()

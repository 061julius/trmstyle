from trmstyle import Color, color

def test_red():
    result = color("Hello", Color.FORE_RED)

    assert "Hello" in result
    assert Color.FORE_RED in result
    assert Color.RESET in result
    
    print("Test passed.")

if __name__ == '__main__':
    test_red()

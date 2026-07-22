from trmstyle import rainbow_text, Color

def test_rainbow_chars():
    result = rainbow_text("abc")

    assert 'a' in result
    assert 'b' in result
    assert 'c' in result
    assert Color.RESET in result

    print("Test passed.")

if __name__ == '__main__':
    test_rainbow_chars()

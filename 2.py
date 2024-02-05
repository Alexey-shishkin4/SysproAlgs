def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    m = max(len(str(x)), len(str(y))) // 2
    high1, low1 = divmod(x, 10 ** m)
    high2, low2 = divmod(y, 10 ** m)

    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    z2 = karatsuba(high1, high2)

    return (z2 * 10 ** (2 * m)) + ((z1 - z2 - z0) * 10 ** m) + z0


def test_karatsuba():
    result = karatsuba(123, 456)
    assert result == 123 * 456

    result = karatsuba(12345678901234567890, 98765432109876543210)
    assert result == 12345678901234567890 * 98765432109876543210

    result = karatsuba(12345, 6789012345)
    assert result == 12345 * 6789012345

    result = karatsuba(0, 987654321)
    assert result == 0

    result = karatsuba(-123, 456)
    assert result == -123 * 456

    print("all tests passed!")


test_karatsuba()

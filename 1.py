def division(dividend, divisor):
    quotient = 0
    current_dividend = 0
                                                                                     # время  кол-во операций
    for i in str(dividend):                                                          # с1     n
        current_dividend = current_dividend * 10 + int(i)                            # c2     n

        current_quotient = 0                                                         # c3     n
        current_remainder = 0                                                        # c4     n
        for j in range(1, 10):                                                       # c5     9 * n
            if current_dividend - (j * divisor) < 0:                                 # c6     9 * n
                current_quotient = j - 1                                             # c7     9 * n
                current_remainder = current_dividend - (current_quotient * divisor)  # c8     9 * n
                break                                                                # c9     9 * n
            if current_dividend - (j * divisor) == 0:                                # c10    9 * n
                current_quotient = j                                                 # c11    9 * n
                current_remainder = 0                                                # c12    9 * n
                break                                                                # c13    9 * n

        current_dividend = current_remainder                                         # c14    n
        quotient = quotient * 10 + current_quotient                                  # c15    n

    return quotient, current_remainder
# T(n) = n * (c1 + c2 + c3 + c4 + 9*c5 + 9*c6 + 9*c7 + 9*c8 + 9*c9 + 9*c10 + 9*c11 + 9*c12 + 9*c13 + c14 + c15) = nd, d > 0
# T(n) = O(n)

# лучший: O(n) - на 10 строке надо зайти ровно 1 раз для каждой цифры из dividend
# худший: O(9n) = O(n) - для каждого делимого перебрать все числа из [1, 9]

dividend = 2713919314930
divisor = 123242
result_quotient, result_remainder = division(dividend, divisor)
print(f"целая часть: {result_quotient} остаток: {result_remainder}")
#print(dividend // divisor, dividend % divisor)

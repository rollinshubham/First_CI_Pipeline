def is_armstrong(number):
    if number < 0:
        return False

    original = number

    # Count the number of digits
    digits = 0
    temp = number

    if temp == 0:
        digits = 1
    else:
        while temp > 0:
            digits += 1
            temp //= 10

    # Calculate the sum of each digit raised to that count
    total = 0
    temp = number

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == original
def is_prime(number):
    for i in range(2, number):
        print(i)
        if number % (i * i) == 0:
            return False
        else:
            return True
    if number == 1:
        return False
    return number


number = int(input("Enter a number: "))

if is_prime(number):
    print(number,"소수가 맞습니다")
else:
    print(number,"소수가 아닙니다")

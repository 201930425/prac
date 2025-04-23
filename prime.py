number = int(input("Enter a number: "))
is_prime = True

for i in range(2, number):
    print(i)
    if number % (i*i) == 0:
        is_prime = False
        break


if number == 1:
    is_prime = False

if is_prime:
    print(number,"소수가 맞습니다")
else:
    print(number,"소수가 아닙니다")

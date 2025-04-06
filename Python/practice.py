num = 2
while num <= 100:
    prime_number = True
    i = 2
    while i <= (num // 2):
       
        if num % i == 0:
            prime_number = False
            break
        i += 1
    if prime_number:
        print(num, end=' ')
    num += 1

def prime_checker(number) :
    i =  2
    is_prime = True
    while i < number:
        if number % i == 0:
            is_prime = False
        i += 1  
    if is_prime:
        print("It is prime")
    else:
        print("It is Not Prime")
        
n = int(input("Check this number: "))
prime_checker(n)
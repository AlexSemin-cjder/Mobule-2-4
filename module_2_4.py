numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

primes = []
not_primes = []

for num in numbers:
    Flag = True
    for divider in range(2, num):
        if num % divider == 0:
            Flag = False
            not_primes.append(num)
            break
            
    if Flag == True and num !=1:
          primes.append(num)
          
print(primes)  
print(not_primes)             
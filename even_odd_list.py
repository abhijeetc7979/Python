num = int(input('Enter up to what number you want list of even numbers: - '))
even_list = []
odd_list = []
prime_list = []
for i in range(1, num+1):
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

for num in range(2, num):
    if num > 1:
        for i in range (2,num):
            if (num % i) == 0:
                break
        else:
            prime_list.append(num)

print(f"list of even numbers upto {num} is {even_list}")
print(f"list of odd numbers upto {num} is {odd_list}")
print(f"list of prime numbers upto {num} is {prime_list}")
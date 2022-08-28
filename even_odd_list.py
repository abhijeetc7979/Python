num = int(input("Enter up to what number you want list of even numbers: - "))
even_list = []
odd_list = []
prime_list = []
for i in range(1, num + 1):
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

for i in range(2, num):
    if i % 2:
        prime_list.append(i)

print(even_list)
print(odd_list)
print(prime_list)

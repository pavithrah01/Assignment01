numbers = tuple(input("Enter series of numbers"))
even_count = 0
odd_count = 0
print(numbers)
for i in numbers:
    if int(i)%2 == 0:
        even_count += 1
    else:
        odd_count += 1
print('Number of even numbers:', even_count)
print('Number of odd numbers:', odd_count)

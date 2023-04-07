n = int(input("Enter the number of terms in sequence"))
a = 0
b = 1
count = 0
if n <= 0:
    print("Nothing to generate")
elif n == 1:
    print("Series upto",n,':',+a)
else:
    print("Fibonacci sequence upto",n,"are:")
    while count < n:
        print(a)
        value = a + b
        a = b
        b = value
        count += 1

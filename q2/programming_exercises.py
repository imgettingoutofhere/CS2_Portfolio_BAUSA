# Exercise 1: Count Even Numbers
for i in range(2, 21, 2):
    print(i)

# Exercise 2: The Countdown Timer
count = 10

while count >= 1:
    print(count)
    count -= 1

print("Time is up!")

# Exercise 3: Skip Multiples
for i in range(1, 16):
    if i % 3 == 0:
        continue
    print(i)

# Exercise 4: Multiplication Table Generator
def show_table(number):
    for i in range(1, 11):
        print(number * i)

num = int(input("Enter a number: "))
show_table(num)


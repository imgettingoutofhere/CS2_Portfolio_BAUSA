# 1. Sum of Numbers Using a For Loop
def getSum(limit):
    if limit < 1:
        print("Invalid input.")
        return

    total = 0
    for i in range(1, limit + 1):
        total += i

    print("Sum:", total)
    print("Correct?", total == limit * (limit + 1) // 2)

try:
    num = int(input("Enter a positive number: "))
    getSum(num)
except:
    print("Invalid input.")

# 2. Password Validation Using a While Loop and Break
def checkPassword(correctPassword):
    while True:
        enteredPassword = input("Enter your password: ")
        
        if enteredPassword == "":
            print("Invalid input! Password cannot be blank.")
            continue
        elif enteredPassword == correctPassword:
            print("Welcome! Access granted.")
            break
        else:
            print("Incorrect password. Try again.")

checkPassword("kumsaytwo123")

# 3. Displaying Number Patterns Using Nested Loops
def verifyPattern(generatedRows, generatedColumns, rows, columns):
    if generatedRows == rows and generatedColumns == columns:
        print("Pattern verified.")
    else:
        print("Pattern verification failed.")

def displayPattern(rows, columns):
    if rows <= 0 or columns <= 0:
        print("Invalid input!")
        return

    for i in range(rows):
        for j in range(1, columns + 1):
            print(j, end=" ")
        print()

    verifyPattern(i + 1, j, rows, columns)

try:
    r = int(input("Enter rows: "))
    c = int(input("Enter columns: "))
    displayPattern(r, c)
except:
    print("Invalid input!")

# 4. Skipping Multiples Using the continue Keyword
def verifyOutput(skippedCount, expectedSkippedCount):
    if skippedCount == expectedSkippedCount:
        print("Output verified.")
    else:
        print("Output verification failed.")

def skipMultiples(limit):
    if limit <= 0:
        print("Invalid input! Please enter a positive number.")
        return

    skippedCount = 0

    for i in range(1, limit + 1):
        if i % 3 == 0:
            skippedCount += 1
            continue
        print(i)

    expectedSkippedCount = limit // 3
    verifyOutput(skippedCount, expectedSkippedCount)

try:
    limit = int(input("Enter a positive number: "))
    skipMultiples(limit)
  
except ValueError:
    print("Invalid input! Please enter a positive number.")


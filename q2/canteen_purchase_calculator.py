def calculate_total(price, quantity):
    return price * quantity


def calculate_change(payment, total):
    return payment - total


# 1. Input collection
price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
payment = float(input("Enter amount paid: "))

# 2. & 3. Calculate and store total cost
total_cost = calculate_total(price, quantity)

# 4. Calculate change/balance
balance = calculate_change(payment, total_cost)

# 5. & 6. Display results
print(f"Total Cost: PHP {total_cost:.2f}")

if balance >= 0:
    print(f"Change: PHP {balance:.2f}")
else:
    print(f"Insufficient payment. Additional amount needed: PHP {-balance:.2f}")


# DOCUMENTATION ANSWERS

# 1. 'calculate_total' finds the gross cost by multiplying price and quantity and 'calculate_change' finds the financial difference by subtracting the total cost from the customer's payment.

# 2. Parameters are the variable names in the function definition (like 'price'). Arguments are the actual user values passed into the function when running it.

# 3. The total is stored in the 'total_cost' variable. It is reused by being passed into 'calculate_change' and being printed in the receipt.

# 4. Separating functions makes code clean, reusable, and easy to fix. You can modify how total cost is calculated later without breaking the change logic.

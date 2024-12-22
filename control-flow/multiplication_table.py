# multiplication_table.py

# Step 1: Prompt the user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Step 2: Generate and print the multiplication table using a for loop
for i in range(1, 11):  # Loop from 1 to 10
    result = number * i  # Calculate the product
    print(f"{number} * {i} = {result}")  # Print the multiplication table line


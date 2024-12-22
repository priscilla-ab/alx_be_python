# pattern_drawing.py

# Step 1: Prompt the user for the pattern size
size = int(input("Enter the size of the pattern: "))

# Step 2: Use a while loop to print each row
row = 0
while row < size:
    # Use a for loop to print asterisks on the same line
    for col in range(size):
        print("*", end="")
    
    # After printing each row, move to the next line
    print()
    
    # Move to the next row
    row += 1


# age.py

# Ask the user for their current age
current_age = int(input("Enter your age: "))

# Calculate future ages
for i in range(10, 50, 10):
    future_age = current_age + i
    print(f"In {i} years, you will be {future_age} years old.")

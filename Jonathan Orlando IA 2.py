# Problem 1: Temperature Conversion and Water State

# Prompt user to enter temperature in Fahrenheit
temperature_fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius using the formula: (F - 32) * 5/9
temperature_celsius = (temperature_fahrenheit - 32) * 5/9

# Display the converted temperature in Celsius with 1 decimal place
print(f"Temperature in Celsius: {temperature_celsius:.1f}")

# Determine the state of water based on Celsius temperature
# Water is ice at or below 0 degrees Celsius
if temperature_celsius <= 0:
    print("Ice")
# Water is liquid between 0 and 100 degrees Celsius (exclusive of 100)
elif temperature_celsius > 0 and temperature_celsius <= 100:
    print("Liquid")
# Water is gas above 100 degrees Celsius
else:
    print("Gas")

# Print empty line to separate Problem 1 and Problem 2 outputs
print()

# Problem 2: Delivery Cost Calculator

# Prompt user to enter the number of packages to ship
num_packages = int(input("Enter # of packages to ship: "))

# Prompt user to choose shipping type: regular (r) or express (e)
shipping_type = input("Enter r for regular, e for express: ")

# Determine the shipping rate based on user's choice
# Regular shipping costs $10 per package
if shipping_type == "r":
    rate = 10
# Express shipping costs $15 per package
elif shipping_type == "e":
    rate = 15
# Handle invalid input by defaulting to regular shipping
else:
    rate = 10
    print("Invalid input, defaulting to regular shipping")

# Calculate total cost: number of packages multiplied by rate per package
total_cost = num_packages * rate

# Display the total cost with US currency formatting
print(f"Total cost: $ {total_cost}")
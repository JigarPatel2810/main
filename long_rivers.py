# Create a list of river dictionaries
rivers = [
    {"name": "Nile", "length": 4157},
    {"name": "Yangtze", "length": 3434},
    {"name": "Murray-Darling", "length": 2310},
    {"name": "Volga", "length": 2290},
    {"name": "Mississippi", "length": 2540},
    {"name": "Amazon", "length": 3915}
]

# Task 1: Print out each river's name using a for loop
print("Task 1:")
for river in rivers:
    print(river["name"])

# Task 2: Calculate and print the total length of all the rivers
print("\nTask 2:")
total_length = 0
for river in rivers:
    total_length += river["length"]
print("Total length of all rivers:", total_length, "miles")

# Extension 1: Print out every river's name that begins with the letter 'M'
print("\nExtension 1:")
m_rivers = []
for river in rivers:
    if river["name"][0] == "M":
        m_rivers.append(river["name"])
print("Rivers whose names start with 'M':", ", ".join(m_rivers))

# Extension 2: Print out every river's length in kilometers
print("\nExtension 2:")
conversion_factor = 1.6  # 1 mile is roughly 1.6 kilometers
for river in rivers:
    length_km = river["length"] * conversion_factor
    print(river["name"], "- Length:", length_km, "km")

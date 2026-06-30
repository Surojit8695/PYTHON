
# Build a program that determines how long it will take
# to empty a swimming pool

length = 12
width = 7
height = 2

flow_rate = 17   # cubic meters per hour

# Calculate volume of pool
volume = length * width * height

# Calculate time required
time = volume / flow_rate

print("The volume of the swimming pool is:", volume, "cubic meters")
print("The time required to empty the swimming pool is:", round(time, 2), "hours")

# Exercise 4: Apollo

import matplotlib.pyplot as plt
import numpy as np
import math as m

#Ta'Nasia Coleman: I opened up the data file and put the data into a dictionary
# Open the Apollo 10 ascent-phase data file
with open("as-505-ascent-phase-data.txt", "r") as data_file:
    flight_data = data_file.readlines()

# Select the section containing the data and headers
flight_data = flight_data[12:136]

# Get the names of the headers from the text file
header_names = flight_data[0].replace(" ", "").strip("\n").split(",")
units = flight_data[1].replace(" ", "").strip("\n").split(",")
print(units)
# Initilize the variable to store the numerical flight data
numerical_data = []

#Getting the flight data by first checkig if the very first index has . which will let me know that its a number
for data_row in flight_data:
    row_values = data_row.replace(" ", "").strip("\n").split(",")

    if "." in row_values[0]:
        numerical_data.append(list(map(float, row_values)))
    else:
        continue

# Create a dictionary containing each parameter and its data
flight_data_dict = dict(zip(header_names, zip(*numerical_data)))

print(flight_data_dict)

#Now make a plot with each parameter as a function of time

for i, header in enumerate(header_names[1:], start=1):
    fig, ax = plt.subplots(figsize=(9,5))
    ax.plot(flight_data_dict['TIME'], flight_data_dict[header])
    ax.set_title(f"Flight Data: {header}")
    ax.set_xlabel("Time (SEC)")
    ax.set_ylabel(f"{header}  ({units[i]})")
plt.show()




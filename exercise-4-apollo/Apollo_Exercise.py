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

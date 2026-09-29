# Exercise 4: Apollo

import matplotlib.pyplot as plt
import numpy as np
import math as m
from matplotlib.collections import LineCollection

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


######## By Shreyas Dhumal #######
horizontal_coord = flight_data_dict['LONG']
vertical_coord = flight_data_dict['GCLAT']
altitude_coord = flight_data_dict['ALTITUDE']

# https://matplotlib.org/stable/gallery/lines_bars_and_markers/multicolored_line.html (multicolor lines )
fig2, ax2 = plt.subplots()
# for whole map
# map_img = plt.imread("NE1_50M_SR_W_1080.png")
# #ax2.imshow(map_img, extent=[-180, 180, -90, 90])     #  https://matplotlib.org/stable/users/explain/artists/imshow_extent.html

#for cropped
map_img = plt.imread("NE1_50M_SR_W_CROPPED_1080.png")
ax2.imshow(map_img, extent=[-120, -30, 15, 60])
ax2.set_aspect('equal')

point_pairs = np.array([horizontal_coord, vertical_coord]).T.reshape(-1, 1, 2)   #it'll make pair and transpose the horizontal array
segments = np.concatenate([point_pairs[:-1], point_pairs[1:]], axis=1)
line = LineCollection(segments, cmap='plasma')     # this will create the line and assign color 
line.set_array(np.array(altitude_coord))
line.set_linewidth(2)

ax2.add_collection(line)
#  for whole map
# ax2.set_xlim(-180, 180)
# ax2.set_ylim(-90, 90)

#for cropped
ax2.set_xlim(-120, -30)
ax2.set_ylim(15, 60)

ax2.set_xlabel("Longitude")
ax2.set_ylabel("Latitude")
ax2.set_title("Apollo 10 Groundtrack")
colour_bar = fig2.colorbar(line, ax=ax2)
colour_bar.set_label("Altitude")

plt.show()


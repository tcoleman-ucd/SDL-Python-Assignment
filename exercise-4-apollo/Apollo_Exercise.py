# Exercise 4: Apollo

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection

# Ta'Nasia Coleman: I opened up the data file and put the data into a dictionary
# Open the Apollo 10 ascent-phase data file
with open("as-505-ascent-phase-data.txt", "r") as data_file:
    flight_data = data_file.readlines()

# Select the section containing the data and headers
start_line = 12
end_line = 136
flight_data = flight_data[start_line:end_line]

# Get the names of the headers from the text file
header_names = flight_data[0].replace(" ", "").strip("\n").split(",")
units = flight_data[1].replace(" ", "").strip("\n").split(",")
print(units)
# Initialize the variable to store the numerical flight data
numerical_data = []

# Getting the flight data by first checking if the very first index has. which will let me know that it's a number
for data_row in flight_data:
    row_values = data_row.replace(" ", "").strip("\n").split(",")

    if "." in row_values[0]:
        numerical_data.append(list(map(float, row_values)))
    else:
        continue

# Create a dictionary containing each parameter and its data
flight_data_dict = dict(zip(header_names, zip(*numerical_data)))

for row in numerical_data[:5]:
    print(row)

# Now make a plot with each parameter as a function of time

for i, header in enumerate(header_names[1:], start=1):
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(flight_data_dict["TIME"], flight_data_dict[header])
    ax.set_title(f"Flight Data: {header}")
    ax.set_xlabel("Time (SEC)")
    ax.set_ylabel(f"{header}  ({units[i]})")



######## By Shreyas Dhumal ####### (Improved version)

horizontal_coord = flight_data_dict["LONG"]
vertical_coord = flight_data_dict["GCLAT"]
altitude_coord = flight_data_dict["ALTITUDE"]

# References used to get multicolor lines and for plots:
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/multicolored_line.html
# https://matplotlib.org/stable/api/figure_api.html#matplotlib.figure.Figure.colorbar
# https://matplotlib.org/stable/api/collections_api.html#matplotlib.collections.LineCollection

# Loading the maps
whole_map = plt.imread("maps/NE1_50M_SR_W_1080.png")
cropped_map = plt.imread("maps/NE1_50M_SR_W_CROPPED_1080.png")

fig_whole, ax_whole = plt.subplots(figsize=(10, 6), layout="constrained")
fig_cropped, ax_cropped = plt.subplots(figsize=(10, 6), layout="constrained")

# To display the maps
# Reference used: https://matplotlib.org/stable/users/explain/artists/imshow_extent.html
ax_whole.imshow(whole_map, extent=(-180, 180, -90, 90))
ax_whole.set_aspect("equal")

ax_cropped.imshow(cropped_map, extent=(-120, -30, 15, 60))
ax_cropped.set_aspect("equal")

point_pairs = np.array([horizontal_coord, vertical_coord]).T.reshape(-1, 1, 2)  # This will make pair and transpose the horizontal array
segments = np.concatenate([point_pairs[:-1], point_pairs[1:]], axis=1)   # This will calculate segments for each altitude

line = LineCollection(segments, cmap="plasma")  # this will create the line and assign color
line.set_array(np.array(altitude_coord))
line.set_capstyle("round")
line.set_linewidth(2.5)

line2 = LineCollection(segments, cmap="plasma")
line2.set_array(np.array(altitude_coord))
line2.set_capstyle("round")
line2.set_linewidth(2.5)

#  for whole map
ax_whole.set_xlim(-180, 180)
ax_whole.set_ylim(-90, 90)
ax_whole.add_collection(line)
ax_whole.set_xlabel("Longitude")
ax_whole.set_ylabel("Latitude")
ax_whole.set_title("Apollo 10 Groundtrack")
colour_bar = fig_whole.colorbar(line, ax=ax_whole, shrink=0.75, fraction=0.045, pad=0.03)
colour_bar.set_label("Altitude")

# for cropped
ax_cropped.set_xlim(-120, -30)
ax_cropped.set_ylim(15, 60)
ax_cropped.set_ylim(15, 60)
ax_cropped.add_collection(line2)
ax_cropped.set_xlabel("Longitude")
ax_cropped.set_ylabel("Latitude")
ax_cropped.set_title("Apollo 10 Groundtrack")
colour_bar = fig_cropped.colorbar(line2, ax=ax_cropped, shrink=0.75, fraction=0.045, pad=0.03)
colour_bar.set_label("Altitude")

plt.show()

################################# END ##############################################

######## By Shreyas Dhumal ####### (Old version)
# # https://matplotlib.org/stable/gallery/lines_bars_and_markers/multicolored_line.html (multicolor lines )
# fig_whole, ax_whole = plt.subplots()
# fig_cropped, ax_cropped = plt.subplots()
# # for whole map
# whole_map = plt.imread("NE1_50M_SR_W_1080.png")
# ax_whole.imshow(whole_map, extent=[-180, 180, -90, 90])  #  https://matplotlib.org/stable/users/explain/artists/imshow_extent.html
#
# # for cropped
# cropped_map = plt.imread("NE1_50M_SR_W_CROPPED_1080.png")
# ax_cropped.imshow(cropped_map, extent=[-120, -30, 15, 60])
# ax_cropped.set_aspect("equal")
#
# point_pairs = np.array([horizontal_coord, vertical_coord]).T.reshape(-1, 1, 2)  # it'll make pair and transpose the horizontal array
# segments = np.concatenate([point_pairs[:-1], point_pairs[1:]], axis=1)
# line = LineCollection(segments, cmap="plasma")  # this will create the line and assign color
# line.set_array(np.array(altitude_coord))
# line.set_linewidth(2)
# line2 = LineCollection(segments, cmap="plasma")  # this will create the line and assign color
# line2.set_array(np.array(altitude_coord))
# line2.set_linewidth(2)
#
#
# #  for whole map
# ax_whole.set_xlim(-180, 180)
# ax_whole.set_ylim(-90, 90)
# ax_whole.add_collection(line)
#
# ax_whole.set_xlabel("Longitude")
# ax_whole.set_ylabel("Latitude")
# ax_whole.set_title("Apollo 10 Groundtrack")
#
#
# # for cropped
# ax_cropped.set_xlim(-120, -30)
# ax_cropped.set_ylim(15, 60)
# ax_cropped.add_collection(line2)
#
# ax_cropped.set_xlabel("Longitude")
# ax_cropped.set_ylabel("Latitude")
# ax_cropped.set_title("Apollo 10 Groundtrack")
# colour_bar = fig2.colorbar(line, ax=ax2)
# colour_bar.set_label("Altitude")
#
# plt.show()

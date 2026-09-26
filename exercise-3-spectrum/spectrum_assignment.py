#Excersize 3 Ta'Nasia Coleman


##### By Shreyas Dhumal Code added till data separation of wavelength and flux #####
import matplotlib.pyplot as plt
import numpy as np
with open("spectrum.txt", 'r') as spectrum_file:
    spectrum_data = spectrum_file.readlines()

wavelength_list = []
flux_list = []
is_data_reached = False
for line in spectrum_data:
    line = line.strip()        #It'll remove next line jump in readline
    if line == "# DATA":
        is_data_reached = True   #this will tell the loop do operations after Data line is reached 
        continue
    if is_data_reached:
        if line == "WAVELENGTH,FLUX":      
            continue
        wavelength_list.append(float(line.split(",")[0]))
        flux_list.append(float(line.split(",")[1]))

############## - ###########

###Ta'Nasia work

#plot Flux vs wavelength
fig, ax = plt.subplots(figsize=(9,5))
ax.plot(wavelength_list, flux_list)
ax.set_xlabel(r"Wavelength ($\AA$)")
ax.set_ylabel("Flux (ADU)")
plt.title("Spectrum Plot")

plt.show()
#plot of flux vs wavelength with fitted curve
max_fl = max(flux_list) #Need to find the emission line/max flux and then remove it from the list to plot the polynomial
index = np.where(flux_list == max_fl)
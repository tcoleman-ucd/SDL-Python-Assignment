#Excersize 3 Ta'Nasia Coleman


##### By Shreyas Dhumal Code added till data separation of wavelength and flux #####
import matplotlib.pyplot as plt
import numpy as np
import math as m
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

#Valeria Trijueque
#Low-order polynomial
coefficients = np.polyfit(wavelength_list, flux_list, deg=1) #polynomial coefficiens
new_flux_list = []#start list for new flux list
for val in wavelength_list:    
    #print(coefficients)
    y = coefficients[0]*val + coefficients[1] # calculate fitted flux
    new_flux_list.append(y) #store the values
    #print(y)

amplitude = max(flux_list) #amplitude
amplitude_index = flux_list.index(amplitude) #index at which the amplitude is max, peak
wavelength_at_peak = wavelength_list[amplitude_index] # wavelength at peak

mean = np.mean(flux_list) #calculate the mean of flux
sum=0
for val in flux_list:
    sum += (val + mean)**2 
    
standard_deviation = np.sqrt(sum/len(flux_list)) #calculate standard deviation
##Another way of calculating the standard deviaiton
# mean1 = 0
# for v in flux_list:
#     mean1 += v
#     mean2 = sqrt(mean1/len(flux_list))
# print(mean2)

gaucian_distribution = [] # calculate gaucian disctribution
for flux,wave  in zip(new_flux_list,wavelength_list):
    gaucian = amplitude*m.exp(-((wave-wavelength_at_peak)**2)/(2*standard_deviation**2))+flux
    gaucian_distribution.append(gaucian)

#Calculate uncertinty (THIS IS NOT CORRECT)
# n = len(flux_list)
# #uncertinty= 0
# for b in gaucian_distribution:
    
#     uncertinty = np.sqrt((b+mean)**2/(n*(n-1)))
   
#     print(uncertinty)

###Ta'Nasia work

#plot Flux vs wavelength
fig, ax = plt.subplots(figsize=(9,5))
fig, ax1 = plt.subplots(figsize=(9,5))
ax.plot(wavelength_list, flux_list)
ax.plot(wavelength_list, new_flux_list)
ax1.plot(wavelength_list, gaucian_distribution)
ax.set_xlabel(r"Wavelength ($\AA$)")
ax.set_ylabel("Flux (ADU)")
plt.title("Spectrum Plot")

plt.show()
#plot of flux vs wavelength with fitted curve
max_fl = max(flux_list) #Need to find the emission line/max flux and then remove it from the list to plot the polynomial
#index = np.where(flux_list == max_fl)
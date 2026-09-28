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
coefficients,cov = np.polyfit(wavelength_list, flux_list,deg=1, cov=True) #polynomial coefficiens
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

# gaucian_distribution = [] # calculate gaucian disctribution
# for flux,wave  in zip(new_flux_list,wavelength_list):
#     gaucian = amplitude*m.exp(-((wave-wavelength_at_peak)**2)/(2*standard_deviation**2))+flux
#     gaucian_distribution.append(gaucian) #curve fit 
#https://www.geeksforgeeks.org/python/python-gaussian-fit/
#x =np.asarray(flux_list)
#c_0 = np.asarray(new_flux_list)
#y =np.asarray(wavelength_list)
from scipy.optimize import curve_fit
#define the function of the gaussian distribution of the peak
def gaussian(x,A, mu, sigma):#, c_0):
    return A*np.exp(-((x-mu)**2)/(2*sigma**2))#+c_0)) # formula

x = np.asarray(wavelength_list)#convert the list of values into an np array
y = np.asarray(flux_list)

wavelength_list_peak = x[(x>6680) &(x<6700)]#select only the peak
flux_list_peak = y[(x>6680) &(x<6700)]

#use curve_fit to optain the optimal parameters from the initial parameters (which are very acurate)
par1,par2 = curve_fit(gaussian,wavelength_list_peak, flux_list_peak, p0=[amplitude, wavelength_at_peak, standard_deviation])

#create a line that fits around the peak(with the selection of threshold done above and the gaussian)
curvex = np.linspace(min(wavelength_list_peak), max(wavelength_list_peak),2878)
curvey = gaussian(curvex,*par1)

#calculate the uncertinties of the parameters doing the square of the diagonal
uncertainties = np.sqrt(np.diag(par2))
print(uncertainties)
uncertainties2 = np.sqrt(np.diag(cov))
print(uncertainties2)

#Calculate uncertinty (THIS IS NOT CORRECT)
# n = len(flux_list)
# #uncertinty= 0
# for b in gaucian_distribution:
    
#     uncertinty = np.sqrt((b+mean)**2/(n*(n-1)))
   
#     print(uncertinty)

#######by shreyas####### 
# Hard coding the peak region
# approx_peak_center = wavelength[np.argmax(flux)]   #as prof said, we can take a line for the center and consider approx value around it
# print(approx_peak_center)
# lower_limit = approx_peak_center - 10                  # 20 is random guess
# upper_limit = approx_peak_center + 10
# is_masked = []
# for value in wavelength:                               # it'll give True if these values are not in peak
#     if value < lower_limit or value > upper_limit:
#         is_masked.append(True)
#     else:
#         is_masked.append(False)
# coefficients = np.polyfit(wavelength[is_masked], flux[is_masked], deg=1)
# new_flux_list = np.polyval(coefficients, wavelength)

###Ta'Nasia work
plt.close("all")
#plot Flux vs wavelength
fig, ax = plt.subplots(figsize=(9,5))
fig, ax1 = plt.subplots(figsize=(9,5))
ax1.plot(wavelength_list, flux_list)
ax.plot(wavelength_list_peak, flux_list_peak)
ax1.plot(wavelength_list, new_flux_list)

ax.plot(curvex, curvey)
ax.set_xlabel(r"Wavelength ($\AA$)")
ax.set_ylabel("Flux (ADU)")
plt.title("Spectrum Plot")

plt.show()
#plot of flux vs wavelength with fitted curve
max_fl = max(flux_list) #Need to find the emission line/max flux and then remove it from the list to plot the polynomial
#index = np.where(flux_list == max_fl)

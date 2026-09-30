#Excersize 3 Ta'Nasia Coleman


##### By Shreyas Dhumal Code added till data separation of wavelength and flux #####
import matplotlib.pyplot as plt
import numpy as np
import math as m
from scipy.optimize import curve_fit
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
x = np.asarray(wavelength_list)
y = np.asarray(flux_list)

def fit_line(x, a, b):
    return a*x+b

popt, pcov = curve_fit(
    fit_line,
    x,
    y,
    p0=[1, 1],
    bounds=[
        (-5, 0), # lower bounds for each parameter 
        (10, 1e9)  # upper bounds for each parameter
    ]
)
line = fit_line(x, *popt)

sub = y - line

xpeak = x[(x>6670) &(x<6750)] #select only the peak
ypeak = sub[(x>6670) &(x<6750)]


amplitude = max(flux_list) #amplitude
amplitude_index = flux_list.index(amplitude) #index at which the amplitude is max, peak
wavelength_at_peak = wavelength_list[amplitude_index] # wavelength at peak

mean = np.mean(flux_list) #calculate the mean of flux
sum=0
for val in flux_list:
    sum += (val + mean)**2 
    
standard_deviation = np.sqrt(sum/len(flux_list)) #calculate standard deviation

FMHW = standard_deviation*2.355
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


#define the function of the gaussian distribution of the peak
def gaussian(x,A, mu, sigma):#, c_0):
    return A*np.exp(-((x-mu)**2)/(2*sigma**2))#+c_0)) # formula

#y1 = gaussian(x, amplitude,wavelength_at_peak, standard_deviation)

#y_total = y1+line


#sub = x-popt[0]
#wavelength_list_peak = x[(x>6680) &(x<6700)]#select only the peak
#flux_list_peak = y[(x>6680) &(x<6700)]

#y_true = gaussian(x, amplitude, wavelength_at_peak, standard_deviation)

#y_data = y_true + y

gopt, gcov = curve_fit(gaussian, xpeak, ypeak, p0=[amplitude, wavelength_at_peak, standard_deviation])

y_fit = line + gaussian(x, *gopt)
#calculate the uncertinties of the parameters doing the square of the diagonal
uncertainties = np.sqrt(np.diag(pcov))
print(uncertainties)
uncertainties2 = np.sqrt(np.diag(gcov))
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

ax1.plot(wavelength_list, line)
ax.plot(wavelength_list, flux_list)
ax.plot(x, y_fit)
ax.set_xlabel(r"Wavelength ($\AA$)")
ax.set_ylabel("Flux (ADU)")
plt.title("Spectrum Plot")

plt.show()
#plot of flux vs wavelength with fitted curve
max_fl = max(flux_list) #Need to find the emission line/max flux and then remove it from the list to plot the polynomial
#index = np.where(flux_list == max_fl)

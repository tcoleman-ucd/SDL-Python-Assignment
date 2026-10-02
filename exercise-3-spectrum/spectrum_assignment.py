#Excersize 3 

##### By Shreyas Dhumal Code added till data separation of wavelength and flux #####
import matplotlib.pyplot as plt
import numpy as np
import math as m
import sys
import argparse
from scipy.optimize import curve_fit

def main(filename):
    with open(filename, 'r') as spectrum_file:
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

    ##### By Valeria Trijueque - Fit a low-order polynomial and fit gaussian to the emission peak

    #Fit low-order polynomial:
    x = np.asarray(wavelength_list) #convert the wavelengths list into a numpy array
    y = np.asarray(flux_list) #convert the flux list into a numpy array

    def fit_line(x, a, b): #define the low-order polynomial function
        return a*x+b 

    #Optain the best-fit parameters and their uncertinties using curve_fit
    popt, pcov = curve_fit(
        fit_line,
        x,
        y,
        p0=[1, 1],
    )

        
    line = fit_line(x, *popt) #fit line

    sub = y - line # substract the polynomial fit line and the raw data lo leave the background noise and the emission peak

    #select only the peak
    xpeak = x[(x>6670) &(x<6750)] 
    ypeak = sub[(x>6670) &(x<6750)]

    #Compute the initial parameters
    amplitude = max(flux_list) #amplitude
    amplitude_index = flux_list.index(amplitude) #index amplitude, peak
    wavelength_at_peak = wavelength_list[amplitude_index] #wavelength at peak

    #calculate the standard deviation of the flux
    mean = np.mean(flux_list) 
    sum=0
    for val in flux_list:
        sum += (val + mean)**2 
        
    standard_deviation = np.sqrt(sum/len(flux_list)) 

    ##Another way of calculating the standard deviaiton
    # mean1 = 0
    # for v in flux_list:
    #     mean1 += v
    #     mean2 = sqrt(mean1/len(flux_list))
    # print(mean2)


    #https://www.geeksforgeeks.org/python/python-gaussian-fit/
    #https://www.youtube.com/watch?v=peBOquJ3fDo


    #define the function for the gaussian fit:
    def gaussian(x,A, mu, sigma):
        return A*np.exp(-((x-mu)**2)/(2*sigma**2))
    #Where A is the amplitude, x is the raw flux data, mu is the position of the center of the peak, and sigma**2 is the variance

    #Obtain the best fit parameters from the gaussian fit and their uncertinties
    gopt, gcov = curve_fit(gaussian, xpeak, ypeak, p0=[amplitude, wavelength_at_peak, standard_deviation])

    y_fit = line + gaussian(x, *gopt) #bring the baseline of the gaussian to the spectrum baseline using the polynomial fit line 

    FMHW = gopt[2]*2.355 #full-width at half-maximum

    #Print the best fit parameters from the gaussian and polynomial
    print(f"The best fit amplitude is {gopt[0]}")
    print(f"The best fit central wavelength of the peak is {gopt[1]}")
    print(f"The best fit FWHM is {FMHW}")

    print(f"The slope of the low order polynomial is {popt[0]}")
    print(f"The y-intercept of the low order polynomial is {popt[1]}")

    #calculate the uncertinties of the parameters doing the square of the diagonal
    uncertainties = np.sqrt(np.diag(gcov))
    FMHWuncertainty = uncertainties[2]*2.355
    print(f"The uncertainty of the amplitude is {uncertainties[0]}")
    print(f"The uncertainty of the central wavelength of the peak is {uncertainties[1]}")
    print(f"The uncertainty of the FWHM is {FMHWuncertainty}")
    uncertainties_poly = np.sqrt(np.diag(pcov))
    print(f"The uncertainty of the slope is {uncertainties_poly[0]}")
    print(f"The uncertainty of the y-intercept is {uncertainties_poly[1]}")


    #### By Ta'Nasia - plot the spectrum
    plt.close("all")
    #plot Flux vs wavelength
    fig, ax = plt.subplots(figsize=(9,5))
    fig, ax1 = plt.subplots(figsize=(9,5))
    fig, ax2 = plt.subplots(figsize=(9,5))

    ax.plot(wavelength_list, flux_list)
    ax1.plot(wavelength_list, flux_list)
    ax1.plot(wavelength_list, line, 'g-')
    ax2.plot(wavelength_list, flux_list)
    ax2.plot(wavelength_list, line,'g-')
    ax2.plot(wavelength_list, y_fit,'r-')
    ax.set_xlabel(r"Wavelength ($\AA$)")
    ax.set_ylabel("Flux (ADU)")
    ax1.set_xlabel(r"Wavelength ($\AA$)")
    ax1.set_ylabel("Flux (ADU)")
    ax2.set_xlabel(r"Wavelength ($\AA$)")
    ax2.set_ylabel("Flux (ADU)")
    ax.set_title("Spectrum Plot")
    ax1.set_title("Spectrum Plot with polynomial fit")
    ax2.set_title("Spectrum Plot with polynomial and gaussian fit")

    plt.show()

if __name__ == '__main__':
    args = sys.argv[1:]
    main(args[0])




# cmb_visualizer.py
# Author: Sahar Dordaei Joghan
# Date: March 2025
# Description:
#     This script visualizes the Cosmic Microwave Background (CMB) temperature
#     anisotropies using the Planck 2018 SMICA map. It uses a Mollweide projection,
#     converts temperatures to microkelvin, prints basic statistics (min, max, mean,
#     std), and saves the resulting full-sky map.

# =================== MIT License ===================
# Copyright (c) 2025 Sahar Dordaei Joghan
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software to use, modify, distribute, and publish with attribution.
# ===================================================


# ==== Import Required Libraries ====
import healpy as hp               # HEALPix: handles spherical maps like the CMB
import numpy as np                # For numerical array and statistics
import matplotlib.pyplot as plt   # For plotting and saving the image

# ==== Step 1: Load the CMB Temperature Map ====
# Make sure your FITS file is renamed to this and placed in the same directory
fits_file = "smica_cmb_map.fits"

# The SMICA FITS file includes several components (I, Q, U, etc.)
# We are only interested in the temperature (I_STOKES), which is field=0
# This loads the temperature values for every pixel in HEALPix format
temperature_map = hp.read_map(fits_file, field=0, verbose=False)

# ==== Step 2: Convert Units to μK (microkelvin) ====
# Planck maps are usually in kelvin (K), but most scientific CMB studies use μK
# So we convert from kelvin to microkelvin: 1 K = 1,000,000 μK
temperature_map_uK = temperature_map * 1e6

# ==== Step 3: Compute and Print Basic Statistics ====
# These statistics are useful for checking the dynamic range of the anisotropies
coldest_temp = np.min(temperature_map_uK)
hottest_temp = np.max(temperature_map_uK)
mean_temp = np.mean(temperature_map_uK)
std_temp = np.std(temperature_map_uK)

# Print values to terminal
print(f"Coldest pixel temperature: {coldest_temp:.3f} μK")
print(f"Hottest pixel temperature: {hottest_temp:.3f} μK")
print(f"Mean temperature: {mean_temp:.3f} μK")
print(f"Standard deviation: {std_temp:.3f} μK")

# ==== Step 4: Display the Full-Sky Temperature Map (Mollweide Projection) ====
# The Mollweide projection is commonly used for all-sky astrophysical maps.
# We fix the color scale range to ±300 μK for consistency with Planck publications.
# The color scale used is 'turbo', which provides high visual contrast and is suitable for CMB visualization:
#     • Blue: Coldest regions (negative ΔT, below average temperature)
#     • Red: Hottest regions (positive ΔT, above average temperature)
#     • Yellow/green: Near-average temperature (ΔT ≈ 0 μK)

hp.mollview(
    temperature_map_uK,              # Map data (in μK)
    title="Planck CMB Temperature Anisotropies (SMICA 2018)",  # Title
    unit="ΔT [μK]",                  # Unit for color bar
    cmap="turbo",                   # Scientifically accepted color scheme
    min=-300, max=300,               # Fix range to ±300 μK
    coord=['G'],                     # Galactic coordinates
    cbar=True                        # Show colorbar
)

# Add galactic coordinate gridlines to map for reference
hp.graticule()

# ==== Step 5: Save the Image ====
# Save the plot to a PNG file (300 dpi for high resolution)
plt.savefig("cmb_temperature_mollweide.png", dpi=300)

# Optional: Show the plot if running interactively (e.g. in Jupyter)
# plt.show()

# Close the plot to free memory (important when generating many images)
plt.close()

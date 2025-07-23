# Planck CMB Temperature Visualizer

A Python tool to visualize the **temperature anisotropies** in the **Cosmic Microwave Background (CMB)** using the **Planck 2018 SMICA map**. This script loads temperature data, converts it to microkelvin, and generates a full-sky **Mollweide projection** commonly used in cosmology.

---

## What It Does

- Loads the SMICA 2018 temperature (I) component from a Planck FITS file.
- Converts from Kelvin to microkelvin for clarity and standardization.
- Prints important statistics: **minimum**, **maximum**, **mean**, and **standard deviation**.
- Plots a full-sky Mollweide projection in **galactic coordinates**.
- Uses a perceptually uniform colormap (`turbo`) for meaningful scientific interpretation.
- Saves the output as a high-resolution PNG.

---

## Files Included

| File                           | Description                                              |
|--------------------------------|----------------------------------------------------------|
| `cmb_visualizer.py`            | Main Python script                                       |
| `cmb_temperature_mollweide.png`| Output image: CMB anisotropy map in μK                   |
| `README.md`                    | Project description and usage guide                      |
| `LICENSE`                      | MIT License                                              |

---

## How to Run

1. **Install Dependencies**

Requires Python 3.10+ with the following libraries:

   ```bash
   pip install healpy numpy matplotlib
   ```

2. **Prepare the FITS File**

   Download the SMICA 2018 full map from the [Planck Legacy Archive](https://pla.esac.esa.int/).  
   Rename the downloaded file to:

   ```
   smica_cmb_map.fits
   ```

   Place it in the same folder as `cmb_visualizer.py`.

3. **Run the Script**

   ```bash
   python3 cmb_visualizer.py
   ```

4. **Result**

   The image `cmb_temperature_mollweide.png` will be saved in your project folder.

---

## Example Output

```text
Coldest pixel temperature: -5755.000 μK
Hottest pixel temperature: 7898.794 μK
Mean temperature: -0.000 μK
Standard deviation: 108.365 μK
```

---

## Scientific Notes

- This visualizes **temperature fluctuations (ΔT)** around the CMB mean temperature of ~2.725 K.
- The map uses **HEALPix** pixelization and **Galactic coordinates**.
- The color scale is fixed to ±300 μK, consistent with Planck publications.
- The `turbo` colormap offers perceptual uniformity and physical interpretability:
  - **Blue** = cooler spots (negative ΔT)
  - **Red** = hotter spots (positive ΔT)
  - **Yellow** = near-average regions

---

## License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute with attribution.

---

## Author

**Sahar Dordaei Joghan**  
Created: March 2025  
Updated: July 2025 (for GitHub Portfolio)

---

## Acknowledgments

- [ESA Planck Mission](https://www.cosmos.esa.int/web/planck)
- [HEALPix and Healpy](https://healpy.readthedocs.io/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)

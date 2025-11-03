Metis Instrument and Data Overview
==================================


### The Metis Instrument
Metis is the multi-wavelength coronagraph for the Solar Orbiter mission. It is designed to simultaneously observe the solar corona in two different wavelengths:
* **Visible Light (VL) channel:** This channel observes the solar corona in polarized white light (K-corona), between 580 and 640 nm, due to the Thomson scattering of photons by the free electrons in the corona
* **Ultraviolet (UV) channel**: The UV channel observes in the Lyman-α line at 121.6 nm, emitted by neutral hydrogen in the extended corona. Note: The same spectral line is observed on-disk by EUI/HRILYA (also onboard Solar Orbiter).


### Metis Data Products and Processing Levels

Metis data is distributed via the Solar Orbiter Archive (SOAR) and follows the standard processing level definitions established for the mission.
Level,Name,Description and Content,Units,Readiness for Analysis
L0,Raw Data,"Uncalibrated, uncompressed data obtained directly from grouped telemetry packets. FITS files contain only basic telemetry header information.",DN (Digital Numbers),No (Diagnostic Use Only)
L1,Engineering Data,"L0 data supplemented with essential metadata, engineering data, and housekeeping telemetry. Data remains uncalibrated.",DN (Digital Numbers),No (Requires Calibration)
L2,Calibrated Science Data,"Data ready for scientific analysis. All necessary corrections applied: bias, dark-current, flat-field, vignetting, exposure normalization, and radiometric calibration. Coordinates are expressed in standard WCS (World Coordinate System).",Physical Units,Yes (Recommended)
L3,Derived Data,"High-level scientific products generated after advanced analysis of L2 data. Includes maps, filtered images, movies, electron density maps, etc.",Derived Physical Units,Yes (Advanced Analysis)
| Level | Name | Description | Units | Readiness for Analysis |
| :--- | :--- | :--- | :--- | :--- | 
| **L0** | Raw Data | Uncalibrated, uncompressed FITS files containing only basic telemetry header information. | DN (Digital Numbers) | No  |
| **L1** | Engineering Data | Uncalibrated data with additional metadata (housekeeping, WCS keywords). | DN (Digital Numbers) | No (intermediate stage). |
| **L2** | Calibrated Science Data | Data ready for scientific analysis; Corrections (bias, dark-current, flat-field, vignetting, exposure normalization, radiometric calibration) are applied. | Physical Units | Yes (Recommended)|
| **L3** | Derived Data | High-level scientific products derived from Level 2 after advanced scientific analysis. | Derived Physical Units | Yes (Advanced products: e.g., electron density maps, solar wind velocity maps, Carrington maps). |

#### Primary L2 Data Products

The Python analysis tools focus heavily on loading these primary Level 2 data types:

* **VL Images:** Polarized Brightness (pB), Total Brightness (tB)Fixed Polarization (FP); Pol-angle, Stokes.
* **UV Images:** Ly-α narrowband images.

### Metis FITS File Naming Convention

All Metis data products are provided in the standard FITS format and follow the ESA/Solar Orbiter file naming convention. Understanding this structure is crucial for querying data programmatically (e.g., using `sunpy.net.Fido`).

The standard format is:

``solo_<LEVEL>_[DESCRIPTOR]_[DATETIME]_V[VERSION].fits``

| Component | Description | Example | Relevance |
| :--- | :--- | :--- | :--- |
| **LEVEL** | Processing level (L1, L2, L3). | `L2` | Determines calibration status. |
| **DESCRIPTOR** | Unique string identifying the data type. | `metis-vl-tB` (VL total brightness) | Required for fetching specific products. |
| **DATETIME** | Timestamp of the data acquisition (UTC). | `20240515T120000` | Used for time-based searching. |
| **VERSION** | Version of the FITS file/pipeline used. | `V01` | Important for reproducible analysis. |

.. note::
    When using the Metis Python Tools, the specific **DESCRIPTOR** is handled internally by functions.  
Python Analysis Functions Overview
==================================

The **Metis Python Tools** are built to streamline data handling, leveraging the power and standards of the SunPy ecosystem. This section introduces the core functionality.

Core Data Handling (The `metis_load` family)
--------------------------------------------

The primary entry points for interacting with Metis data are dedicated loader and fetching routines.

* **Data Loading:** The main function is typically named something like **``metis_load()``**. This function abstracts the complexities of file formats (e.g., FITS files or proprietary formats), returning data as standard SunPy objects (like `~sunpy.map.Map` for images or `~sunpy.timeseries.TimeSeries` for telemetry).

    .. code-block:: python

        from metis_tools import metis_load

        # Load an L1 image file for a specific time
        metis_map = metis_load('2024-05-15T12:00:00')

        # The output object is a standard SunPy Map
        print(type(metis_map))

* **Metadata:** All loaded objects automatically carry essential metadata (WCS coordinates, timestamps, observation details), ensuring compatibility with other SunPy tools.

Visualization and Plotting
--------------------------

Metis tools provide custom plotting functions optimized for coronal data, often building upon Matplotlib.

* **Basic Plotting:** Functions for quick visualization of calibrated images. These often include default color maps (colormaps) and scaling appropriate for Metis data.
    * Example: **``metis_plot_image()``**
* **Advanced Visualization:** Tools for specialized plotting, such as time-series data visualization or plotting data over SunPy's coordinate system framework.

.. note::
    For advanced data analysis and plotting examples, refer to the **Example Gallery** (`auto_gallery/index.rst`) section.

Data Processing and Calibration
-------------------------------

While Level 1 (L1) data is generally calibrated, dedicated Python routines are often provided for user-specific data preparation.

* **Calibration Routines:** Functions for applying custom calibration steps or corrections that are not part of the standard L1 pipeline.
    * Example: **``metis_apply_flatfield()``** or **``metis_derotate()``** (for co-alignment).
* **Unit Conversion:** Tools to convert data between different physical units or coordinate systems.

API Reference
-------------

For detailed parameters, return types, and usage examples for every function:

.. seealso::
    Consult the :doc:`API Reference <../api_reference/index>` for comprehensive technical documentation.
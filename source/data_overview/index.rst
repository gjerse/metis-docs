Metis Data and Analysis Tools
=============================

This section serves as your central resource for understanding the access, structure, and analysis of Solar Orbiter Metis data. Here you will find procedures for downloading data, overviews of the **Python analysis toolkit**, and guidance on **IDL integration**.

.. toctree::
   :maxdepth: 2
   :caption: Analysis Resources

   Data Overview <data_overview>
   Data Access and Download <data_access>
   Python Analysis Functions <analysis_tools>
   Integration of Legacy IDL Tools <idl_tools>



**Key Analysis Workflows**

Use the resources below to navigate your analysis path, from data acquisition to final results.

* **Data Overview** (:doc:`data_overview`)
    A comprehensive introduction to Metis data products, including details on data levels (L0, L1, L2, L3) and the FITS file naming conventions used in the Solar Orbiter Archive (SOAR).

* **Data Access and Download** (:doc:`data_access`)
    This page provides clear instructions and **Python code snippets** for the programmatic download of Metis data from the official SOAR archive using the SunPy FIDO client.

* **Python Analysis Functions** (:doc:`analysis_tools`)
    An overview of the core functionality within the **``metis-tools`` Python package**. Learn about the primary data loader (e.g., ``metis_load()``) and the functions available for visualization and processing, all built to be compatible with the SunPy ecosystem.

* **Integration of Legacy IDL Tools** (:doc:`idl_tools`)
    A crucial guide detailing when and how to utilize **legacy IDL routines**. It explains the method for safely importing IDL output files (``.sav``) into the Python environment for final analysis and publication-ready plotting, minimizing interruptions to your Python workflow.
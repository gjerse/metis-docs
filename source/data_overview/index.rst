Metis Data and Analysis Tools
=============================

This section is your central resource for understanding, accessing, and
analyzing **Solar Orbiter Metis data** in Python. It covers:

- data products and processing levels;
- FITS structure and naming conventions;
- programmatic data access from the SOAR archive;
- the core ``metis-tools`` Python package;
- integration with legacy IDL routines.

Use the pages below to follow a typical analysis workflow: from data discovery
and download, to loading, processing, and visualization.


How to use this section
-----------------------

If you are:

**New to Metis data**

- Start with :doc:`products_and_levels` to understand data levels, products, and FITS
  structure.
- Then go to :doc:`data_access` to learn how to find and download data from
  SOAR.

**Ready to analyze data in Python**

- Go directly to :doc:`analysis_tools` for an overview of the ``metis-tools``
  package and typical workflows.
- Browse the :doc:`../auto_gallery/index` for reproducible examples.

**Using or migrating from IDL**

- See :doc:`idl_tools` for guidance on using legacy IDL routines and importing
  ``.sav`` files into Python.


Key analysis workflows
----------------------

**Data Overview** (:doc:`products_and_levels`)  
A comprehensive introduction to Metis data products, including:

- data levels (L0, L1, L2, L3) and their scientific meaning;
- FITS file naming conventions used in the Solar Orbiter Archive (SOAR);
- key header keywords and metadata.

**Data Access and Download** (:doc:`data_access`)  
Instructions and **Python code snippets** for programmatically downloading
Metis data from the official SOAR archive using the SunPy ``Fido`` client and
the ``sunpy-soar`` plug‑in.

**Python Analysis Functions** (:doc:`analysis_tools`)  
An overview of the core functionality in the ``metis-tools`` Python package:

- the main data loader (e.g. ``metis_load()``);
- utilities for visualization and basic processing;
- integration with SunPy ``Map`` and the broader SunPy/Astropy ecosystem.

**Integration of Legacy IDL Tools** (:doc:`idl_tools`)  
Guidance on when and how to use **legacy IDL routines**, and how to safely
import IDL output files (``.sav``) into the Python environment for final
analysis and publication‑ready plotting, minimizing interruptions to your
Python workflow.


.. toctree::
   :maxdepth: 2
   :caption: Analysis Workflows

   products_and_levels
   data_access
   analysis_tools
   idl_tools






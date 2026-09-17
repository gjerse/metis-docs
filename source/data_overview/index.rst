Metis Data and Data Access
==========================

This section provides a central resource for understanding and accessing
**Solar Orbiter Metis data**. It introduces the available data products,
processing levels, FITS structure, metadata, and the different ways of
accessing Metis observations from the Solar Orbiter Archive (SOAR).

The section covers:

* data products and processing levels;
* FITS structure and naming conventions;
* key header keywords and metadata;
* programmatic access to Metis data from the SOAR archive;
* data access through the SunPy ``Fido`` interface;
* advanced archive access through the SOAR TAP service.

Use the pages below to follow a typical data-access workflow, from
understanding the available data products to discovering and downloading
the observations you need.


How to use this section
-----------------------

New to Metis data
^^^^^^^^^^^^^^^^^

* Start with :doc:`products_and_levels` to understand the available data
  products, processing levels, and FITS structure.
* Then go to :doc:`data_access` to learn how to find and download Metis
  observations from the Solar Orbiter Archive (SOAR).

Looking for programmatic data access
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* See :doc:`data_access` for examples using the SunPy ``Fido`` interface and
  the ``sunpy-soar`` plugin.
* See :doc:`data_access_tap` for advanced access to SOAR through the TAP
  service, including metadata queries using ADQL and PyVO.


Data and access workflows
-------------------------

Data products and processing levels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:doc:`products_and_levels` introduces the Metis data products, including:

* data processing levels (L0, L1, L2, L3) and their scientific meaning;
* the different types of Metis data products;
* FITS file naming conventions used in the Solar Orbiter Archive (SOAR);
* relevant header keywords and metadata.

Data access and download
^^^^^^^^^^^^^^^^^^^^^^^^

:doc:`data_access` gives instructions and Python examples for discovering and
downloading Metis data from the Solar Orbiter Archive using the SunPy ``Fido``
client and the ``sunpy-soar`` plugin.

Advanced SOAR access
^^^^^^^^^^^^^^^^^^^^

:doc:`data_access_tap` documents how to access the SOAR archive through the
Table Access Protocol (TAP) service. It introduces ADQL queries and the PyVO
interface for advanced metadata searches, archive inspection, and flexible
data selection.


.. toctree::
   :maxdepth: 2
   :caption: Metis Data

   products_and_levels
   data_access
   data_access_tap
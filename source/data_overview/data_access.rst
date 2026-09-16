Ways to Access Metis Data
=========================

This page summarizes the main ways to access and download **Solar Orbiter
Metis data** from the **Solar Orbiter Archive (SOAR)**.

If you are not sure where to start, use the **recommended Python workflow**
below.


Quick overview: how to access Metis data
----------------------------------------

There are four main access methods:

1. **Programmatic access with SunPy (recommended for Python users)**  
   Search, download, and load Metis data directly in Python using
   ``sunpy.net.Fido`` and the native SOAR client.  
   Best for: reproducible analysis, notebooks, pipelines.  
   → See: :doc:`data_access_python`

2. **Advanced metadata queries via SOAR TAP (power users)**  
   Use the SOAR TAP service and ADQL to build custom queries and catalogues.  
   Best for: large-scale queries, custom filters, archive inspection.  
   → See: :doc:`data_access_tap`

3. **Manual access via the SOAR web interface**  
   Browse and download individual files through the SOAR website.  
   Best for: first exploration, quick checks, small downloads.  
   → See: :ref:`soar-web-interface`

4. **Legacy / alternative access via VSO and SolarSoft (IDL)**  
   Access Metis data through the Virtual Solar Observatory and IDL/SolarSoft.  
   Best for: existing IDL workflows and legacy pipelines.  
   → See: :ref:`vso-ssw-access`


Method 1: Programmatic access with SunPy (recommended)
------------------------------------------------------

This is the **recommended workflow** for most users working in Python.

You can:

- search the SOAR archive with ``sunpy.net.Fido``;
- download Metis files;
- load them with ``sunpy.map.Map``;
- use the native ``METISMap`` class for Level 2 products.

Key features:

- integrated SOAR client in ``sunpy.net`` (no separate ``sunpy-soar`` package
  needed);
- standard SunPy syntax, consistent with other instruments;
- full interoperability with the SunPy ecosystem.

**Where to find detailed examples**

- :doc:`data_access_python` – step-by-step guide with code snippets.
- :doc:`../auto_gallery/index` – runnable notebooks and scripts, including:
  - searching and downloading Metis data;
  - loading and plotting ``METISMap`` objects;
  - building time series and CME height–time plots.

If you are new to Metis data, start from these pages.


Method 2: Advanced metadata queries via SOAR TAP
------------------------------------------------

For advanced use cases, SOAR provides a **TAP service** based on IVOA
standards. You can query the archive metadata using ADQL (Astronomical Data
Query Language) via ``PyVO`` or ``astroquery``.

This method is useful when you need to:

- build custom catalogues;
- filter on metadata not exposed by the standard ``Fido`` attributes;
- inspect archive descriptors and data-product properties;
- develop large-scale or highly customized queries.

**Where to find detailed examples**

- :doc:`data_access_tap` – detailed explanation of the TAP service, example
  ADQL queries, and Python code using ``astroquery``.


.. _soar-web-interface:

Method 3: Manual access via the SOAR web interface
--------------------------------------------------

The official **Solar Orbiter Archive** web interface is the primary tool for
manual browsing and download of individual files.

- **Interface:** `Solar Orbiter Archive <https://soar.esac.esa.int/soar/>`__
- **Search parameters:** instrument, time range, data level, product, filename.
- **Data types:** science data, low-latency data, auxiliary data.

This method is particularly useful when:

- you are exploring the archive for the first time;
- you want to check which products are available for a given time interval;
- you need to download a small number of files manually.

The web interface also supports **SAMP** (Simple Application Messaging
Protocol), allowing search results to be transferred to compatible external
applications such as **JHelioviewer**.

For more information, see the SOAR documentation on SAMP and external tool
integration.


.. _vso-ssw-access:

Method 4: Legacy / alternative access via VSO and SolarSoft
-----------------------------------------------------------

Metis data may also be accessed through the **Virtual Solar Observatory
(VSO)** and the **SolarSoft/IDL** ecosystem.

This route may be useful for:

- users maintaining established IDL workflows;
- legacy analysis procedures;
- cross-instrument queries involving data available through VSO.

For new Python workflows, the integrated SunPy/SOAR interface is recommended
because it provides the current standard interface for searching and loading
Metis data.


Data availability and releases
------------------------------

Metis data are distributed through scheduled data releases. The available
products, processing levels, and calibration status may depend on the release
and the version of the processing pipeline.

Before beginning a scientific analysis, record:

- the data-release identifier;
- the processing level;
- the product and observing mode;
- the pipeline or calibration version, when available;
- the date on which the data were downloaded.

Level 0 raw data and Level 1 engineering or uncalibrated products are not
necessarily distributed publicly. They may be available upon request for
calibration activities or specific scientific studies.

For technical assistance or data requests outside the public releases, contact
the Metis team through the support channel listed in
:doc:`../about/support`.


Recommended workflow for new users
----------------------------------

If you are new to Metis data, the following path is recommended:

1. Read this overview page.
2. Follow the **programmatic access with SunPy** examples in
   :doc:`data_access_python`.
3. Run one or more notebooks from the :doc:`../auto_gallery/index`.
4. Consult the relevant :doc:`../topic_guides/index` pages (coordinates,
   units, calibration, known issues) before interpreting enhanced or
   polarimetric products.


See also
--------

- :doc:`data_access_python` – detailed Python examples with ``Fido`` and
  ``METISMap``.
- :doc:`data_access_tap` – advanced TAP/ADQL queries.
- :doc:`analysis_tools` – overview of Metis analysis functions.
- :doc:`../auto_gallery/index` – runnable examples and notebooks.
- :doc:`../topic_guides/index` – scientific and technical background.
- :doc:`../about/support` – how to get help and report issues.
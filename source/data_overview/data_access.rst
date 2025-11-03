
Ways to Access Metis Data
=========================

This page details the available methods for accessing and downloading Metis data products from the **Solar Orbiter Archive (SOAR)**, focusing on **programmatic Python access**.

**Metis Data Availability**

Metis L2 data are available through the Solar Orbiter Archive
Level 0 (Raw) and Level 1 (Engineering) uncalibrated data are not publicly distributed but may be available upon request.  
For technical assistance or data requests outside of public releases, please contact the **Metis Team**.`<metis@inaf.it>`__


1. Programmatic Access (Python Recommended)
-------------------------------------------

Programmatic access allows users to search, download, and load data directly into their analysis environment (e.g., **Jupyter Notebooks**), ensuring a seamless workflow with the **Metis Python Tools**.


1.1. SunPy Plugin (``sunpy-soar``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The recommended and most straightforward method for Python users to interact with **SOAR** is via the **sunpy-soar** plugin.  
This integrates Metis data access directly into SunPy's ``Fido`` client.

.. list-table:: **Tool Overview**
   :header-rows: 1
   :widths: 20 50 30

   * - **Tool**
     - **Description**
     - **Relevance**
   * - ``sunpy-soar``
     - Plugin for accessing data in the Solar Orbiter Archive (SOAR) via the ``sunpy.net.Fido`` search interface.
     - Primary tool used by the Metis Python tools (e.g., ``metis_load()``).



1.2. VO Protocol Access (``PyVO``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For users familiar with the **Virtual Observatory (VO)** standards, the **PyVO** package allows querying the SOAR metadata tables directly using the **Table Access Protocol (TAP)** and the **Astronomy Data Query Language (ADQL)**.

.. list-table:: **VO Access Summary**
   :header-rows: 1
   :widths: 25 45 30

   * - **Protocol**
     - **Service URL**
     - **Purpose**
   * - TAP (Table Access Protocol)
     - http://soar.esac.esa.int/soar-sl-tap/tap
     - Query SOAR metadata and request data files using ADQL.

**Implementation Example (Searching SOAR tables)**

.. code-block:: python

   import pyvo as vo

   # TAP service URL endpoint to access SOAR tables
   service = vo.dal.TAPService("http://soar.esac.esa.int/soar-sl-tap/tap/")

   # Example: Execute an ADQL query to find data products
   results = service.search(
        "SELECT * FROM dbo.v_solo_files WHERE instrument='METIS' AND level=2")
   results.to_table().pprint()



1. Web Interface and Manual Access
----------------------------------

2.1. SOAR Web Interface
~~~~~~~~~~~~~~~~~~~~~~~

The primary method for manual browsing and download is the official **Solar Orbiter Archive** web interface.

- **Interface:** `SOAR Web Interface <https://soar.esac.esa.int/>`_
- **Search Parameters:** Instrument, Time (from/to), Level (L0, L1, L2, L3), and filename.
- **Data Types Available:** Science, Low Latency (LL), and Auxiliary Data.


2.2. Interoperability and Visualization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **SAMP Protocol:** The SOAR web interface supports the **SAMP (Simple Application Messaging Protocol)**.  
  This allows the search results to be instantly transferred and viewed in external visualization tools like **JHelioviewer**.

**Reference:** Consult the *SAMP tutorial* for setting up external tool integration.


2.3. VSO and SSW Access (Legacy / Alternative)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Data is also available via the **Virtual Solar Observatory (VSO)** interface, which can be accessed either through **IDL/SSW (SolarSoftWare)** or programmatically via the VSO module in **SunPy’s Fido**.


Data Availability and Releases
--------------------------------

Metis data is made available through scheduled periodic **data releases**.  
Check the list of current releases on the **Metis Team website** or the **SOAR interface** for the latest available data.

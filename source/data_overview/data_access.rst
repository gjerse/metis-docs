
Ways to Access Metis Data
=========================

This page details the available methods for accessing and downloading Metis data products from the **Solar Orbiter Archive (SOAR)**.

**Metis Data Availability**

Metis L2 data are available through the Solar Orbiter Archive.

Level 0 (Raw) and Level 1 (Engineering) uncalibrated data are not publicly distributed but may be available upon request.  
For technical assistance or data requests outside of public releases, please contact the **Metis Team** at `metis@inaf.it <mailto:metis@inaf.it>`_.


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
     - Primary tool used by the Metis Python tools. See Example Gallery for usage.

1.2. VO Protocol Access (``PyVO``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The direct web interface for the Solar Orbiter Archive (SOAR) is limited and not suitable for automated scripting. 

To address this, SOAR provides an Application Programming Interface (API) based on the standard IVOA (International Virtual Observatory Alliance) protocols.

PyVO simplifies this process in the Python environment, providing the necessary interface to execute TAP queries against the SOAR service.

.. list-table:: **VO Access Summary**
   :header-rows: 1
   :widths: 25 45 30

   * - **Protocol**
     - **Service URL**
     - **Purpose**
   * - TAP (Table Access Protocol)
     - http://soar.esac.esa.int/soar-sl-tap/tap
     - Query SOAR metadata and request data files using ADQL (Astronomy Data Query Language).

**Implementation Example (Searching SOAR tables)**

.. code-block:: python

    from astroquery.utils.tap.core import TapPlus
    from astropy.table import Table
    from datetime import datetime, timedelta

    # 1. TAP SOAR Service Configuration
    # The TAP service endpoint for SOAR
    SOAR_URL = 'http://soar.esac.esa.int/soar-sl-tap/tap'

    try:
        # 2. Initialize the TapPlus object
        SOAR = TapPlus(url=SOAR_URL)
        print("Connection to SOAR TAP service established.")
    except Exception as e:
        print(f"ERROR: Could not connect to TapPlus: {e}")
        # Note: Added 'sys.exit(1)' or similar would be needed to truly halt execution here.
        # For now, we continue execution for demonstration purposes.

    # --- Search Period Definition ---
    # We define a period of 600 days to find recent data
    end_date = datetime.today()
    start_date = end_date - timedelta(days=600)

    start_time_iso = start_date.strftime('%Y-%m-%dT%H:%M:%S')
    end_time_iso = end_date.strftime('%Y-%m-%dT%H:%M:%S')

    print(f"\nSearching for Metis L2 data between {start_date.date()} and {end_date.date()}...")

    # 3. ADQL Query Construction (Astronomy Data Query Language)
    # We query the scientific data items table (v_sc_data_item)
    ADQL_QUERY = f"""
        SELECT top 5 * FROM v_sc_data_item 
        WHERE 
            instrument = 'METIS' AND 
            level = 'L2' AND 
            begin_time >= '{start_time_iso}' AND 
            end_time <= '{end_time_iso}'
    """

    # 4. Asynchronous Task Execution (launch_job)
    # We use launch_job for queries that might take a long time
    try:
        tap_job = SOAR.launch_job(ADQL_QUERY)
        
        # 5. Get Results as an Astropy Table
        results_table = tap_job.get_results()
        
        # Print key results
        print(f"\n[RESULT] Found {len(results_table)} Metis L2 files (showing top 5):")
        
        # Convert the Astropy table to a Pandas DataFrame for clean visualization
        results_df = results_table.to_pandas()
        print(results_df[['data_item_id', 'begin_time', 'level', 'descriptor']].head())

        # 6. Extract Download URLs (The actual goal of TAP)
        # Direct download URLs are often included as the "access_url" column
        if 'access_url' in results_table.colnames:
            first_url = results_table['access_url'][0]
            print(f"\nDownload URL First File: {first_url}")
            
            # Note: The function for direct file download via astroquery 
            # depends on the service configuration; Fido is often used for the actual fetch.

    except Exception as e:
        print(f"\nERROR during ADQL query execution: {e}")



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

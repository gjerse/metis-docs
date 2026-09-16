Ways to Access Metis Data
=========================

This page describes the available methods for accessing and downloading
**Solar Orbiter Metis data** from the **Solar Orbiter Archive (SOAR)**.

For most Python users, the recommended workflow is to use the SOAR client
integrated into ``sunpy.net``. SunPy 8.0 also provides native support for
Metis Level 2 products through the ``METISMap`` class, allowing data search,
download, loading, and visualization within a standard SunPy workflow.

The main access methods are:

- programmatic access with SunPy and ``Fido``;
- advanced metadata queries through the SOAR TAP service;
- manual browsing through the SOAR web interface;
- legacy access through VSO and SolarSoft/IDL.


.. contents::
   :local:
   :depth: 2


SunPy and SOAR access
---------------------

SunPy 8.0 integrates the Solar Orbiter Archive client directly into
``sunpy.net``. The separate ``sunpy-soar`` package is no longer required for
this workflow.

This integration provides:

- a unified ``Fido`` interface for searching and downloading Solar Orbiter
  data;
- native SOAR search attributes;
- standard SunPy syntax for METIS data queries;
- compatibility with the broader SunPy data-access ecosystem;
- maintenance through the SunPy core ecosystem rather than through a separate
  client package.

Install or update SunPy with::

    pip install --upgrade sunpy

To verify the installed version::

    import sunpy

    print(sunpy.__version__)

The version should be ``8.0`` or later for the native ``METISMap`` and the
integrated SOAR workflow described on this page.


Searching and downloading data with Fido
----------------------------------------

The preferred method for searching and downloading Metis data is
``sunpy.net.Fido``.

The following example searches SOAR for Metis Level 2 visible-light total
brightness products and downloads the corresponding files:

.. code-block:: python

    from sunpy.net import Fido, attrs as a

    results = Fido.search(
        a.Time("2022-03-22 21:00", "2022-03-22 22:50"),
        a.Instrument.metis,
        a.Level(2),
        a.Provider.soar,
        a.soar.Product.metis_vl_tb,
    )

    print(results)

    files = Fido.fetch(results)

The exact number of files returned depends on the archive contents and the
search interval. The downloaded files can then be loaded with
``sunpy.map.Map``.


Loading Metis Level 2 data with METISMap
----------------------------------------

SunPy 8.0 provides the ``METISMap`` class for Metis Level 2 products.
``METISMap`` is a ``GenericMap`` subclass designed to preserve the standard
SunPy map interface while handling Metis-specific metadata and geometry.

A Metis FITS file may contain multiple HDUs. When such a file is loaded,
SunPy can return a list of map objects corresponding to the available data
products.

.. code-block:: python

    import sunpy.map

    maps = sunpy.map.Map(files[0])

    for metis_map in maps:
        print(metis_map.measurement)

For example, the visible-light total-brightness map can be selected using its
measurement metadata:

.. code-block:: python

    vl_tb = [
        metis_map for metis_map in maps
        if metis_map.measurement == "VL-TB"
    ][0]

    vl_tb.plot()

The ``METISMap`` implementation provides several Metis-specific features:

- support for visible-light and ultraviolet products;
- recognition of the measurement through the map metadata;
- handling of multiple products stored in a single FITS file;
- automatic masking of pixels inside the internal occulter and outside the
  outer field of view, when the relevant metadata are available;
- a sensible default display stretch for visualization.

The mask is intended to identify pixels outside the observed annular field of
view. It should not be interpreted as a substitute for scientific quality
assessment or calibration validation.


Visible-light and ultraviolet products
--------------------------------------

``METISMap`` supports both the visible-light and ultraviolet channels.

The visible-light channel includes products such as polarized brightness
(``pB``) and total brightness (``tB``). The ultraviolet channel observes the
hydrogen Lyman-alpha emission at approximately 121.6 nm.

The measurement can be inspected through the map object:

.. code-block:: python

    print(vl_tb.measurement)

For a file containing several products, inspect all returned maps before
selecting the product required for the analysis:

.. code-block:: python

    for index, metis_map in enumerate(maps):
        print(index, metis_map.measurement, metis_map.data.shape)


Visualization and image enhancement
-----------------------------------

The default ``METISMap.plot()`` behavior is intended to provide a useful first
visualization of the observed annular field of view. The display stretch can
be adjusted when needed.

.. code-block:: python

    vl_tb.plot(clip_interval=(1, 99.5))

For scientific interpretation, distinguish clearly between:

- calibrated data;
- visualization stretches;
- image-enhancement products;
- quantitatively derived physical quantities.

Enhancement methods such as MGN, NRGF, FNRGF, RHEF, and related techniques may
be useful for identifying structures such as CME fronts and streamers.
However, enhanced images should not automatically be used for quantitative
photometry or radiometric measurements.

For more information, see the
:doc:`../topic_guides/index` section.


Advanced access through the SOAR TAP service
-------------------------------------------

The SOAR web interface is useful for manual browsing, but advanced users may
need more flexible queries than those exposed through the standard ``Fido``
interface.

SOAR provides a TAP service based on IVOA standards. The service can be queried
using ADQL, the Astronomical Data Query Language, through ``PyVO`` or
``astroquery``.

.. list-table:: **SOAR TAP access**
   :header-rows: 1
   :widths: 25 45 30

   * - **Protocol**
     - **Service URL**
     - **Purpose**
   * - TAP
     - ``http://soar.esac.esa.int/soar-sl-tap/tap``
     - Query SOAR metadata and retrieve data-access information using ADQL.

TAP access is particularly useful for:

- building custom catalogues;
- filtering on metadata not exposed by the standard ``Fido`` attributes;
- inspecting archive descriptors;
- developing large-scale or automated archive queries.


Example: querying SOAR with astroquery
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from astroquery.utils.tap.core import TapPlus
    from datetime import datetime, timedelta

    soar_url = "http://soar.esac.esa.int/soar-sl-tap/tap"

    soar = TapPlus(url=soar_url)

    end_date = datetime.today()
    start_date = end_date - timedelta(days=600)

    start_time = start_date.strftime("%Y-%m-%dT%H:%M:%S")
    end_time = end_date.strftime("%Y-%m-%dT%H:%M:%S")

    adql_query = f"""
        SELECT TOP 5 *
        FROM v_sc_data_item
        WHERE
            instrument = 'METIS'
            AND level = 'L2'
            AND begin_time >= '{start_time}'
            AND end_time <= '{end_time}'
    """

    tap_job = soar.launch_job(adql_query)
    results_table = tap_job.get_results()

    print(f"Found {len(results_table)} Metis L2 data products.")
    print(results_table)


If an ``access_url`` column is present, it can be inspected as follows:

.. code-block:: python

    if "access_url" in results_table.colnames:
        print(results_table["access_url"][0])

The exact table names, column names, and service behavior should be checked
against the current SOAR TAP documentation before using a query in a
production pipeline.


SOAR web interface
------------------

The official SOAR web interface remains useful for manual searches and
individual downloads.

- **Interface:** `Solar Orbiter Archive <https://soar.esac.esa.int/soar/>`__
- **Search parameters:** instrument, time range, data level, product, and
  filename;
- **Data types:** science data, low-latency data, and auxiliary data.

The web interface is particularly useful when:

- exploring the archive for the first time;
- checking which products are available;
- inspecting a specific observation;
- downloading a small number of files manually.


Interoperability and visualization
----------------------------------

The SOAR web interface supports the **SAMP** protocol, the Simple Application
Messaging Protocol.

SAMP allows search results to be transferred to compatible external astronomy
applications, including visualization tools such as **JHelioviewer**.

See the relevant SOAR documentation for instructions on configuring SAMP and
connecting external applications.


VSO and SolarSoft access
------------------------

Metis data may also be accessed through the **Virtual Solar Observatory (VSO)**
and the SolarSoft/IDL ecosystem.

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


Recommended workflow
--------------------

For most users, the following workflow is recommended:

1. Install SunPy 8.0 or later.
2. Search the SOAR archive with ``Fido``.
3. Download the required files with ``Fido.fetch``.
4. Load the products with ``sunpy.map.Map``.
5. Inspect the returned ``METISMap`` objects and their metadata.
6. Apply the analysis workflow appropriate to the product.
7. Record the data release and software versions used.
8. Consult the relevant topic guides before interpreting enhanced or
   polarimetric products.

See also:

- :doc:`analysis_tools` for Metis analysis functions;
- :doc:`../auto_gallery/index` for runnable examples;
- :doc:`../topic_guides/index` for calibration, coordinates, uncertainties,
  polarimetry, and known issues;
- the official SunPy example
  `Downloading and plotting Metis coronagraph data
  <https://docs.sunpy.org/en/stable/generated/gallery/map/plotting_metis_data.html>`__.
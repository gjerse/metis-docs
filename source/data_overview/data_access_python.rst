.. _data-access-python:

Accessing Metis Data with Python (SunPy)
========================================

This page shows how to search, download, and load **Solar Orbiter Metis data**
in Python using the integrated SOAR client in ``sunpy.net``.

This is the **recommended workflow** for most users.


Prerequisites
-------------

You need:

- Python 3.10 or newer;
- SunPy 8.0 or later (for the native SOAR client and ``METISMap`` support);
- optionally, the Metis Python tools if your workflow depends on them.

Install or upgrade SunPy with::

    pip install --upgrade sunpy

To verify the installed version::

    import sunpy

    print("SunPy version:", sunpy.__version__)

The version should be ``8.0`` or later.


Overview of the workflow
------------------------

The typical Python workflow is:

1. Define the time range and the Metis product you need.
2. Search the SOAR archive with ``sunpy.net.Fido``.
3. Download the files with ``Fido.fetch``.
4. Load the data with ``sunpy.map.Map``.
5. Inspect the returned ``METISMap`` objects and their metadata.
6. Proceed with your scientific analysis (plotting, time series, polarimetry,
   etc.).

The following sections show each step in detail.


Searching Metis data with Fido
------------------------------

The ``sunpy.net.Fido`` interface provides a unified way to search data from
multiple archives, including SOAR.

The following example searches for Metis Level 2 visible-light total-brightness
products in a given time interval:

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

The result is a ``FidoSearchResults`` object listing the matching data products.
You can inspect the number of files and their metadata:

.. code-block:: python

    print(f"Number of results: {len(results)}")
    for table in results:
        print(table)

Adjust the time range, level, and product according to your scientific needs.
Available products and levels depend on the data release and the archive
contents.


Downloading the data
--------------------

Once you have identified the desired results, download the files with
``Fido.fetch``:

.. code-block:: python

    files = Fido.fetch(results)

    print("Downloaded files:")
    for f in files:
        print(f)

By default, SunPy stores downloaded files in a cache directory (typically under
your home directory). Subsequent searches for the same data will use the
cached files instead of downloading them again.

If you want to control the download location, you can specify a custom path
(consult the SunPy documentation for the current API).


Loading Metis data with METISMap
--------------------------------

SunPy 8.0 provides the ``METISMap`` class for Metis Level 2 products. When you
load a Metis FITS file with ``sunpy.map.Map``, SunPy automatically uses
``METISMap`` if the metadata match the expected pattern.

A single FITS file may contain multiple HDUs, corresponding to different
products or channels. Loading such a file returns a list of map objects:

.. code-block:: python

    import sunpy.map

    maps = sunpy.map.Map(files[0])

    print(f"Number of maps in this file: {len(maps)}")

    for index, metis_map in enumerate(maps):
        print(index, metis_map.measurement, metis_map.data.shape)

You can then select the product you need. For example, to select the
visible-light total-brightness map:

.. code-block:: python

    vl_tb = [
        metis_map for metis_map in maps
        if metis_map.measurement == "VL-TB"
    ][0]

    print("Selected map:")
    print("  Measurement:", vl_tb.measurement)
    print("  Date:", vl_tb.date)
    print("  Detector:", vl_tb.detector)
    print("  Data shape:", vl_tb.data.shape)

The ``METISMap`` implementation is designed to:

- support visible-light and ultraviolet products;
- recognize the measurement through the map metadata;
- handle multiple products stored in a single FITS file;
- provide automatic masking of pixels inside the internal occulter and outside
  the outer field of view, when the relevant metadata are available;
- use a sensible default display stretch for visualization.

The mask is intended to identify pixels outside the observed annular field of
view. It should not be interpreted as a substitute for scientific quality
assessment or calibration validation.


Basic visualization
-------------------

Once you have a ``METISMap`` object, you can visualize it using the standard
SunPy plotting interface:

.. code-block:: python

    import matplotlib.pyplot as plt

    vl_tb.plot()
    plt.title(f"Metis {vl_tb.measurement} - {vl_tb.date}")
    plt.show()

You can adjust the display stretch using the ``clip_interval`` parameter:

.. code-block:: python

    vl_tb.plot(clip_interval=(1, 99.5))
    plt.show()

For scientific interpretation, distinguish clearly between:

- calibrated data;
- visualization stretches;
- image-enhancement products;
- quantitatively derived physical quantities.

Enhanced images (e.g. MGN, NRGF, RHEF) may be useful for identifying
structures such as CME fronts and streamers, but they should not automatically
be used for quantitative photometry or radiometric measurements.


Time series and sequences
-------------------------

To analyze a time series of Metis images, you can build a ``MapSequence``:

.. code-block:: python

    # Suppose 'files' contains multiple FITS files
    all_maps = []

    for f in files:
        maps = sunpy.map.Map(f)
        # Select the same product from each file
        selected = [
            m for m in maps
            if m.measurement == "VL-TB"
        ][0]
        all_maps.append(selected)

    sequence = sunpy.map.Map(all_maps, sequence=True)

    print(f"MapSequence with {len(sequence)} maps")

You can then:

- plot individual frames;
- create running-difference or base-difference sequences;
- animate the sequence (see the SunPy documentation for animation examples).


Example: CME height–time analysis
---------------------------------

A typical use case is to track a CME front in a sequence of Metis images and
build a height–time plot.

The general steps are:

1. Download a time series of Metis images covering the CME.
2. Load the data as a ``MapSequence``.
3. For each frame, identify the CME front (manually or with an automated
   method).
4. Convert pixel positions to heliocentric distances using the map metadata.
5. Plot height versus time.

A complete example is available in the :doc:`auto_gallery/index`. You can use
it as a starting point and adapt it to your own events and methods.


Common search patterns
----------------------

Below are a few common patterns you may find useful.

**Search by time range and instrument**

.. code-block:: python

    results = Fido.search(
        a.Time("2022-03-22 00:00", "2022-03-22 23:59"),
        a.Instrument.metis,
    )

**Search by level and provider**

.. code-block:: python

    results = Fido.search(
        a.Time("2022-03-22 21:00", "2022-03-22 22:50"),
        a.Instrument.metis,
        a.Level(2),
        a.Provider.soar,
    )

**Search by product**

.. code-block:: python

    results = Fido.search(
        a.Time("2022-03-22 21:00", "2022-03-22 22:50"),
        a.Instrument.metis,
        a.Level(2),
        a.Provider.soar,
        a.soar.Product.metis_vl_tb,
    )

The exact set of available attributes and products may evolve over time. For
the most up-to-date information, consult the SunPy documentation and the
:doc:`../auto_gallery/index` examples.


Troubleshooting
---------------

**No results returned**

- Check that the time range actually contains Metis observations.
- Verify that the level and product exist for that period.
- Try a broader time interval or remove some filters.

**Import errors or missing attributes**

- Ensure that you are using SunPy 8.0 or later.
- Check that you are importing from ``sunpy.net`` and not from a deprecated
  ``sunpy-soar`` package.
- Consult the SunPy “What’s New” documentation for version-specific changes.

**Issues with METISMap**

- Verify that the file you are loading is a Metis Level 2 product.
- Inspect the map metadata (``metis_map.meta``) to confirm that the required
  keywords are present.
- Compare with the official SunPy Metis example in the SunPy gallery.


Where to go next
----------------

- :doc:`data_access_tap` – advanced metadata queries via the SOAR TAP service.
- :doc:`analysis_tools` – overview of Metis analysis functions.
- :doc:`../auto_gallery/index` – runnable examples and notebooks.
- :doc:`../topic_guides/index` – coordinates, units, calibration, known issues.
- :doc:`../about/support` – how to get help and report issues.


References
----------

- SunPy documentation: `https://docs.sunpy.org <https://docs.sunpy.org>`__
- What’s New in SunPy 8.0: `whatsnew/8.0.html
  <https://docs.sunpy.org/en/latest/whatsnew/8.0.html>`__
- Example: Downloading and plotting Metis coronagraph data:
  `plotting_metis_data.html
  <https://docs.sunpy.org/en/stable/generated/gallery/map/plotting_metis_data.html>`__
- SOAR archive: `https://soar.esac.esa.int/soar/
  <https://soar.esac.esa.int/soar/>`__
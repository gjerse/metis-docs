.. _data-access-tap:

Advanced Access to Metis Data via SOAR TAP (PyVO)
=================================================

This page describes how to perform advanced queries on the **Solar Orbiter
Archive (SOAR)** using the **TAP (Table Access Protocol)** service and ADQL
(Astronomical Data Query Language) via the **PyVO** library.

This method is intended for **power users** who need:

- custom metadata filters;
- large-scale archive queries;
- detailed inspection of archive tables and columns;
- integration with non-SunPy pipelines.

For most day-to-day analysis, the standard ``sunpy.net.Fido`` interface
described in :doc:`data_access_python` is simpler and sufficient.


Overview of the SOAR TAP service
--------------------------------

SOAR provides a TAP service that allows you to query the archive metadata
using ADQL.

- **Service URL:** ``http://soar.esac.esa.int/soar-sl-tap/tap``
- **Protocol:** TAP (IVOA Table Access Protocol)
- **Query language:** ADQL (Astronomical Data Query Language)

Through this service you can:

- search for Metis data products by time, level, instrument, and other
  metadata;
- inspect available tables and views (e.g. ``v_sc_data_item``,
  ``v_met_sc_fits``, etc.);
- retrieve metadata columns such as ``data_item_id``, ``begin_time``,
  ``level``, ``descriptor``, and, when available, ``access_url``;
- build custom catalogues for downstream analysis.

The TAP service is particularly useful when you need more flexibility than the
standard ``Fido`` search attributes provide.

Some SOAR tools (e.g. data-availability plots, internal data-release checks)
also rely on the same TAP interface.


Installing PyVO
---------------

Install PyVO with::

    pip install pyvo

You will also need Astropy (usually already installed if you use SunPy)::

    pip install astropy


Connecting to the SOAR TAP service
----------------------------------

The following example shows how to connect to the SOAR TAP service using
PyVO.

.. code-block:: python

    import pyvo as vo

    # TAP service URL endpoint for SOAR
    service = vo.dal.TAPService("http://soar.esac.esa.int/soar-sl-tap/tap")

You can then inspect the available tables:

.. code-block:: python

    tables = service.tables

    print("Available tables:")
    for table_name in tables:
        print(table_name)

To access metadata for a specific table:

.. code-block:: python

    table_name = "soar.v_met_sc_fits"
    table = service.tables[table_name]

    print(f"Table: {table_name}")
    print(f"Description: {table.description}")

    print("Columns:")
    for column in table.columns:
        print(f"- {column.name}: {column.description} ({column.datatype})")

The exact table names and columns may evolve over time. Use this approach to
explore the current schema before writing your queries.


Basic ADQL query for Metis data
-------------------------------

The following example queries a Metis-specific view for Level 2 products in a
given time interval.

.. code-block:: python

    # Define ADQL query
    query = """
        SELECT *
        FROM soar.v_met_sc_fits
        WHERE
            level = 'L2'
            AND date_begin >= '2022-04-01T00:00:00'
            AND date_end   <= '2022-05-01T00:00:00'
        ORDER BY date_begin
    """

    # Run synchronous query
    job = service.run_sync(query)

    # Get result as an Astropy Table
    result_table = job.to_table()

    print(f"Found {len(result_table)} Metis L2 data products.")
    print(result_table)

You can adapt the query to:

- change the time interval;
- restrict to specific products (if exposed in the metadata);
- select specific columns instead of ``SELECT *``.


Selecting specific columns
--------------------------

To reduce the amount of data transferred, you can select only the columns you
need. For example:

.. code-block:: python

    query = """
        SELECT
            data_item_id,
            date_begin,
            date_end,
            level,
            descriptor,
            access_url
        FROM soar.v_met_sc_fits
        WHERE
            level = 'L2'
            AND date_begin >= '2022-04-01T00:00:00'
            AND date_end   <= '2022-05-01T00:00:00'
        ORDER BY date_begin
    """

    job = service.run_sync(query)
    result_table = job.to_table()

    print(result_table)

Inspect the available columns by running a ``SELECT *`` query once and
examining ``result_table.colnames``.


Saving results to disk
----------------------

You can save the query result to a CSV file for later use:

.. code-block:: python

    result_table.write("metis_data.csv", format="csv", overwrite=True)

You can then load this file in Python (e.g. with Astropy or Pandas) or in
other tools.


Using the results
-----------------

The result of a TAP query is an ``astropy.table.Table``. You can:

- convert it to a Pandas DataFrame:

  .. code-block:: python

      import pandas as pd

      df = result_table.to_pandas()
      print(df.head())

- filter it further in Python;
- save it to disk (e.g. CSV, Parquet) for later use;
- extract download URLs if an ``access_url`` column is present.

For example, to inspect the first download URL:

.. code-block:: python

    if "access_url" in result_table.colnames:
        first_url = result_table["access_url"][0]
        print("First access URL:", first_url)

The exact mechanism for downloading files from these URLs depends on the
service configuration. In many cases, you can use standard HTTP tools or
``requests`` to fetch the files once you have the URLs.


Alternative query: generic data-item view
-----------------------------------------

In addition to instrument-specific views, SOAR exposes more generic views such
as ``v_sc_data_item``. These can be useful for cross-instrument queries or for
a broader overview of the archive.

Example:

.. code-block:: python

    query = """
        SELECT TOP 20 *
        FROM v_sc_data_item
        WHERE
            instrument = 'METIS'
            AND level = 'L2'
            AND begin_time >= '2022-04-01T00:00:00'
            AND end_time   <= '2022-05-01T00:00:00'
        ORDER BY begin_time
    """

    job = service.run_sync(query)
    result_table = job.to_table()

    print(f"Found {len(result_table)} Metis L2 data products.")
    print(result_table)

The exact column names (``begin_time`` vs ``date_begin``, etc.) depend on the
specific table or view. Always inspect the table metadata before writing your
queries.


Synchronous vs asynchronous queries
-----------------------------------

The examples above use **synchronous** queries via ``run_sync``. This is
suitable for queries that return a moderate amount of data and complete
quickly.

For very large queries, the service may also support **asynchronous** queries
(via ``submit_job`` / ``run_async``, depending on the PyVO version and service
capabilities). In that case:

.. code-block:: python

    job = service.submit_job(query)
    job.run()
    job.wait()
    result_table = job.fetch_result().to_table()

Consult the PyVO documentation and the SOAR TAP documentation for details on
asynchronous queries, job limits, and timeouts.


Comparison with the Fido interface
----------------------------------

The main differences between the TAP approach and the standard
``sunpy.net.Fido`` workflow are:

- **Fido**:
  - high-level, instrument-oriented interface;
  - integrated with SunPy’s data loading and map classes;
  - recommended for most scientific analyses.

- **TAP/ADQL (PyVO)**:
  - low-level, metadata-oriented interface;
  - maximum flexibility for custom queries;
  - better suited for building catalogues, archive inspection, and advanced
    filtering;
  - requires more manual work to go from metadata to loaded data.

In practice, many users will:

- use Fido for routine analysis;
- use TAP for specific tasks that require custom metadata queries or
  large-scale archive exploration.


Troubleshooting
---------------

**Connection errors**

- Verify the service URL: ``http://soar.esac.esa.int/soar-sl-tap/tap``.
- Check your network connection and any firewall or proxy settings.
- Try accessing the TAP endpoint in a web browser to confirm that it is
  reachable.

**No results returned**

- Check that the time interval actually contains Metis observations.
- Verify that the level and instrument names match the archive conventions
  (e.g. ``'METIS'``, ``'L2'``).
- Try a broader time interval or remove some filters.

**Unexpected columns or missing metadata**

- The available tables and columns may change between data releases.
- Inspect the table schema using ``service.tables`` and explore the relevant
  table definitions.
- Consult the SOAR documentation for the most up-to-date metadata description.


Where to go next
----------------

- :doc:`data_access_python` – recommended Python workflow with ``Fido`` and
  ``METISMap``.
- :doc:`analysis_tools` – overview of Metis analysis functions.
- :doc:`../auto_gallery/index` – runnable examples and notebooks.
- :doc:`../topic_guides/index` – coordinates, units, calibration, known issues.
- :doc:`../about/support` – how to get help and report issues.


References
----------

- SOAR archive: `https://soar.esac.esa.int/soar/
  <https://soar.esac.esa.int/soar/>`__
- PyVO documentation: `https://pyvo.readthedocs.io
  <https://pyvo.readthedocs.io>`__
- IVOA TAP standard: `https://www.ivoa.net/documents/TAP/
  <https://www.ivoa.net/documents/TAP/>`__
- SOAR TAP documentation (via the SOAR website).
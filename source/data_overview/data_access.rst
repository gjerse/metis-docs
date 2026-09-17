Ways to Access Metis Data
=========================

This page summarizes the main ways to access and download **Solar Orbiter
Metis data** from the **Solar Orbiter Archive (SOAR)**.

If you are not sure where to start, the **Python workflow with SunPy** 
is the recommended starting point for most users. 


Quick overview: how to access Metis data
----------------------------------------

There are three main ways to access Metis data:

1. **Programmatic access with SunPy**  

   Search, download, and load Metis data directly in Python using
   ``sunpy.net.Fido`` and the native SOAR client.  
   | *Best for:* reproducible analysis, notebooks, pipelines.
   | *See:* :doc:`/data_overview/data_access_python`
   

2. **Advanced metadata queries via SOAR TAP**  
   Use the SOAR TAP service and ADQL to build custom queries and catalogues.  
   | *Best for:* large-scale queries, custom filters, archive inspection.  
   | *See:* :doc:`/data_overview/data_access_tap`

3. **Manual access via the SOAR web interface**  
   The official **Solar Orbiter Archive** web interface provides a convenient way to browse and download individual files.

    - **Interface:** `Solar Orbiter Archive <https://soar.esac.esa.int/soar/>`__
    - **Search parameters:** instrument, time range, data level, product, filename.
    - **Data types:** science data, low-latency data and auxiliary data.

    The web interface also supports **SAMP** (Simple Application Messaging
    Protocol), allowing search results to be transferred to compatible external
    applications such as **JHelioviewer**.

    For more information, see the SOAR documentation on SAMP and external tool
    integration.



Data availability and planning
------------------------------

Metis observations are not continuous: they are scheduled within Remote-Sensing
Windows and dedicated campaigns. Before searching the archive, check the
`Observation Summary <https://metis.oato.inaf.it/obs_summary_new.html>`_ to find the observing periods relevant to your science
case, and the `Metis data access page <https://metis.oato.inaf.it/data_access.html>`_ for the products and public releases
currently available.

Publicly distributed products are Level 2, calibrated in physical units and
intended for scientific analysis. They may be reprocessed as the calibration
and the understanding of the instrument response improve, so always record
which release you used. Level 0 and Level 1 products are not publicly
distributed, but may be made available on request for calibration work or
specific studies.

.. warning::
 
   Low-latency data are produced for quick-look purposes only and must not be
   used for quantitative analysis.


Using Metis data
----------------

When using Metis data for scientific analysis, the recommended workflow
is:

1. **Identify the observing period** using the
   `Observation Summary <https://metis.oato.inaf.it/obs_summary_new.html>`_.

2. **Check data availability and release information** through the
   `Metis data access page <https://metis.oato.inaf.it/data_access.html>`_.

3. **Search and download the required Level-2 products** using
   SunPy/SOAR or the other access methods described above.

4. **Load and analyse the data** using the Metis/SunPy tools and the
   examples provided in this documentation.

5. **Record the dataset and release information** used in the analysis,
   including the relevant dataset identifier or DOI.

6. **Check the Metis Publication Policy** for
   acknowledgements, dataset DOI, citations, and authorship
   requirements.


If you are unsure whether a product is suitable for your analysis, contact the
Metis team (:doc:`../about/support`).



Links
-----

* `Ways to access Metis data <https://metis.oato.inaf.it/data_access.html>`_
* `Observation Summary <https://metis.oato.inaf.it/obs_summary_new.html>`_
* `Metis Publication Policy <https://metis.oato.inaf.it/policy.html>`_
* `Data access with SunPy <data_access_python.html>`_
* `Advanced access via SOAR TAP <data_access_tap.html>`_
* `Example Gallery <../auto_gallery/index.html>`_




.. code-block:: rst
 
    Legacy IDL Tools
    ================
 
    Metis data analysis has historically been carried out with IDL and
    SolarSoft. Those procedures are still in use and still produce results
    that must be reproducible, so they are documented here.
 
    New analyses should use the Python tools described in
    :doc:`/analysis_python/index`. This section exists to make the existing
    IDL work understandable, reproducible, and portable, not to encourage
    new development in IDL.
 
    What you will find here:
 
    * what each legacy routine does, and which data products it expects;
    * whether a Python equivalent exists, and where it is;
    * how to read IDL ``.sav`` outputs into Python;
    * differences in conventions (axis order, units, masking) that produce
      apparently different results between the two implementations.
 
    .. list-table:: IDL to Python correspondence
       :header-rows: 1
       :widths: 25 40 35
 
       * - IDL routine
         - Purpose
         - Python equivalent
       * - ``metis_read``
         - Read an L2 FITS file
         - ``sunpy.map.Map``
       * - ``metis_mask``
         - Mask occulter and outer FOV
         - built into ``METISMap``
       * - ``...``
         - ...
         - not yet available
 
    .. toctree::
       :maxdepth: 2
 
       routine_reference
       reading_idl_output
       conventions
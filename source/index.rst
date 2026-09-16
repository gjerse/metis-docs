.. Solar Orbiter Metis Docs documentation master file, created by
   sphinx-quickstart on Sat Nov  1 18:18:26 2025.

====================================
Metis Data Tools User Guide
====================================
Welcome to the **Solar Orbiter Metis Data Tools User Guide**! 🌞🚀

This documentation supports researchers and students working with **Metis data in Python**, 
primarily within the ``SunPy`` / ``Astropy`` ecosystem. It covers:

- data products and processing levels;
- access to Metis data and metadata;
- scientific caveats and known instrumental effects;
- reproducible analysis workflows and examples;
- reference documentation for the Metis Python tools.


This documentation is divided into key sections to guide you from installation to advanced analysis.

.. grid:: 1 1 2 3
    :gutter: 2 3 4 4

    .. grid-item-card::
        :text-align: center

        :material-outlined:`rocket_launch;8em;sd-text-secondary`

        **Getting Started**
        ^^^

        Install the required packages, configure your environment, and run your first end‑to‑end Metis example.
        +++

        .. button-ref:: getting_started
            :color: primary
            :click-parent:

            To the Getting Started Guide

    .. grid-item-card::
        :text-align: center

        :material-outlined:`build;8em;sd-text-secondary`

        **Data & Tools**
        ^^^

        Understand Metis data levels, FITS structure, descriptors, and access methods.  
        Find links to Python tools and legacy IDL routines.

        +++

        .. button-ref:: data_overview/index
            :color: primary
            :click-parent:

            Explore Data and Tools

    .. grid-item-card::
        :text-align: center

        :material-outlined:`palette;8em;sd-text-secondary`

    **Topic Guides**
        ^^^

        Scientific and technical background: coordinates and FOV, units and
        uncertainties, calibration, polarimetry, image enhancement, known
        issues, and co‑observations.

        +++

        .. button-ref:: topic_guides/index
            :color: primary
            :click-parent:

            Browse Topic Guides

    .. grid-item-card::
        :text-align: center

        :material-outlined:`code;8em;sd-text-secondary`

        **Example Gallery**
        ^^^

        Reproducible Python scripts and Jupyter notebooks for common Metis analyses: 
        time series, polarimetry, CME tracking, and multi‑instrument studies.

        +++

        .. button-ref:: auto_gallery/index
            :color: primary
            :click-parent:

            Open the Gallery

    .. grid-item-card::
        :text-align: center

        :material-outlined:`volunteer_activism;8em;sd-text-secondary`

        **API Reference**
        ^^^

        Auto‑generated reference for the Metis Python packages: classes, functions, and parameters.

        +++

        .. button-ref:: api_reference/index
            :color: primary
            :click-parent:

            View API Reference

    .. grid-item-card::
        :text-align: center

        :material-outlined:`volunteer_activism;8em;sd-text-secondary`


        **Contribute & About**
        ^^^

        How to contribute to this documentation, report issues, and find the changelog, glossary, and support contacts.
        +++

        .. button-ref:: about/index
            :color: primary
            :click-parent:

            See Contribution Guide


What is this Documentation For?
===============================  

.. container:: custom-section
    
    This documentation aims to support the Metis data user community by:
    
    * Helping researchers and enthusiasts work with Solar Orbiter Metis data.
    * Providing interactive Python examples for common data analysis tasks.
    * Hosting useful links, resources, and tutorials.
    * Encouraging community contributions!

**Useful Links**

| `ESA Solar Orbiter <https://www.cosmos.esa.int/web/solar-orbiter>`__ |
| `Solar Orbiter Archive <https://soar.esac.esa.int/soar/>`__ |
| `Metis Project <https://metis.oato.inaf.it/>`__ |
| `GitHub Repository <https://github.com/gjerse/metis-docs>`__ |


.. toctree::
   :maxdepth: 1
   :hidden:

   Getting Started <getting_started>
   Data and Tools Overview <data_overview/index>
   Topic Guide <topic_guides/index>  
   Example Gallery <examples/index>
   API Reference <api_reference/index>
   About <about/index>
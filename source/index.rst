.. Solar Orbiter Metis Docs documentation master file, created by
   sphinx-quickstart on Sat Nov  1 18:18:26 2025.

====================================
Metis Data Tools User Guide
====================================
Welcome to the **Solar Orbiter Metis Data Tools User Guide**! 🌞🚀

This documentation provides guides, interactive examples, and resources 
for working with **Metis data in Python**, primarily utilizing the powerful 
`SunPy <https://sunpy.org>`__ ecosystem.

### Key Sections and Documentation Structure

This documentation is divided into key sections to guide you from installation to advanced analysis.

.. grid:: 1 1 2 2
    :gutter: 2 3 4 4

    .. grid-item-card::
        :text-align: center

        :material-outlined:`rocket_launch;8em;sd-text-secondary`

        **Getting Started**
        ^^^

        Learn how to install Python dependencies and begin loading your first Metis data file.

        +++

        .. button-ref:: getting_started
            :color: primary
            :click-parent:

            To the Getting Started Guide

    .. grid-item-card::
        :text-align: center

        :material-outlined:`build;8em;sd-text-secondary`

        **Data & Tools Overview**
        ^^^

        Details on Metis data levels and documentation for both Python and legacy IDL analysis tools.

        +++

        .. button-ref:: data_overview/index
            :color: primary
            :click-parent:

            Explore Data and Tools

    .. grid-item-card::
        :text-align: center

        :material-outlined:`palette;8em;sd-text-secondary`

        **Example Gallery**
        ^^^

        Browse interactive scripts and Jupyter Notebooks demonstrating Metis data analysis and visualization.

        +++

        .. button-ref:: auto_gallery/index
            :color: primary
            :click-parent:

            Open the Gallery

    .. grid-item-card::
        :text-align: center

        :material-outlined:`volunteer_activism;8em;sd-text-secondary`

        **Contribute**
        ^^^

        Learn how to help improve this documentation, submit examples, or contribute to the Metis Python code.

        +++

        .. button-ref:: contributing
            :color: primary
            :click-parent:

            See Contribution Guide


.. container:: custom-section
    
    What is this Documentation For?
    ===============================
    
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
   Example Gallery <auto_gallery/index>
   API Reference <api_reference/index>
   Contributing <contributing>
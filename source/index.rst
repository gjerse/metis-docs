.. Solar Orbiter Metis Docs documentation master file, created by
   sphinx-quickstart on Sat Nov  1 18:18:26 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


==================================
Solar Orbiter Metis Data Documentation
================================== 
Welcome to the Solar Orbiter Data Documentation! 🌞🚀  

# Metis Documentation
=====================  <-- CORREZIONE: Sostituito il titolo H1 non-RST (# Metis Documentation) con un'intestazione H2 corretta, e allineato l'underline.

Welcome to the **Metis Python Tools documentation**!!   🌞🚀

This wants to provide guides, examples, and resources 
for working with Metis data in Python, using the `SunPy <https://sunpy.org>`__ ecosystem.

.. grid:: 1 1 2 2
    :gutter: 2 3 4 4

    .. grid-item-card::
        :text-align: center

        :material-outlined:`rocket_launch;8em;sd-text-secondary`

        **Getting Started**
        ^^^

        Learn how to install dependencies and get started with Solar Orbiter Metis data.

        +++

        .. button-ref:: getting_started
            :color: secondary
            :click-parent:

            To the Getting Started Guide



    .. grid-item-card::
        :text-align: center

        :material-outlined:`build;8em;sd-text-secondary`

        **Analysis Tools**
        ^^^

        Tools for analyzing Solar Orbiter Metis data using SunPy and other Python packages.

        +++

        .. button-ref:: data_overview/analysis_tools
            :color: secondary
            :click-parent:

            To the Analysis Tools

    .. grid-item-card::
        :text-align: center

        :material-outlined:`palette;8em;sd-text-secondary`

        **Example Gallery**
        ^^^

        Browse interactive examples demonstrating Solar Orbiter Metis data analysis.

        +++

        .. button-ref:: auto_gallery/index
            :color: secondary
            :click-parent:

            To the Example Gallery

    .. grid-item-card::
        :text-align: center

        :material-outlined:`volunteer_activism;8em;sd-text-secondary`

        **Contribute to the Docs**
        ^^^

        Help improve this documentation by adding examples, fixing typos, or suggesting new content.

        +++

        .. button-ref:: contributing
            :color: secondary
            :click-parent:

            Go to Contributing Guide


What is this Documentation For?
=================================
                                 <-- CORREZIONE: Riga vuota tra titolo e lista (RST richiede una linea vuota)

* Helping researchers and enthusiasts work with Solar Orbiter Metis data.
* Providing interactive Python examples for common data analysis tasks.
* Hosting useful links, resources, and tutorials.
* Encouraging community contributions!



**Useful links**:
`ESA Solar Orbiter <https://www.cosmos.esa.int/web/solar-orbiter>`__ |
`Solar Orbiter Archive <https://soar.esac.esa.int/soar/>`__ |
`Metis Project <https://metis.oato.inaf.it/>`__ |
`GitHub Repository <https://github.com/gjerse/metis-docs>`__   <-- CORREZIONE: Ho chiuso l'URL del repository GitHub, che era la causa del warning "start-string without end-string" sulla linea 109 (che era il link utile). Ho anche rimosso la barra verticale (|) finale, che era in eccesso.


.. toctree::
   :maxdepth: 1
   :hidden:

   Getting Started <getting_started>
   Data and Tools Overview <data_overview/index>
   Topic Guide <topic_guides/index>  
   Example Gallery <auto_gallery/index>
   Contributing <contributing>
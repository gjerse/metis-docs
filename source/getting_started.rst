
Getting Started with Metis Data Tools
=====================================

This page provides an overview of how to set up your Python environment and start working with **Solar Orbiter Metis data** using the official analysis tools.

This documentation and the :doc:`Example Gallery <auto_gallery/index>` build upon existing tools in the `SunPy <https://sunpy.org>`__ ecosystem, leveraging community-developed libraries for solar physics research.


1. Installing Python and Development Environment
------------------------------------------------

**Anaconda**  

A comprehensive suite for installing Python and major scientific libraries.
 
- Guide: `Installing Anaconda <https://docs.anaconda.com/anaconda/install/>`_  
- Official site: `Anaconda.org <https://anaconda.org/>`_

**Miniconda**  

A lightweight alternative to Anaconda for creating custom environments.

- Guide: `Installing Miniconda <https://docs.anaconda.com/miniconda/install/>`_

**Python.org**  

Official Python installation for minimal setups.

- Guide: `Python Installation <https://docs.python.org/3/using/index.html>`_
- Official site: `Python.org <https://www.python.org/>`_

1. Code Editors and IDEs
------------------------

**Jupyter Notebook** 

An interactive environment for writing, running, and visualizing Python code; ideal for data exploration and quick prototyping. 

- Guide: `Using Jupyter <https://jupyter-notebook.readthedocs.io/en/stable/>`_  
- Official site: `Jupyter.org <https://jupyter.org/>`_

**Visual Studio Code**  

A lightweight IDE with excellent Python support.

- Extensions: Python, Jupyter, and Pylance for linting and autocompletion.  
- Guide: `Getting Started with VS Code <https://code.visualstudio.com/docs/python/python-tutorial>`_  
- Official site: `Visual Studio Code <https://code.visualstudio.com/>`_

**Spyder**  

An IDE included with Anaconda, tailored for scientific computing.

- Ideal for beginners transitioning from MATLAB.  
- Official site: `Spyder IDE <https://www.spyder-ide.org/>`_

1. Managing Python Environments
-------------------------------

**Conda (via Anaconda or Miniconda)**  
Create and manage isolated environments.

Example::

    conda create -n myenv python=3.10
    conda activate myenv

Guide: `Conda Environments <https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html>`_

**Virtualenv**  
Alternative tool for managing Python environments.

- Guide: `Virtualenv Tutorial <https://virtualenv.pypa.io/en/latest/>`_


1. Installing the Required Packages
-----------------------------------

Before working with Metis data, you need **Python** (version 3.11+ recommended) and a few key libraries. For detailed installation instructions, including setting up a dedicated environment, please refer to the `SunPy Installation Guide <https://docs.sunpy.org/en/stable/tutorial/installation.html>`__.

**Quick Setup**

For a quick setup, you can install the core dependencies using **pip**. This command includes the Metis analysis package and essential SunPy libraries for data access:

.. code-block:: bash

    pip install metis-tools sunpy sunpy-soar 

Or, if you prefer using conda:

.. code-block:: bash

    conda install -c conda-forge metis-tools sunpy sunpy-soar 

These packages provide:

* **``metis-tools``**: The core Python package with functions specific to Metis.
* `sunpy <https://docs.sunpy.org/en/stable/>`__
* `sunpy_soar <https://docs.sunpy.org/projects/soar/en/latest/>`__: The SunPy plug-in interface for programmatic access to the Solar Orbiter Archive (SOAR) via Fido.


Verifying Your Installation
---------------------------

To ensure your setup is correct and all packages are accessible, run the following commands in your Python environment:

.. code-block:: python

    import sunpy
    import sunpy_soar
    import metis_tools

    print("SunPy version:", sunpy.__version__)
    print("Metis Tools version:", metis_tools.__version__)

If this runs without errors, you're ready to start working with Metis data!


1. Tutorials and Online Resources
---------------------------------

**Python for Astronomy**

- `AstroPython <https://astropy.org/>`_: Tutorials and resources for using Python in astronomy.
- `Solar Orbiter Data Tutorials <https://www.cosmos.esa.int/web/solar-orbiter/data-tutorials>`_: Practical examples for astrophysical data analysis.

**Interactive Python Tutorials**

- `Google Colab <https://colab.google/>`_: Online Jupyter-like environment for running Python without local setup.
- `Kaggle Notebooks <https://www.kaggle.com/code>`_: Free notebooks with Python examples for scientific computation.

**Python Basics**

- `Python.org Tutorials <https://docs.python.org/3/tutorial/>`_: Official Python documentation.
- `Real Python <https://realpython.com/>`_: Beginner-friendly Python tutorials.



First Example: Loading Metis Data
---------------------------------

The most common first step is to load data using the core Metis function, which automatically utilizes SunPy's Fido client (`sunpy.net.Fido`) to check your cache and download the file if necessary.

.. code-block:: python

    from metis_tools import metis_load

    # Define the observation time and data product (e.g., L1 image)
    time_stamp = '2024-05-15T12:00:00'

    # Load the data. This returns a SunPy Map object.
    metis_map = metis_load(time_stamp, product='L1') 

    print("Data loaded for:", metis_map.date)
    print(f"File source: {metis_map.meta.get('dsname')}")

This query quickly loads calibrated Level 1 data and verifies that your data fetching and loading routines are functioning.

---

Next Steps
----------

Once your setup is complete, check out the following resources to continue your work:

* :doc:`data_overview/index`:  
  Learn more about Metis data products, observation levels (L1, L2), and the full suite of available tools (Python and IDL).

* :doc:`data_overview/analysis_tools`: 
  Dive deeper into the specific community-developed Python functions for Metis data processing and plotting.

* :doc:`auto_gallery/index`:  
  Browse practical **interactive examples** of how to query, download, and analyze Metis observations, often provided as executable Python scripts or Jupyter Notebooks.

* :doc:`contributing`:  
  Want to contribute examples or improve the documentation? Find out how you can help!
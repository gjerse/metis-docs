
Getting Started with Metis Data Tools
=====================================

This page explains how to set up a Python environment and start working with
**Solar Orbiter Metis data** using the official analysis tools.

The examples and workflows in this documentation build on the
`SunPy <https://sunpy.org>`__ ecosystem and related community libraries for
solar physics.

If you are already familiar with Python and SunPy, you can skip directly to
the :ref:`quick-setup` section.


Python and environment requirements
-----------------------------------

To follow the examples in this documentation you need:

- **Python 3.10 or newer** (3.11+ recommended);
- a working installation of:
  - `SunPy <https://docs.sunpy.org>`__,
  - `Astropy <https://www.astropy.org>`__,
  - the Metis Python tools (e.g. ``metis-tools`` or the package you maintain).

We strongly recommend using an **isolated environment** (Conda or ``venv``) so
that package versions remain stable and reproducible.


Installing Python and Conda
---------------------------

If you do not yet have Python or Conda, you can choose one of the following
options:

**Anaconda**  
A full-featured distribution with many scientific packages pre-installed.

- Installation guide: `Installing Anaconda <https://docs.anaconda.com/anaconda/install/>`__
- Website: `Anaconda.org <https://anaconda.org/>`__

**Miniconda**  
A minimal Conda distribution; ideal if you want to install only what you need.

- Installation guide: `Installing Miniconda <https://docs.anaconda.com/miniconda/install/>`__

**Python.org**  
Official Python installer for minimal setups (you will manage packages with
``pip`` and possibly ``venv``).

- Installation guide: `Python Installation <https://docs.python.org/3/using/index.html>`__
- Website: `Python.org <https://www.python.org/>`__

For most solar physics workflows, **Miniconda or Anaconda** are the most
convenient options because they simplify the installation of scientific
libraries and the management of environments.


Managing Python environments
----------------------------

Using isolated environments avoids conflicts between packages and makes your
setup reproducible.

**Conda (via Anaconda or Miniconda)**

Example::

    conda create -n metis-env python=3.11
    conda activate metis-env

Guide: `Conda Environments <https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html>`__

**Virtualenv**

Alternative tool for managing Python environments when you do not use Conda.

- Guide: `Virtualenv <https://virtualenv.pypa.io/en/latest/>`__

Whichever tool you use, we recommend creating a dedicated environment for
Metis analysis (e.g. ``metis-env``) and documenting the package versions you
use for each project.


Code Editors and IDEs
---------------------

Any editor that supports Python and Jupyter notebooks is suitable. Common
choices in the solar physics community include:

**Jupyter Notebook / JupyterLab**  
Interactive environment ideal for data exploration, visualization, and sharing
analysis as notebooks.

- Documentation: `Jupyter Notebook <https://jupyter-notebook.readthedocs.io/>`__
- Website: `Jupyter.org <https://jupyter.org/>`__

**Visual Studio Code**  
Lightweight IDE with excellent Python and Jupyter support.

- Recommended extensions: Python, Jupyter, Pylance.
- Tutorial: `Python in VS Code <https://code.visualstudio.com/docs/python/python-tutorial>`__
- Website: `Visual Studio Code <https://code.visualstudio.com/>`__

**Spyder**  
Scientific IDE included with Anaconda, familiar to users coming from MATLAB.

- Website: `Spyder IDE <https://www.spyder-ide.org/>`__

You do not need a specific IDE to use the Metis tools; choose the environment
in which you are most productive.


.. _quick-setup:

Installing the required packages
--------------------------------

Once you have Python and an active environment, install the core libraries
needed for Metis data analysis.

For a **quick setup** with ``pip``::

    pip install metis-tools sunpy sunpy-soar

Or, if you prefer Conda::

    conda install -c conda-forge metis-tools sunpy sunpy-soar

These commands install:

- ``metis-tools``:  
  Core Python package with functions specific to Metis data (loading,
  calibration helpers, utilities).
- `SunPy <https://docs.sunpy.org>`__:  
  Community library for solar data, providing ``Map``, ``Fido``, and related
  tools.
- `sunpy-soar <https://docs.sunpy.org/projects/soar/en/latest/>`__:  
  Plug-in for programmatic access to the Solar Orbiter Archive (SOAR) via
  ``Fido``.

If you already have SunPy and only need the Metis-specific tools, you can
install just ``metis-tools``.

For more detailed instructions on creating environments and managing
dependencies, see the
`SunPy Installation Guide <https://docs.sunpy.org/en/stable/tutorial/installation.html>`__.


Verifying your installation
---------------------------

To check that your installation is working correctly, run the following in a
Python session or notebook::

    import sunpy
    import metis_tools

    print("SunPy version:", sunpy.__version__)
    print("Metis Tools version:", metis_tools.__version__)

If this runs without errors, your environment is correctly configured and you
can proceed to load and analyze Metis data.

If you encounter import errors or version conflicts, try:

- creating a fresh environment (e.g. ``conda create -n metis-test python=3.11``);
- reinstalling the packages in that environment;
- checking the :doc:`contributing` page for information on how to report issues.


Tutorials and further resources
-------------------------------

If you are new to Python or SunPy, the following resources can help you get
up to speed:

**Python and astronomy**

- `Astropy tutorials <https://learn.astropy.org>`__
- `Solar Orbiter data tutorials <https://www.cosmos.esa.int/web/solar-orbiter/data-tutorials>`__

**Interactive Python environments**

- `Google Colab <https://colab.google>`__ – run notebooks in the browser without
  local installation.
- `Kaggle Notebooks <https://www.kaggle.com/code>`__ – free notebooks with
  example code for scientific computing.

**Python basics**

- `Official Python tutorial <https://docs.python.org/3/tutorial/>`__
- `Real Python <https://realpython.com>`__ – beginner-friendly tutorials and
  articles.

These resources are optional; the examples in this documentation are designed
to be self-contained once you have installed the required packages.


Next steps
----------

Once your environment is set up and you have successfully loaded your first
Metis dataset, you can continue with:

- :doc:`data_overview/index` –  
  Learn about Metis data products, processing levels (L0–L2+), FITS structure,
  descriptors, and access methods.

- :doc:`topic_guides/index` –  
  Understand coordinates and field of view, units and uncertainties,
  calibration, polarimetry, image enhancement, and known instrumental effects.

- :doc:`auto_gallery/index` –  
  Browse reproducible examples of time-series analysis, polarimetry, CME
  tracking, and multi-instrument studies.

- :doc:`api_reference/index` –  
  Consult the auto-generated API reference for the Metis Python packages.

- :doc:`contributing` –  
  Contribute examples, report issues, or help improve this documentation.


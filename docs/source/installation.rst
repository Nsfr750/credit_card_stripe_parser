.. _installation:

Installation
============

This page contains instructions for installing the Credit Card Stripe Parser package.

.. contents:: Table of Contents
   :depth: 2
   :local:
   :backlinks: top

Prerequisites
------------

Before installing the Credit Card Stripe Parser, make sure you have the following installed:

- **Python 3.8 or higher**
  - Check your Python version by running:
    .. code-block:: bash

       python --version
       # or
       python3 --version

- **pip** (Python package installer)
  - Usually comes with Python, but you can upgrade it with:
    .. code-block:: bash

       python -m pip install --upgrade pip

- **Git** (for development installations)

Installing from PyPI
-------------------

The easiest way to install the package is using pip:

.. code-block:: bash

   pip install credit-card-stripe-parser

For a specific version, use:

.. code-block:: bash

   pip install credit-card-stripe-parser==1.2.0

Installing from Source
---------------------

If you want to install the latest development version or contribute to the project:

1. Clone the repository:

   .. code-block:: bash

      git clone https://github.com/Nsfr750/credit-card-stripe-parser.git
      cd credit-card-stripe-parser

2. Install the package in development mode:

   - For basic usage:
     .. code-block:: bash

        pip install -e .

   
   - For development (includes testing and documentation tools):
     .. code-block:: bash
     
        pip install -e ".[dev]"

   
   - For all optional dependencies:
     .. code-block:: bash
     
        pip install -e ".[all]"


Verifying the Installation
-------------------------

After installation, verify that the package was installed correctly:

.. code-block:: bash

   # Check version
   python -c "import credit_card_stripe_parser; print('Credit Card Stripe Parser version:', credit_card_stripe_parser.__version__)"
   
   # Run basic test
   python -m credit_card_stripe_parser --version

Dependencies
-----------

The package has the following dependencies:

.. list-table::
   :header-rows: 1
   :widths: 20 40 40
   
   * - Package
     - Version
     - Purpose
   * - Python
     - 3.8+
     - Core language
   * - pydantic
     - >=1.8.0,<3.0.0
     - Data validation and settings management
   * - python-dateutil
     - >=2.8.0
     - Date parsing and manipulation

Optional Dependencies
~~~~~~~~~~~~~~~~~~~~

The following dependencies are optional and only required for specific features:

- **GUI Support** (included by default):
  - `tkinter` (usually included with Python)

- **Development Dependencies** (installed with `[dev]` extra):
  - `pytest` - Testing framework
  - `black` - Code formatter
  - `isort` - Import sorter
  - `mypy` - Static type checker
  - `pylint` - Code linter

Install all optional dependencies with:

.. code-block:: bash

   pip install -e ".[all]"

Upgrading
---------

To upgrade an existing installation:

.. code-block:: bash

   pip install --upgrade credit-card-stripe-parser

For source installations, pull the latest changes and reinstall:

.. code-block:: bash

   git pull origin main
   pip install -e . --upgrade

Troubleshooting
--------------

### Permission Errors

If you encounter permission errors, try using the `--user` flag:

.. code-block:: bash

   pip install --user credit-card-stripe-parser

### Virtual Environment

For better dependency management, consider using a virtual environment:

.. code-block:: bash

   # Create a virtual environment
   python -m venv venv
   
   # Activate it (Windows)
   .\venv\Scripts\activate
   
   # Or on Unix/macOS
   source venv/bin/activate
   
   # Now install the package
   pip install credit-card-stripe-parser
- pytest-cov
- black
- flake8
- mypy
- sphinx (for documentation)

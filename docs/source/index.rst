.. _readme:

================================
Credit Card Stripe Parser
================================

**Credit Card Stripe Parser** is a Python library and command-line tool for parsing and analyzing
magnetic stripe data from credit cards. It supports both Track 1 and Track 2 formats as specified
in ISO/IEC 7811-2 and ISO/IEC 7813 standards.

.. note::
   This tool is intended for educational and testing purposes only. Always handle payment card
   data in compliance with PCI DSS requirements and applicable laws and regulations.

.. raw:: html

   <div class="badges">
   <a href="https://pypi.org/project/credit-card-stripe-parser/">
     <img src="https://img.shields.io/pypi/v/credit-card-stripe-parser.svg" alt="PyPI Version">
   </a>
   <a href="https://pypi.org/project/credit-card-stripe-parser/">
     <img src="https://img.shields.io/pypi/pyversions/credit-card-stripe-parser.svg" alt="Python Versions">
   </a>
   <a href="https://github.com/Nsfr750/credit-card-stripe-parser/blob/main/LICENSE">
     <img src="https://img.shields.io/github/license/Nsfr750/credit-card-stripe-parser.svg" alt="License">
   </a>
   <a href="https://github.com/psf/black">
     <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black">
   </a>
   </div>

   <style>
   .badges img {
       margin: 0 0.2em;
       vertical-align: middle;
   }
   </style>

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Getting Started
   
   installation
   quickstart
   usage
   examples
   gui

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: API Reference
   
   api
   api/full_track_parser
   api/models
   api/exceptions
   api/gui
   api/modules

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Project Info
   
   changelog
   contributing
   faq
   license

Key Features
===========

- Parse Track 1 and Track 2 magnetic stripe data
- Validate track data format and checksums
- Extract cardholder information, account numbers, and expiration dates
- Simple and intuitive API
- Command-line interface
- Graphical User Interface (GUI)
- Comprehensive documentation
- Extensive test coverage

Quick Start
===========

.. code-block:: bash

   # Install the package
   pip install credit-card-stripe-parser

   # Parse track data from the command line
   ccsparse "%B4111111111111111^CARDHOLDER/NAME^2512101000000000000000000000000?;4111111111111111=25121010000000000000?"

   # Or use the GUI
   ccsparse-gui

Documentation
============

For detailed documentation, please refer to the sections in the sidebar.

- :doc:`Getting Started <installation>` - Installation and basic usage
- :doc:`API Reference <api/full_track_parser>` - Detailed API documentation
- :doc:`GUI Documentation <gui>` - Guide to the graphical interface
- :doc:`Changelog <changelog>` - Release history and changes

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. |br| raw:: html

   <br />

.. |nbsp| unicode:: 0xA0
   :trim:

.. * :doc:`glossary`

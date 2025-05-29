.. _gui:

=======================
Graphical User Interface
=======================

The Credit Card Stripe Parser comes with a user-friendly GUI built with Tkinter.

.. contents:: Table of Contents
   :depth: 2
   :local:
   :backlinks: top

Launching the Application
========================

You can start the GUI in several ways:

1. From the command line:

   .. code-block:: bash

      python -m credit_card_stripe_parser gui

2. By running the main script:

   .. code-block:: bash

      python main.py

3. By directly executing the module:

   .. code-block:: bash

      python -m credit_card_stripe_parser

Interface Components
===================

The GUI consists of the following main components:

Menu Bar
--------
- **File**: Open, save, and exit options
- **Edit**: Copy, paste, and clear options
- **View**: Toggle between different views
- **Help**: Documentation and about information

Input Section
------------
- **Track 1**: Input field for Track 1 data
- **Track 2**: Input field for Track 2 data
- **Parse Button**: Process the input data
- **Clear Button**: Clear all input fields

Output Tabs
----------
- **Parsed Data**: Structured view of parsed track data
- **Raw Data**: Raw track data with formatting
- **JSON**: Parsed data in JSON format
- **Debug**: Debug information and logs

Status Bar
---------
- Shows the current status and messages

Basic Usage
==========

1. **Enter Track Data**
   - Paste your track data into the appropriate fields
   - You can enter just Track 1, just Track 2, or both

2. **Parse the Data**
   - Click the "Parse" button to process the data
   - The parsed information will be displayed in the output tabs

3. **View Results**
   - Switch between tabs to see different representations of the data
   - Use the "Copy" button to copy data to clipboard

4. **Save Results**
   - Go to *File > Save As...* to save the parsed data
   - Choose between JSON, TXT, or CSV format

Keyboard Shortcuts
=================

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Shortcut
     - Action
   * - ``Ctrl+O``
     - Open file
   * - ``Ctrl+S``
     - Save file
   * - ``Ctrl+Q``
     - Quit application
   * - ``F1``
     - Show help
   * - ``Ctrl+C``
     - Copy selected text
   * - ``Ctrl+V``
     - Paste text
   * - ``Ctrl+A``
     - Select all text
   * - ``F5``
     - Refresh the view

Advanced Features
================

Drag and Drop
------------
- Drag and drop text files containing track data onto the application window
- The file contents will be automatically loaded and parsed

Command Line Arguments
---------------------
- ``--debug``: Enable debug mode
- ``--theme [light|dark]``: Set the color theme
- ``--font-size N``: Set the font size (default: 10)

Custom Styling
-------------
- The GUI supports custom themes and styling
- Create a ``config.ini`` file in the user's config directory to customize the appearance

Troubleshooting
==============

GUI Not Starting
---------------
- Make sure you have Tkinter installed (usually included with Python)
- On Ubuntu/Debian: ``sudo apt-get install python3-tk``
- On RHEL/CentOS: ``sudo yum install python3-tkinter``

Font Issues
----------
- If text appears too small or too large, adjust the font size in the settings
- Go to *View > Font Size* to change the font size

Performance Issues
----------------
- For large files, the GUI might become unresponsive
- Use the command-line interface for batch processing large numbers of tracks

Screenshots
==========

.. figure:: /_static/screenshots/main_window.png
   :align: center
   :width: 80%
   :alt: Main Window
   :figclass: align-center

   Main Application Window

.. figure:: /_static/screenshots/parsed_view.png
   :align: center
   :width: 80%
   :alt: Parsed View
   :figclass: align-center

   Parsed Data View

See Also
--------
- :ref:`quickstart` - Getting started with the Credit Card Stripe Parser
- :ref:`api-reference` - Programmatic API documentation

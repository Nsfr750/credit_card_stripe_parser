.. _module-credit_card_stripe_parser.gui:

GUI Module
=========

.. currentmodule:: credit_card_stripe_parser.gui

Overview
--------

The GUI module provides a user-friendly interface for the Credit Card Stripe Parser.
It allows users to input track data, parse it, and view the results in a graphical interface.

Class Reference
--------------

CreditCardParserApp
~~~~~~~~~~~~~~~~~~~
.. autoclass:: CreditCardParserApp
   :members:
   :undoc-members:
   :show-inheritance:
   :exclude-members: __weakref__, __module__, __annotations__, __dict__, __dataclass_fields__, __dataclass_params__, __orig_bases__, __parameters__

   Main application class for the Credit Card Stripe Parser GUI.
   
   This class creates and manages the main application window and all its widgets.
   
   .. automethod:: __init__
   .. automethod:: create_widgets
   .. automethod:: create_menu
   .. automethod:: parse_track
   .. automethod:: clear_fields
   .. automethod:: show_about
   .. automethod:: show_help
   .. automethod:: on_closing
   .. automethod:: run

Example Usage
------------

Running the GUI Application
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from credit_card_stripe_parser.gui import CreditCardParserApp
   
   if __name__ == "__main__":
       app = CreditCardParserApp()
       app.run()

Or from the command line:

.. code-block:: bash

   python -m credit_card_stripe_parser.gui

Keyboard Shortcuts
-----------------

- **Ctrl+Q**: Quit the application
- **Ctrl+C**: Copy selected text
- **Ctrl+V**: Paste text
- **F1**: Show help
- **F2**: Show about dialog
- **F5**: Parse track data
- **Escape**: Clear all fields

Troubleshooting
--------------

Common Issues
~~~~~~~~~~~~

1. **GUI doesn't start**
   - Ensure you have Python 3.8 or later installed
   - Make sure all dependencies are installed (Tkinter is required)
   - Check the console for any error messages

2. **Text not displaying correctly**
   - Try changing the system font settings
   - Ensure your system's DPI settings are not causing scaling issues

3. **Window size issues**
   - The window is designed to be resizable
   - Minimum size constraints are set to prevent UI elements from overlapping

See Also
--------
- :class:`~credit_card_stripe_parser.full_track_parser.FullTrackParser` - The parser implementation used by the GUI
- :mod:`~credit_card_stripe_parser.models` - Data models used for storing parsed track data
- :mod:`~credit_card_stripe_parser.exceptions` - Exceptions that might be raised during parsing

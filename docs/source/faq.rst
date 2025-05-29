.. _faq:

Frequently Asked Questions (FAQ)
===============================

This page answers common questions about the Credit Card Stripe Parser.

.. contents:: Table of Contents
   :depth: 2
   :local:
   :backlinks: top

General Questions
----------------

What is the Credit Card Stripe Parser?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The Credit Card Stripe Parser is a Python library and command-line tool for parsing and analyzing
magnetic stripe data from credit and debit cards. It supports both Track 1 and Track 2 formats as
specified in ISO/IEC 7811-2 and ISO/IEC 7813 standards.

Is this tool legal to use?
~~~~~~~~~~~~~~~~~~~~~~~~~
Yes, the tool itself is legal to use. However, how you use it must comply with all applicable laws
and regulations. Always ensure you have proper authorization before accessing or processing
payment card data.

Is this tool PCI DSS compliant?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This tool can be used as part of a PCI DSS compliant environment, but proper security measures must
be in place. The tool does not store or transmit card data, but you are responsible for ensuring
that your usage complies with PCI DSS requirements.

Installation Issues
------------------

I'm getting a "ModuleNotFoundError: No module named 'tkinter'" error
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This error occurs when Tkinter is not installed on your system. To fix it:

- On Ubuntu/Debian: ``sudo apt-get install python3-tk``
- On RHEL/CentOS: ``sudo yum install python3-tkinter``
- On macOS: Tkinter is usually included with the Python installation from python.org

How do I install a specific version of the package?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You can install a specific version using pip:

.. code-block:: bash

   pip install credit-card-stripe-parser==1.2.0

Usage Questions
--------------

What's the difference between Track 1 and Track 2?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- **Track 1**: Contains more information including the cardholder's name, but is less commonly used.
  Format: ``%B[PAN]^[NAME]^[YYMM]...?``
  
- **Track 2**: More commonly used, contains essential card data in a more compact format.
  Format: ``;[PAN]=[YYMM]...?``

How do I handle different character encodings?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The parser assumes UTF-8 encoding by default. If you're working with different encodings, you can
convert the track data to UTF-8 before parsing:

.. code-block:: python

   # Example: Convert from Latin-1 to UTF-8
   track_data = track_data_latin1.decode('latin-1').encode('utf-8')
   result = parser.parse(track_data)

Error Messages
-------------

"Invalid track format" error
~~~~~~~~~~~~~~~~~~~~~~~~~~~
This error occurs when the track data doesn't match the expected format. Check that:

1. The track starts with the correct start sentinel (``%`` for Track 1, ``;`` for Track 2)
2. The track ends with a question mark (``?``)
3. The data between matches the expected format for the track type

"LRC validation failed" error
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The Longitudinal Redundancy Check (LRC) is a simple checksum used to verify the integrity of the
track data. This error suggests that the data may be corrupted or the LRC character is missing.

"Checksum validation failed" error
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This indicates that the Luhn checksum for the Primary Account Number (PAN) is invalid. This could
mean:

1. The PAN is incorrect or mistyped
2. The track data is corrupted
3. The card is not following the standard Luhn algorithm (rare)

Performance
----------

Is this library fast enough for high-volume processing?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Yes, the library is designed to be efficient. For very high volumes (millions of tracks), consider:

1. Using the command-line interface for batch processing
2. Processing tracks in parallel using Python's multiprocessing
3. Using a more performant language for the core parsing if needed

How can I improve parsing performance?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. Reuse the parser instance instead of creating a new one for each track
2. Process tracks in batches
3. Use the ``parse_track1`` or ``parse_track2`` methods if you only need one track
4. Disable validation for known-good data (use with caution)

Security
--------

Is it safe to log parsed card data?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
No, you should never log full track data or sensitive card information. If you need to log for
debugging purposes, make sure to mask sensitive data:

.. code-block:: python

   def mask_pan(pan):
       if len(pan) <= 4:
           return pan
       return "*" * (len(pan) - 4) + pan[-4:]

How should I store parsed card data?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In general, you should avoid storing card data unless absolutely necessary. If you must store it:

1. Use strong encryption
2. Ensure your storage is PCI DSS compliant
3. Implement proper access controls
4. Consider using a tokenization service

Troubleshooting
--------------

The parser works for some cards but not others
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This could be due to:

1. Non-standard card formats
2. Custom encoding or encryption
3. Corrupted track data

Try using the ``--debug`` flag to see more detailed information about the parsing process.

I'm getting inconsistent results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Make sure that:

1. The track data is being read correctly (no extra spaces or characters)
2. The encoding is consistent
3. You're using the latest version of the library

If the issue persists, please open an issue with a sample of the track data (with sensitive
information redacted).

Feature Requests
---------------

Can you add support for [feature]?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
We welcome feature requests! Please open an issue on the GitHub repository with details about the
feature you'd like to see.

How can I contribute?
~~~~~~~~~~~~~~~~~~~~
Contributions are welcome! See the :ref:`contributing` guide for more information.

See Also
--------
- :ref:`quickstart` - Getting started guide
- :ref:`examples` - Code examples
- :ref:`api-reference` - Complete API reference

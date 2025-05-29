.. _quickstart:

Quickstart Guide
===============

This guide will help you quickly get started with the Credit Card Stripe Parser.

.. contents:: Table of Contents
   :depth: 2
   :local:
   :backlinks: top

Command Line Usage
-----------------

Basic parsing of a track:

.. code-block:: bash

   python -m credit_card_stripe_parser parse-track "%B4111111111111111^CARDHOLDER/NAME^2512101000000000000000000000000?;4111111111111111=25121010000000000000?"

Parse a specific track:

.. code-block:: bash

   # Parse only track 1
   python -m credit_card_stripe_parser parse-track --track 1 "%B4111111111111111^CARDHOLDER/NAME^2512101000000000000000000000000?"

   # Parse only track 2
   python -m credit_card_stripe_parser parse-track --track 2 ";4111111111111111=25121010000000000000?"

Using the GUI
------------

1. Start the GUI application:

   .. code-block:: bash

      python -m credit_card_stripe_parser gui

2. Enter your track data in the appropriate fields
3. Click "Parse" to process the data
4. View the parsed results in the output tabs

Python API
---------

Parsing track data programmatically:

.. code-block:: python

   from credit_card_stripe_parser import FullTrackParser
   
   # Create a parser instance
   parser = FullTrackParser()
   
   # Parse full track data (both tracks)
   track_data = "%B4111111111111111^CARDHOLDER/NAME^2512101000000000000000000000000?;4111111111111111=25121010000000000000?"
   result = parser.parse(track_data)
   
   # Access parsed data
   print(f"Primary Account Number: {result.primary_account_number}")
   print(f"Cardholder Name: {result.cardholder_name}")
   print(f"Expiration Date: {result.expiration_date}")
   print(f"Service Code: {result.service_code}")

Parsing Individual Tracks
------------------------

You can also parse individual tracks:

.. code-block:: python

   # Parse track 1
   track1 = "%B4111111111111111^CARDHOLDER/NAME^2512101000000000000000000000000?"
   result1 = parser.parse_track1(track1)
   
   # Parse track 2
   track2 = ";4111111111111111=25121010000000000000?"
   result2 = parser.parse_track2(track2)

Error Handling
-------------

The parser raises specific exceptions for different error conditions:

.. code-block:: python

   from credit_card_stripe_parser.exceptions import (
       TrackValidationError,
       LRCValidationError,
       ChecksumValidationError
   )
   
   try:
       result = parser.parse(invalid_track_data)
   except TrackValidationError as e:
       print(f"Invalid track data: {e}")
   except LRCValidationError as e:
       print(f"LRC validation failed: {e}")
   except ChecksumValidationError as e:
       print(f"Checksum validation failed: {e}")

Next Steps
----------

- Learn more about :ref:`usage`
- Explore the :ref:`API Reference <apiref>`
- Check out the :ref:`examples` section for more advanced use cases
- Read the :ref:`changelog` for recent changes and updates

.. _module-credit_card_stripe_parser.full_track_parser:

FullTrackParser
==============

.. currentmodule:: credit_card_stripe_parser.full_track_parser

.. autoclass:: FullTrackParser
   :members:
   :undoc-members:
   :show-inheritance:
   :exclude-members: __weakref__, __module__, __annotations__, __dict__, __dataclass_fields__, __dataclass_params__, __orig_bases__, __parameters__

   The FullTrackParser class provides functionality to parse credit card track data from magnetic stripes.
   It supports parsing of both Track 1 and Track 2 data, either separately or combined.

.. note::
   This class returns instances of :class:`~credit_card_stripe_parser.models.track_one_model.TrackOneModel`,
   :class:`~credit_card_stripe_parser.models.track_two_model.TrackTwoModel`, or
   :class:`~credit_card_stripe_parser.models.full_track_data_model.FullTrackDataModel` depending on the method called.

   .. automethod:: __init__
   .. automethod:: parse
   .. automethod:: parse_track1
   .. automethod:: parse_track2
   .. automethod:: parse_full_track
   .. automethod:: validate_track
   .. automethod:: calculate_lrc
   .. automethod:: calculate_checksum

Example Usage
------------

Parsing Full Track Data
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from credit_card_stripe_parser import FullTrackParser
   
   # Initialize the parser
   parser = FullTrackParser()
   
   # Parse full track data (both tracks)
   track_data = "%B4111111111111111^CARDHOLDER/NAME^2512101000000000000000000000000?;4111111111111111=25121010000000000000?"
   result = parser.parse(track_data)
   
   # Access parsed data
   print(f"Primary Account Number: {result.primary_account_number}")
   print(f"Cardholder Name: {result.cardholder_name}")
   print(f"Expiration Date: {result.expiration_date}")
   print(f"Service Code: {result.service_code}")
   print(f"Discretionary Data: {result.discretionary_data}")

Parsing Individual Tracks
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Parse individual tracks
   track1 = "%B4111111111111111^CARDHOLDER/NAME^2512101000000000000000000000000?"
   track2 = ";4111111111111111=25121010000000000000?"
   
   # Parse Track 1
   result1 = parser.parse_track1(track1)
   print(f"Track 1 - PAN: {result1.primary_account_number}")
   print(f"Track 1 - Cardholder: {result1.cardholder_name}")
   
   # Parse Track 2
   result2 = parser.parse_track2(track2)
   print(f"Track 2 - PAN: {result2.primary_account_number}")
   print(f"Track 2 - Expiry: {result2.expiration_date}")

Error Handling
~~~~~~~~~~~~~

.. code-block:: python

   from credit_card_stripe_parser.exceptions import TrackValidationError, LRCValidationError, ChecksumValidationError
   
   try:
       # This will raise an exception for invalid track data
       parser.parse("INVALID_TRACK_DATA")
   except TrackValidationError as e:
       print(f"Invalid track data: {e}")
   except LRCValidationError as e:
       print(f"LRC validation failed: {e}")
   except ChecksumValidationError as e:
       print(f"Checksum validation failed: {e}")
   except Exception as e:
       print(f"An unexpected error occurred: {e}")

See Also
--------
- :ref:`models` - Data models used by the parser
- :ref:`exceptions` - Custom exceptions raised by the parser
- :ref:`constants` - Constants used throughout the library

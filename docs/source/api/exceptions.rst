.. _exceptions:

Exceptions
=========

This module contains all custom exceptions used in the Credit Card Stripe Parser.

.. currentmodule:: credit_card_stripe_parser.exceptions

Overview
--------

The exceptions are organized in a hierarchy, with a base exception that all other
exceptions inherit from. This allows you to catch specific exceptions or all
parser-related exceptions by catching the base exception.

Exception Hierarchy
------------------

.. code-block:: text

   Exception
   └── CreditCardParserError (base)
       ├── TrackValidationError
       │   ├── Track1ValidationError
       │   ├── Track2ValidationError
       │   └── TrackFormatError
       ├── LRCValidationError
       └── ChecksumValidationError

Reference
---------

Base Exception
~~~~~~~~~~~~~
.. autoexception:: CreditCardParserError
   :show-inheritance:
   :members: __init__, __str__
   :exclude-members: __weakref__, __module__, __annotations__, __dict__

   Base exception for all credit card parser exceptions.
   This exception should be used as the base class for all custom exceptions
   in the module to allow users to catch all parser-related exceptions.

   Example:

   .. code-block:: python

      try:
          # Code that might raise a parser exception
          pass
      except CreditCardParserError as e:
          # Handle any parser-related exception
          print(f"Parser error: {e}")


Track Validation Exceptions
~~~~~~~~~~~~~~~~~~~~~~~~~
.. autoexception:: TrackValidationError
   :show-inheritance:
   :members: __init__, __str__
   :exclude-members: __weakref__, __module__, __annotations__, __dict__
   
   Base exception for track validation errors.
   Raised when there is a general validation error with track data.

   Example:

   .. code-block:: python

      try:
          parser.validate_track("INVALID_TRACK_DATA")
      except TrackValidationError as e:
          print(f"Track validation failed: {e}")

.. autoexception:: Track1ValidationError
   :show-inheritance:
   :members: __init__, __str__
   :exclude-members: __weakref__, __module__, __annotations__, __dict__
   
   Raised when there is an error validating Track 1 data.
   This could be due to invalid format, missing fields, or invalid values.

   Example:

   .. code-block:: python

      try:
          parser.parse_track1("%B1234567890123456^INVALID/NAME^2512?")
      except Track1ValidationError as e:
          print(f"Track 1 validation failed: {e}")

.. autoexception:: Track2ValidationError
   :show-inheritance:
   :members: __init__, __str__
   :exclude-members: __weakref__, __module__, __annotations__, __dict__
   
   Raised when there is an error validating Track 2 data.
   This could be due to invalid format, missing fields, or invalid values.

   Example:

   .. code-block:: python

      try:
          parser.parse_track2(";1234567890123456=2512?")
      except Track2ValidationError as e:
          print(f"Track 2 validation failed: {e}")

.. autoexception:: TrackFormatError
   :show-inheritance:
   :members: __init__, __str__
   :exclude-members: __weakref__, __module__, __annotations__, __dict__
   
   Raised when the track data format is invalid.
   This could be due to missing start/end sentinels, incorrect field separators,
   or other formatting issues.

   Example:

   .. code-block:: python

      try:
          # Missing start sentinel
          parser.parse("B1234567890123456^CARDHOLDER/NAME^2512?")
      except TrackFormatError as e:
          print(f"Invalid track format: {e}")

LRC Validation Exception
~~~~~~~~~~~~~~~~~~~~~~~
.. autoexception:: LRCValidationError
   :show-inheritance:
   :members: __init__, __str__
   :exclude-members: __weakref__, __module__, __annotations__, __dict__
   
   Raised when the LRC (Longitudinal Redundancy Check) validation fails.
   The LRC is a form of checksum used to verify the integrity of the track data.

   Example:

   .. code-block:: python

      try:
          # Track data with invalid LRC
          parser.parse("%B1234567890123456^CARDHOLDER/NAME^2512101000000000000000000000000X")
      except LRCValidationError as e:
          print(f"LRC validation failed: {e}")

Checksum Validation Exception
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. autoexception:: ChecksumValidationError
   :show-inheritance:
   :members: __init__, __str__
   :exclude-members: __weakref__, __module__, __annotations__, __dict__
   
   Raised when the checksum validation fails for track data.
   This typically indicates that the track data has been corrupted or tampered with.

   Example:

   .. code-block:: python

      try:
          # Track data with invalid checksum
          parser.parse("%B1234567890123456^CARDHOLDER/NAME^2512101000000000000000000000000?")
      except ChecksumValidationError as e:
          print(f"Checksum validation failed: {e}")

Example Usage
------------

.. code-block:: python

   from credit_card_stripe_parser import FullTrackParser
   from credit_card_stripe_parser.exceptions import (
       CreditCardParserError,
       TrackValidationError,
       LRCValidationError,
       ChecksumValidationError
   )
   
   parser = FullTrackParser()
   
   try:
       result = parser.parse(invalid_track_data)
   except TrackValidationError as e:
       print(f"Invalid track data: {e}")
   except LRCValidationError as e:
       print(f"LRC validation failed: {e}")
   except ChecksumValidationError as e:
       print(f"Checksum validation failed: {e}")
   except CreditCardParserError as e:
       print(f"Parser error: {e}")
   except Exception as e:
       print(f"Unexpected error: {e}")

Best Practices
-------------

1. Always catch the most specific exception first, then more general ones.
2. Use the base ``CreditCardParserError`` to catch any parser-related exceptions.
3. Include meaningful error messages when raising exceptions.
4. Log exceptions with appropriate context for debugging.

See Also
--------
- :ref:`module-credit_card_stripe_parser.full_track_parser` - Where these exceptions are typically raised
- :ref:`models` - Data models used for validation

API Reference
============

This document provides detailed information about the public API of the Credit Card Stripe Parser library.

FullTrackParser
---------------

.. autoclass:: credit_card_stripe_parser.full_track_parser.FullTrackParser
   :members:
   :inherited-members:
   :show-inheritance:

   The main parser class that handles parsing of credit card track data.

   .. automethod:: __init__
   .. automethod:: parse
   .. automethod:: parse_track_one
   .. automethod:: parse_track_two
   .. automethod:: try_parse_track_one
   .. automethod:: try_parse_track_two
   .. automethod:: validate_track_one
   .. automethod:: validate_track_two
   .. automethod:: calculate_lrc

Data Models
-----------

FullTrackDataModel
~~~~~~~~~~~~~~~~~~

.. autoclass:: credit_card_stripe_parser.models.full_track_data_model.FullTrackDataModel
   :members:
   :show-inheritance:

   Represents the complete parsed data from both Track 1 and Track 2.

   .. autoattribute:: track_one
   .. autoattribute:: track_two
   .. autoattribute:: is_track_one_valid
   .. autoattribute:: is_track_two_valid
   .. autoattribute:: source_string

TrackOneModel
~~~~~~~~~~~~~

.. autoclass:: credit_card_stripe_parser.models.track_one_model.TrackOneModel
   :members:
   :show-inheritance:

   Represents the parsed data from Track 1.

   
   .. autoattribute:: format_code
   .. autoattribute:: pan
   .. autoattribute:: card_holder_name
   .. autoattribute:: expiration_date
   .. autoattribute:: service_code
   .. autoattribute:: discretionary_data
   .. autoattribute:: source_string

TrackTwoModel
~~~~~~~~~~~~~

.. autoclass:: credit_card_stripe_parser.models.track_two_model.TrackTwoModel
   :members:
   :show-inheritance:

   Represents the parsed data from Track 2.
   
   .. autoattribute:: pan
   .. autoattribute:: expiration_date
   .. autoattribute:: service_code
   .. autoattribute:: pvki
   .. autoattribute:: pvv_or_cvv
   .. autoattribute:: discretionary_data
   .. autoattribute:: source_string

Exceptions
----------

InvalidTrackDataException
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoexception:: credit_card_stripe_parser.exceptions.InvalidTrackDataException
   :members:

   Base exception for all track data related errors.

InvalidTrackOneException
~~~~~~~~~~~~~~~~~~~~~~~

.. autoexception:: credit_card_stripe_parser.exceptions.InvalidTrackOneException
   :members:

   Raised when there is an error parsing Track 1 data.

InvalidTrackTwoException
~~~~~~~~~~~~~~~~~~~~~~~

.. autoexception:: credit_card_stripe_parser.exceptions.InvalidTrackTwoException
   :members:

   Raised when there is an error parsing Track 2 data.

LRCValidationException
~~~~~~~~~~~~~~~~~~~~~

.. autoexception:: credit_card_stripe_parser.exceptions.LRCValidationException
   :members:

   Raised when LRC (Longitudinal Redundancy Check) validation fails.

Constants
---------

.. automodule:: credit_card_stripe_parser.constants
   :members:
   :show-inheritance:

   Module containing various constants used throughout the library.

Type Definitions
---------------

.. automodule:: credit_card_stripe_parser.types
   :members:
   :show-inheritance:

   Module containing type definitions used throughout the library.

.. _models:

==========
Data Models
==========

This module contains the data models used throughout the Credit Card Stripe Parser.

.. currentmodule:: credit_card_stripe_parser.models

BaseModel
---------
.. autoclass:: BaseModel
   :members:
   :undoc-members:
   :show-inheritance:
   :exclude-members: __weakref__, __module__, __annotations__, __dict__, __dataclass_fields__, __dataclass_params__, __orig_bases__, __parameters__

   Base model class that provides common functionality for all data models.

Track Data Models
----------------

Track1Data
~~~~~~~~~~
.. autoclass:: Track1Data
   :members:
   :undoc-members:
   :show-inheritance:
   :exclude-members: __weakref__, __module__, __annotations__, __dict__, __dataclass_fields__, __dataclass_params__, __orig_bases__, __parameters__

   Model representing Track 1 data from a magnetic stripe card.


Track2Data
~~~~~~~~~~
.. autoclass:: Track2Data
   :members:
   :undoc-members:
   :show-inheritance:
   :exclude-members: __weakref__, __module__, __annotations__, __dict__, __dataclass_fields__, __dataclass_params__, __orig_bases__, __parameters__

   Model representing Track 2 data from a magnetic stripe card.

Pydantic Models
--------------

TrackOneModel
~~~~~~~~~~~~~
.. currentmodule:: credit_card_stripe_parser.models.track_one_model

.. autoclass:: TrackOneModel
   :members:
   :undoc-members:
   :show-inheritance:
   :exclude-members: __weakref__, __module__, __annotations__, __dict__, __dataclass_fields__, __dataclass_params__, __orig_bases__, __parameters__
   :noindex:

   Pydantic model for Track 1 data with validation.
   
   This model is returned by :meth:`~credit_card_stripe_parser.full_track_parser.FullTrackParser.parse_track1`
   and contains all the fields from Track 1 of a magnetic stripe.
   
   Example:
   
   .. code-block:: python
   
      from credit_card_stripe_parser import FullTrackParser
      
      parser = FullTrackParser()
      track1 = "%B4111111111111111^CARDHOLDER/NAME^2512101000000000000000000000000?"
      result = parser.parse_track1(track1)
      print(f"Cardholder: {result.cardholder_name}")
      print(f"PAN: {result.primary_account_number}")

TrackTwoModel
~~~~~~~~~~~~~
.. currentmodule:: credit_card_stripe_parser.models.track_two_model

.. autoclass:: TrackTwoModel
   :members:
   :undoc-members:
   :show-inheritance:
   :exclude-members: __weakref__, __module__, __annotations__, __dict__, __dataclass_fields__, __dataclass_params__, __orig_bases__, __parameters__
   :noindex:

   Pydantic model for Track 2 data with validation.
   
   This model is returned by :meth:`~credit_card_stripe_parser.full_track_parser.FullTrackParser.parse_track2`
   and contains all the fields from Track 2 of a magnetic stripe.
   
   Example:
   
   .. code-block:: python
   
      from credit_card_stripe_parser import FullTrackParser
      
      parser = FullTrackParser()
      track2 = ";4111111111111111=25121010000000000000?"
      result = parser.parse_track2(track2)
      print(f"PAN: {result.primary_account_number}")
      print(f"Expiry: {result.expiration_date}")

FullTrackDataModel
~~~~~~~~~~~~~~~~~~
.. currentmodule:: credit_card_stripe_parser.models.full_track_data_model

.. autoclass:: FullTrackDataModel
   :members:
   :undoc-members:
   :show-inheritance:
   :exclude-members: __weakref__, __module__, __annotations__, __dict__, __dataclass_fields__, __dataclass_params__, __orig_bases__, __parameters__
   :noindex:

   Pydantic model that combines both Track 1 and Track 2 data.
   
   This model is returned by :meth:`~credit_card_stripe_parser.full_track_parser.FullTrackParser.parse`
   when both tracks are provided. It contains all fields from both tracks with proper validation.
   
   Example:
   
   .. code-block:: python
   
      from credit_card_stripe_parser import FullTrackParser
      
      parser = FullTrackParser()
      full_track = "%B4111111111111111^CARDHOLDER/NAME^2512101000000000000000000000000?;4111111111111111=25121010000000000000?"
      result = parser.parse(full_track)
      print(f"Cardholder: {result.track1.cardholder_name}")
      print(f"PAN: {result.track1.primary_account_number}")
      print(f"Expiry: {result.track2.expiration_date}")

Example Usage
------------

.. code-block:: python

   from credit_card_stripe_parser.models import (
       Track1Data,
       Track2Data,
       TrackOneModel,
       TrackTwoModel,
       FullTrackDataModel
   )
   
   # Create a Track1Data instance
   track1 = Track1Data(
       format_code='B',
       primary_account_number='4111111111111111',
       cardholder_name='CARDHOLDER/NAME',
       expiration_date='2512',
       service_code='101',
       discretionary_data='000000000000000000000000000',
       lrc='?'
   )
   
   # Create a Track2Data instance
   track2 = Track2Data(
       primary_account_number='4111111111111111',
       expiration_date='2512',
       service_code='101',
       pvki='',
       pvv='',
       discretionary_data='0000000000000000',
       lrc='?'
   )
   
   # Create a TrackOneModel instance
   track1_model = TrackOneModel(
       format_code='B',
       primary_account_number='4111111111111111',
       cardholder_name='CARDHOLDER/NAME',
       expiration_date='2512',
       service_code='101',
       discretionary_data='000000000000000000000000000',
       lrc='?'
   )
   
   # Create a TrackTwoModel instance (needed for FullTrackDataModel)
   track2_model = TrackTwoModel(
       primary_account_number='4111111111111111',
       expiration_date='2512',
       service_code='101',
       pvki='',
       pvv='',
       discretionary_data='0000000000000000',
       lrc='?'
   )
   
   # Create a FullTrackDataModel instance
   full_track = FullTrackDataModel(
       track1=track1_model,
       track2=track2_model,
       is_track1_valid=True,
       is_track2_valid=True,
       validation_errors=[],
       validation_warnings=[]
   )
   
   # Access data
   print(f"Cardholder: {full_track.track1.cardholder_name}")
   print(f"Expires: {full_track.track2.expiration_date}")

See Also
--------
- :ref:`module-credit_card_stripe_parser.full_track_parser` - The main parser class that uses these models
- :ref:`exceptions` - Exceptions related to model validation

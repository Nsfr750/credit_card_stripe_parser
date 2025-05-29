.. _constants:

Constants
========

This module contains constants used throughout the Credit Card Stripe Parser.

.. automodule:: credit_card_stripe_parser.constants
   :members:
   :undoc-members:
   :show-inheritance:

Track Format Constants
---------------------

Track 1 Format
~~~~~~~~~~~~~~
.. autodata:: TRACK1_FORMAT
   :annotation: = "^%([A-Z])([0-9]{1,19})\^([^\^]{2,26})\^([0-9]{4}|\^)([0-9]{3}|\^)([^\?]+)\?$"

   Regular expression pattern for matching Track 1 data format.
   
   Groups:
   - Format code (A-Z)
   - Primary Account Number (1-19 digits)
   - Cardholder Name (2-26 chars)
   - Expiration Date (YYMM) or ^
   - Service Code (3 digits) or ^
   - Discretionary Data

Track 2 Format
~~~~~~~~~~~~~~
.. autodata:: TRACK2_FORMAT
   :annotation: = "^;([0-9]{1,19})=([0-9]{4})([0-9]{3})([^?]+)\?$"

   Regular expression pattern for matching Track 2 data format.
   
   Groups:
   - Primary Account Number (1-19 digits)
   - Expiration Date (YYMM)
   - Service Code (3 digits)
   - Discretionary Data

Service Code Values
------------------

Interchange Rules
~~~~~~~~~~~~~~~~
.. autodata:: INTERCHANGE_RULES
   :annotation: = {
       '1': 'International interchange OK',
       '2': 'International interchange, use IC (chip) where feasible',
       '5': 'National interchange only except under bilateral agreement',
       '6': 'National interchange only, use IC (chip) where feasible',
       '7': 'No interchange except under bilateral agreement',
       '9': 'Test'
   }


Authorization Processing
~~~~~~~~~~~~~~~~~~~~~~
.. autodata:: AUTHORIZATION_PROCESSING
   :annotation: = {
       '0': 'Normal',
       '2': 'By issuer',
       '4': 'By issuer unless explicit bilateral agreement applies'
   }


Allowed Services
~~~~~~~~~~~~~~~
.. autodata:: ALLOWED_SERVICES
   :annotation: = {
       '0': 'No restrictions',
       '1': 'No cash',
       '2': 'No goods',
       '3': 'No services',
       '4': 'No cashback',
       '5': 'No cash, except under bilateral agreement',
       '6': 'No goods or services, except under bilateral agreement'
   }

PIN Requirements
~~~~~~~~~~~~~~~
.. autodata:: PIN_REQUIREMENTS
   :annotation: = {
       '0': 'PIN required',
       '1': 'None',
       '2': 'None (prompt if PIN pad capable)'
   }

Example Usage
------------

.. code-block:: python

   from credit_card_stripe_parser.constants import (
       TRACK1_FORMAT,
       TRACK2_FORMAT,
       INTERCHANGE_RULES,
       AUTHORIZATION_PROCESSING,
       ALLOWED_SERVICES,
       PIN_REQUIREMENTS
   )
   
   # Check if a track matches the expected format
   import re
   
   track1 = "%B4111111111111111^CARDHOLDER/NAME^2512101000000000000000000000000?"
   if re.match(TRACK1_FORMAT, track1):
       print("Valid Track 1 format")
   
   # Look up service code meaning
   service_code = "101"
   interchange = service_code[0]
   auth_processing = service_code[1]
   allowed_services = service_code[2]
   
   print(f"Interchange: {INTERCHANGE_RULES.get(interchange, 'Unknown')}")
   print(f"Auth Processing: {AUTHORIZATION_PROCESSING.get(auth_processing, 'Unknown')}")
   print(f"Allowed Services: {ALLOWED_SERVICES.get(allowed_services, 'Unknown')}")

See Also
--------
- :ref:`module-credit_card_stripe_parser.full_track_parser` - Where these constants are used
- :ref:`models` - Data models that use these constants for validation

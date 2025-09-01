# API Reference

## Core Functions

### `parse_track_data(track_data: str) -> dict`
Parse magnetic stripe data from credit cards.

**Parameters:**
- `track_data` (str): Raw track data string from a credit card's magnetic stripe

**Returns:**
- `dict`: Parsed track data with the following structure:
  ```python
  {
      'track_type': str,          # '1' for Track 1, '2' for Track 2
      'pan': str,                 # Primary Account Number
      'cardholder_name': str,     # Cardholder name (Track 1 only)
      'expiry_date': str,         # Expiration date (YYMM)
      'service_code': str,        # Service code
      'discretionary_data': str,  # Discretionary data
      'valid': bool,              # Whether the card number is valid
      'card_type': str,           # Card type (Visa, Mastercard, etc.)
  }
  ```

**Raises:**
- `InvalidTrackDataError`: If the track data is malformed or invalid

### `validate_pan(pan: str) -> bool`
Validate a credit card number using the Luhn algorithm.

**Parameters:**
- `pan` (str): Primary Account Number to validate

**Returns:**
- `bool`: True if the PAN is valid, False otherwise

## Models

### `TrackOneData`
Represents parsed Track 1 data.

**Attributes:**
- `format_code` (str): Format code ('A', 'B', or 'C')
- `pan` (str): Primary Account Number
- `cardholder_name` (str): Name of the cardholder
- `expiry_date` (str): Expiration date (YYMM)
- `service_code` (str): Service code
- `discretionary_data` (str): Discretionary data

### `TrackTwoData`
Represents parsed Track 2 data.

**Attributes:**
- `pan` (str): Primary Account Number
- `expiry_date` (str): Expiration date (YYMM)
- `service_code` (str): Service code
- `discretionary_data` (str): Discretionary data

## Exceptions

### `InvalidTrackDataError`
Raised when track data cannot be parsed due to invalid format.

**Attributes:**
- `message` (str): Explanation of the error
- `track_data` (str): The original track data that caused the error

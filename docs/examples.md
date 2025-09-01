# Usage Examples

## Basic Usage

### Parsing Track 1 Data
```python
from credit_card_stripe_parser import parse_track_data

# Example Track 1 data
track1 = "%B4111111111111111^CARDHOLDER/NAME^25121010000000000000?"
result = parse_track_data(track1)

print(f"Card Number: {result['pan']}")
print(f"Cardholder: {result['cardholder_name']}")
print(f"Expires: {result['expiry_date'][:2]}/{result['expiry_date'][2:]}")
print(f"Valid: {result['valid']}")
print(f"Card Type: {result['card_type']}")
```

### Parsing Track 2 Data
```python
from credit_card_stripe_parser import parse_track_data

# Example Track 2 data
track2 = ";4111111111111111=25121010000000000000?"
result = parse_track_data(track2)

print(f"Card Number: {result['pan']}")
print(f"Expires: {result['expiry_date'][:2]}/{result['expiry_date'][2:]}")
print(f"Valid: {result['valid']}")
```

## Advanced Usage

### Batch Processing
```python
from credit_card_stripe_parser import parse_track_data

# List of track data to process
tracks = [
    "%B4111111111111111^CARDHOLDER/NAME^25121010000000000000?",
    ";4111111111111111=25121010000000000000?",
    "%B5555555555554444^JOHN/DOE^26129910000000000000?"
]

for track in tracks:
    try:
        result = parse_track_data(track)
        print(f"\nParsed Card: {result['pan']}")
        print(f"Type: {result['card_type']}")
        print(f"Expiry: {result['expiry_date'][:2]}/{result['expiry_date'][2:]}")
    except Exception as e:
        print(f"\nError processing track data: {e}")
```

### Validating Card Numbers
```python
from credit_card_stripe_parser import validate_pan

# List of card numbers to validate
card_numbers = [
    "4111111111111111",  # Valid Visa
    "1234567890123456",  # Invalid
    "5555555555554444"   # Valid Mastercard
]

for pan in card_numbers:
    is_valid = validate_pan(pan)
    print(f"Card {pan}: {'Valid' if is_valid else 'Invalid'}")
```

## Error Handling

### Catching Parsing Errors
```python
from credit_card_stripe_parser import parse_track_data, InvalidTrackDataError

track_data = "invalid_track_data"

try:
    result = parse_track_data(track_data)
    print(f"Parsed data: {result}")
except InvalidTrackDataError as e:
    print(f"Error: {e.message}")
    print(f"Invalid track data: {e.track_data}")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")
```

## Integration with Other Systems

### CSV Processing
```python
import csv
from credit_card_stripe_parser import parse_track_data

# Example CSV processing
with open('card_data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            result = parse_track_data(row['track_data'])
            print(f"Processed card: {result['pan']} ({result['card_type']})")
        except Exception as e:
            print(f"Error processing row: {row}")
            print(f"Error: {str(e)}")
```

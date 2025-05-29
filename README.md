# Credit Card Stripe Parser

A Python implementation of a credit card stripe parser that can parse Track 1 and Track 2 data from magnetic stripe cards according to ISO 7811-2 standards. The package includes both a Python API and a user-friendly GUI application.

## Features

- **Track Parsing**
  - Parse Track 1 and Track 2 data from magnetic stripe cards
  - Support for both with and without LRC (Longitudinal Redundancy Check) code formats
  - Validate track data format and checksums

- **User Interface**
  - Modern Tkinter-based GUI
  - Real-time parsing and validation
  - Tabbed interface for easy navigation
  - Copy results to clipboard

- **Developer Friendly**
  - Comprehensive API documentation
  - Type hints for better IDE support
  - Unit tested with pytest
  - MIT Licensed

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Using pip

```bash
pip install credit-card-stripe-parser
```

### From Source

1. Clone the repository:
   ```bash
   git clone https://github.com/Nsfr750/credit-card-stripe-parser.git
   cd credit-card-stripe-parser
   ```

2. Install the package in development mode:
   ```bash
   pip install -e .
   ```

### Dependencies
All dependencies are automatically installed during package installation. The main dependencies are:
- Python Standard Library (no external dependencies required for core functionality)
- Tkinter (included with Python on most systems)

## Usage

### Command Line Interface

Run the GUI application:

```bash
python -m credit_card_stripe_parser.gui
```

Or if installed via pip:

```bash
credit-card-stripe-parser
```

### Python API

```python
from credit_card_stripe_parser import FullTrackParser, FullTrackDataModel

# Create a parser instance
parser = FullTrackParser()

# Example track data (without LRC)
track1 = "%B5168755544412233^PKMMV/UNEMBOXXXX          ^1807111100000000000000111000000?"
track2 = ";5168755544412233=18071111000011100000?"

# Parse track data
result = parser.parse(track1 + track2)  # Parse combined tracks

# Or parse tracks individually
track1_data = parser.parse_track1(track1)
track2_data = parser.parse_track2(track2)

# Access parsed data
print(f"Cardholder: {track1_data.card_holder_name}")
print(f"PAN: {track1_data.pan}")
print(f"Expiry: {track1_data.expiration_date}")
print(f"Service Code: {track2_data.service_code}")

# Parse full track with separate track data
full_data = parser.parse_full_track(track1, track2)
```

### GUI Application

The graphical interface provides an easy way to parse and view track data:

1. Enter Track 1 and/or Track 2 data in the input fields
2. Click "Parse Tracks" to process the data
3. View the parsed results in the respective tabs
4. Use the "Clear All" button to reset the form

![Screenshot](screenshot.png)  <!-- Add a screenshot if available -->

## API Reference

### `FullTrackParser`

The main parser class that provides methods to parse and validate track data.

#### Methods

- `parse(full_track: str) -> FullTrackDataModel`  
  Parse both Track 1 and Track 2 data from a single string.

- `parse_full_track(track1: str, track2: str = None) -> FullTrackDataModel`  
  Parse Track 1 and Track 2 data from separate strings.

- `parse_track1(full_track: str) -> TrackOneModel`  
  Parse only Track 1 data.
  
- `parse_track_one(full_track: str) -> TrackOneModel`  
  Alias for `parse_track1`.
  
- `parse_track2(full_track: str) -> TrackTwoModel`  
  Parse only Track 2 data.
  
- `parse_track_two(full_track: str) -> TrackTwoModel`  
  Alias for `parse_track2`.
  
- `try_parse_track_one(full_track: str) -> Tuple[bool, Optional[TrackOneModel]]`  
  Try to parse Track 1 data, returning a success flag and result.
  
- `try_parse_track_two(full_track: str) -> Tuple[bool, Optional[TrackTwoModel]]`  
  Try to parse Track 2 data, returning a success flag and result.

### Models

- `FullTrackDataModel`  
  Container for parsed track data with validation flags.
  - `is_track_one_valid: bool` - Whether Track 1 data is valid
  - `track_one: Optional[TrackOneModel]` - Parsed Track 1 data
  - `is_track_two_valid: bool` - Whether Track 2 data is valid
  - `track_two: Optional[TrackTwoModel]` - Parsed Track 2 data

- `TrackOneModel`  
  Parsed Track 1 data.
  - `format_code: str` - Format code (first character after start sentinel)
  - `pan: str` - Primary Account Number
  - `card_holder_name: str` - Cardholder name
  - `expiration_date: str` - Expiration date (YYMM format)
  - `service_code: str` - Service code
  - `discretionary_data: str` - Additional discretionary data

- `TrackTwoModel`  
  Parsed Track 2 data.
  - `pan: str` - Primary Account Number
  - `expiration_date: str` - Expiration date (YYMM format)
  - `service_code: str` - Service code
  - `discretionary_data: str` - Additional discretionary data

### Exceptions

- `CreditCardStripeError`  
  Base exception for all parser errors.
  
- `InvalidTrackOneError`  
  Raised when there's an error parsing Track 1 data.
  
- `InvalidTrackTwoError`  
  Raised when there's an error parsing Track 2 data.

## Development

### Setting Up Development Environment

1. Clone the repository:
   ```bash
   git clone https://github.com/Nsfr750/credit-card-stripe-parser.git
   cd credit-card-stripe-parser
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install development dependencies:
   ```bash
   pip install -e .[dev]
   ```

### Running Tests

```bash
pytest
```

### Building Documentation

Documentation is written in Markdown (this README.md) and includes:
- Installation instructions
- Usage examples
- API reference
- Development guidelines

### Code Style

This project follows PEP 8 style guidelines. Code is automatically formatted using `black` and `isort`.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- ISO/IEC 7811 - Identification cards — Recording technique
- ISO/IEC 7813 - Identification cards — Financial transaction cards
- [Stripe documentation](https://stripe.com/docs/issuing/cards/security-code) for reference

---

*This tool is for educational and testing purposes only. Always handle payment card data in compliance with PCI DSS requirements.*

# Credit Card Stripe Parser

[![License: GPLv3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

A Python library for parsing and validating credit card magnetic stripe data.

## Table of Contents
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Features](#features)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## Installation

```bash
pip install credit-card-stripe-parser
```

## Quick Start

```python
from credit_card_stripe_parser import parse_track_data

# Example usage
track_data = "%B4111111111111111^CARDHOLDER/NAME^25121010000000000000?;4111111111111111=25121010000000000000?"
parsed_data = parse_track_data(track_data)
print(parsed_data)
```

## Features
- Parse Track 1 and Track 2 magnetic stripe data
- Validate card numbers using Luhn algorithm
- Extract cardholder information
- Support for various card types
- Comprehensive error handling

## Documentation
- [API Reference](api.md)
- [Usage Examples](examples.md)
- [Development Guide](development.md)

## Contributing
Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details on how to get started.

## License
This project is licensed under the GPLv3 License - see the [LICENSE](../LICENSE) file for details.

# Development Guide

## Getting Started

### Prerequisites
- Python 3.7+
- pip (Python package manager)
- Git

### Setting Up the Development Environment

1. Clone the repository:
   ```bash
   git clone https://github.com/Nsfr750/credit_card_stripe_parser.git
   cd credit_card_stripe_parser
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/Mac
   ```

3. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

## Project Structure

```
credit_card_stripe_parser/
├── credit_card_stripe_parser/  # Main package
│   ├── __init__.py
│   ├── about.py
│   ├── exceptions.py
│   └── models/               # Data models
│       ├── __init__.py
│       ├── full_track_data_model.py
│       └── track_one_model.py
├── tests/                    # Test files
├── docs/                     # Documentation
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── setup.py
```

## Running Tests

Run the full test suite:
```bash
pytest
```

Run tests with coverage report:
```bash
pytest --cov=credit_card_stripe_parser tests/
```

## Code Style

This project follows the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide. Code is automatically formatted using [Black](https://github.com/psf/black).

To format your code:
```bash
black .
```

## Versioning

This project follows [Semantic Versioning 2.0.0](https://semver.org/). The version number is maintained in `script/version.py`.

To update the version:
1. Update the version in `script/version.py`
2. Update the `CHANGELOG.md` with the changes

## Documentation

Documentation is written in Markdown and located in the `docs/` directory. The main documentation files are:

- `README.md`: Project overview and basic usage
- `api.md`: API reference
- `examples.md`: Code examples
- `development.md`: This development guide

## Branching Strategy

- `main`: Stable, production-ready code
- `develop`: Integration branch for features
- `feature/*`: New features and enhancements
- `bugfix/*`: Bug fixes
- `hotfix/*`: Critical production fixes

## Pull Request Process

1. Fork the repository
2. Create a feature/bugfix branch
3. Commit your changes
4. Push to the branch
5. Submit a pull request to the `develop` branch

## Release Process

1. Update the version in `script/version.py`
2. Update `CHANGELOG.md` with the new version and changes
3. Create a release tag:
   ```bash
   git tag -a vX.Y.Z -m "Version X.Y.Z"
   git push origin vX.Y.Z
   ```
4. Create a new release on GitHub with the release notes

## License

This project is licensed under the GPLv3 License - see the [LICENSE](../LICENSE) file for details.

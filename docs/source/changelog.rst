.. _changelog:

Changelog
=========

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_,
and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

.. contents:: Table of Contents
   :depth: 2
   :local:
   :backlinks: top

Unreleased
----------

### Added
- Support for parsing additional card formats
- More comprehensive test coverage
- Additional documentation examples

### Changed
- Improved error messages for better debugging
- Updated dependencies to their latest versions

### Fixed
- Minor bug fixes and performance improvements

[1.2.0] - 2025-05-29
-------------------

### Added
- Comprehensive API documentation
- Detailed user guide
- Example code snippets
- FAQ section
- Contribution guidelines
- License documentation
- Changelog

### Changed
- Restructured documentation for better organization
- Improved code examples
- Enhanced error handling
- Updated dependencies

### Fixed
- Fixed documentation typos and inaccuracies
- Resolved minor bugs in the documentation
- Fixed broken links

[1.1.0] - 2025-05-29
-------------------

### Added
- Graphical User Interface (GUI) using Tkinter
- Tabbed interface for viewing parsed data
- About dialog with application information
- Support for parsing tracks individually or together
- Improved error handling and validation
- Enhanced error messages
- Added more test cases

### Changed
- Updated README with GUI documentation
- Improved API documentation
- Better code organization
- More robust parsing logic

### Fixed
- Fixed attribute access in FullTrackDataModel (track_one/track_two vs track1/track2)
- Added missing parse_track1 and parse_track2 methods as aliases
- Fixed issues with LRC validation
- Resolved edge cases in track parsing

[1.0.0] - 2025-05-29
-------------------

### Added
- Initial release of Credit Card Stripe Parser
- Support for parsing Track 1 and Track 2 data
- Basic validation of track data
- Command-line interface
- Unit tests
- Basic documentation
- MIT License
- README with installation and usage instructions

### Changed
- N/A

### Deprecated
- N/A

### Removed
- N/A

### Fixed
- N/A

### Security
- N/A

Versioning Policy
----------------

This project follows `Semantic Versioning 2.0.0 <https://semver.org/>`_:

- **MAJOR** version for incompatible API changes
- **MINOR** version for added functionality in a backward-compatible manner
- **PATCH** version for backward-compatible bug fixes

Deprecation Policy
-----------------

- Deprecated features will be marked as such in the documentation
- Deprecated features will be removed in the next MAJOR version
- At least one MINOR version will be released with deprecation warnings before removal

Upgrade Guide
------------

### From 1.1.0 to 1.2.0
- No breaking changes
- New documentation structure
- Additional examples and guides

### From 1.0.0 to 1.1.0
- Added GUI components
- Some internal API changes, but backward compatible
- Improved error handling

### Initial Release (1.0.0)
- First stable release
- Basic parsing functionality
- Command-line interface

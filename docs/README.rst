Credit Card Stripe Parser Documentation
======================================

This directory contains the source files for the Credit Card Stripe Parser documentation.

Building the Documentation
-------------------------

1. Install the required dependencies:

   .. code-block:: bash

      pip install -r requirements.txt

2. Build the HTML documentation:

   .. code-block:: bash

      make html

   The built documentation will be available in the ``build/html`` directory.

3. For live preview with auto-reload:

   .. code-block:: bash

      sphinx-autobuild source build/html

Documentation Structure
----------------------

- ``source/``: Source files for the documentation
  - ``index.rst``: Main documentation page
  - ``installation.rst``: Installation instructions
  - ``usage.rst``: Usage guide with examples
  - ``api.rst``: API reference
  - ``contributing.rst``: Contribution guidelines
  - ``changelog.rst``: Version history
  - ``_static/``: Static files (CSS, images, etc.)
  - ``_templates/``: Custom templates

Documentation Updates
--------------------

When making changes to the code, please ensure that you update the relevant documentation.

- Update docstrings in the code using the Google style
- Add or update examples in the usage guide
- Update the API reference if there are any changes to the public API
- Add a new entry to the changelog for significant changes

Viewing the Documentation
------------------------

After building the documentation, open ``build/html/index.html`` in your web browser to view the documentation locally.

For the latest version of the documentation, visit: https://tuxxle.ddns.net/credit-card-stripe-parser/docs/

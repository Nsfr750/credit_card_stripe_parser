.. _contributing:

Contributing to Credit Card Stripe Parser
========================================

We welcome contributions from the community! This guide will help you get started with contributing to the project.

.. contents:: Table of Contents
   :depth: 2
   :local:
   :backlinks: top

Ways to Contribute
------------------

There are many ways to contribute to the project:

- **Report Bugs**: File an issue on GitHub if you find a bug
- **Fix Bugs**: Look through the GitHub issues for bugs to fix
- **Request Features**: Suggest new features or improvements
- **Write Documentation**: Help improve the documentation
- **Submit Feedback**: Let us know what you think
- **Become a Maintainer**: Help review and merge pull requests

Code of Conduct
---------------

By participating in this project, you agree to abide by our `Code of Conduct <CODE_OF_CONDUCT.md>`_.

Getting Started
--------------

### Prerequisites

- Python 3.8+
- Git
- pip

### Setting Up Your Development Environment

1. **Fork the Repository**
   - Click the "Fork" button at the top-right of the `GitHub repository <https://github.com/Nsfr750/credit-card-stripe-parser>`_

2. **Clone Your Fork**
   .. code-block:: bash

      # Clone your fork
      git clone https://github.com/YOUR_USERNAME/credit-card-stripe-parser.git
      
      # Navigate to the project directory
      cd credit-card-stripe-parser
      
      # Add the original repository as "upstream"
      git remote add upstream https://github.com/Nsfr750/credit-card-stripe-parser.git

3. **Set Up a Virtual Environment (Recommended)**
   .. code-block:: bash

      # Create a virtual environment
      python -m venv venv
      
      # Activate the virtual environment
      # On Windows:
      .\venv\Scripts\activate
      # On Unix or MacOS:
      # source venv/bin/activate

4. **Install Dependencies**
   .. code-block:: bash

      # Install the package in development mode with all dependencies
      pip install -e ".[dev]"
      
      # Install pre-commit hooks
      pre-commit install

5. **Create a Feature Branch**
   .. code-block:: bash

      # Create and switch to a new branch
      git checkout -b feature/your-feature-name

Making Changes
-------------

### Code Style

We use several tools to maintain code quality and style:

- **Black** for code formatting
- **isort** for import sorting
- **Flake8** for linting
- **Mypy** for static type checking

These will run automatically when you commit changes if you have pre-commit installed.

### Running Tests

Run the test suite to make sure your changes don't break anything:

.. code-block:: bash

   # Run all tests
   pytest
   
   # Run a specific test file
   pytest tests/test_parser.py
   
   # Run tests with coverage report
   pytest --cov=credit_card_stripe_parser

### Building Documentation

To build the documentation locally:

.. code-block:: bash

   # Install documentation dependencies
   pip install -e ".[docs]"
   
   # Build the documentation
   cd docs
   make html
   
   # Open the documentation in your browser
   # On Windows:
   start _build/html/index.html
   # On macOS:
   # open _build/html/index.html
   # On Linux:
   # xdg-open _build/html/index.html

### Commit Message Format

We follow the `Conventional Commits <https://www.conventionalcommits.org/>`_ specification:

.. code-block:: none

   <type>[optional scope]: <description>
   
   [optional body]
   
   [optional footer(s)]

Types:
- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Changes that do not affect the meaning of the code
- **refactor**: A code change that neither fixes a bug nor adds a feature
- **perf**: A code change that improves performance
- **test**: Adding missing or correcting existing tests
- **chore**: Changes to the build process or auxiliary tools

Example:

.. code-block:: none

   feat(parser): add support for new track format
   
   Added support for parsing track data in the new format used by some card issuers.
   
   Closes #123

Submitting a Pull Request
------------------------

1. **Keep your fork in sync**
   .. code-block:: bash

      git fetch upstream
      git checkout main
      git merge upstream/main

2. **Push your changes**
   .. code-block:: bash

      git push origin your-branch-name

3. **Open a Pull Request**
   - Go to https://github.com/Nsfr750/credit-card-stripe-parser
   - Click "New Pull Request"
   - Select your branch
   - Fill in the PR template
   - Submit the PR

4. **Respond to feedback**
   - Make any requested changes
   - Push updates to your branch
   - The PR will be automatically updated

Code Review Process
------------------

1. A maintainer will review your PR
2. They may request changes
3. Once approved, a maintainer will merge your PR

Reporting Issues
---------------

When reporting issues, please include:

1. A clear, descriptive title
2. Steps to reproduce the issue
3. Expected vs actual behavior
4. Version information
5. Any relevant error messages

Feature Requests
---------------

For feature requests:

1. Explain the problem you're trying to solve
2. Describe the solution you'd like
3. Provide examples of similar features in other projects

Becoming a Maintainer
--------------------

Interested in becoming a maintainer? Here's what we look for:

1. Consistent, high-quality contributions
2. Good understanding of the codebase
3. Helpful engagement with the community

Contact the current maintainers to express your interest.

License
-------
By contributing, you agree that your contributions will be licensed under the MIT License.

Coding Standards
---------------

- Follow `PEP 8 <https://www.python.org/dev/peps/pep-0008/>`_ style guide
- Use type hints for all functions and methods
- Write docstrings following the Google style:
  https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings
- Keep lines under 100 characters

Testing
-------

- Write tests for all new functionality
- Run tests before submitting a pull request:

  .. code-block:: bash

     pytest

- Ensure test coverage remains high (95%+)
- Include both positive and negative test cases

Documentation
------------

- Update documentation for any new features or changes
- Ensure docstrings are clear and comprehensive
- Update examples if the API changes

Submitting a Pull Request
-----------------------

1. Ensure all tests pass
2. Update documentation as needed
3. Submit the pull request with a clear description of changes
4. Reference any related issues

Code Review Process
------------------
1. Pull requests are reviewed by maintainers
2. Address any feedback from code reviews
3. Once approved, a maintainer will merge your changes

Reporting Issues
---------------

When reporting issues, please include:

- Description of the problem
- Steps to reproduce
- Expected behavior
- Actual behavior
- Version information (Python version, package version, etc.)

License
-------

By contributing, you agree that your contributions will be licensed under the project's license.

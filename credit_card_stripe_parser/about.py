"""
About information for the Credit Card Stripe Parser application.

This module contains metadata and information about the application,
including version, author, license, and credits.
"""

# Application metadata
APP_NAME = "Credit Card Stripe Parser"
VERSION = "1.2.0"
AUTHOR = "Nsfr750"
YEAR = "2025"
COPYRIGHT = f"Copyright © {YEAR} {AUTHOR}"

# Application URLs
GITHUB_URL = "https://github.com/Nsfr750/credit_card_stripe_parser"
ISSUES_URL = f"{GITHUB_URL}/issues"
DOCS_URL = f"{GITHUB_URL}/blob/main/README.md"

# Application description
DESCRIPTION = """A tool for parsing and analyzing credit card magnetic stripe data.

This application allows you to parse Track 1 and Track 2 data from magnetic 
stripe cards according to ISO 7811-2 standards. It provides both a command-line
interface and a user-friendly GUI for viewing and analyzing the parsed data.

Features:
• Parse Track 1 and Track 2 data
• Validate track data format and checksums
• User-friendly GUI with real-time parsing
• Detailed error reporting
"""

# License information
LICENSE = f"""MIT License

{COPYRIGHT}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

# Credits and acknowledgments
CREDITS = [
    f"Version: {VERSION}",
    "",
    "Developed by Nsfr750",
    "",
    "Built with:",
    "• Python 3.8+",
    "• Tkinter (GUI)",
    "",
    "Third-party resources:",
    "• Icons by Icons8 (https://icons8.com)",
    "• ISO/IEC 7811-2 Standard",
    "",
    f"GitHub: {GITHUB_URL}",
    f"Report issues: {ISSUES_URL}",
]

# Legal disclaimer
DISCLAIMER = """DISCLAIMER:
This software is provided for educational and testing purposes only. 
Always handle payment card data in compliance with PCI DSS requirements 
and applicable laws and regulations. The developers are not responsible 
for any misuse of this software."""

def get_about_info() -> str:
    """
    Return a formatted string with application information.
    
    Returns:
        str: Formatted string containing application information, credits, and license.
    """
    info = [
        f"{APP_NAME} v{VERSION}",
        "",
        f"{DESCRIPTION}",
        "",
        f"Author: {AUTHOR}",
        f"GitHub: {GITHUB_URL}",
        "",
        "Credits:",
        "-" * 40,
    ]
    
    # Add credits
    info.extend(CREDITS)
    
    # Add license and disclaimer
    info.extend([
        "",
        "-" * 40,
        "",
        DISCLAIMER,
        "",
        "-" * 40,
        "",
        LICENSE
    ])
    
    return "\n".join(info)

def get_short_info() -> str:
    """
    Return a short summary of the application information.
    
    Returns:
        str: Short summary including app name, version, and copyright.
    """
    return f"{APP_NAME} v{VERSION}\n{COPYRIGHT}\n{GITHUB_URL}"

"""
Custom exceptions for the credit card stripe parser.
"""


class CreditCardStripeError(Exception):
    """Base exception for all credit card stripe parser errors."""
    pass


class InvalidTrackOneError(CreditCardStripeError):
    """Raised when there's an error parsing Track 1 data."""
    pass


class InvalidTrackTwoError(CreditCardStripeError):
    """Raised when there's an error parsing Track 2 data."""
    pass

"""
TrackOneModel class for storing parsed Track 1 data from a credit card magnetic stripe.
"""
from dataclasses import dataclass


@dataclass
class TrackOneModel:
    """
    A data class that holds the parsed data from Track 1 of a credit card.
    
    ISO 7811-2 track one character encoding definition:
    SS FC PAN FS Name FS Date Discretionary Data ES LRC
    
    Attributes:
        format_code (str): The format code (FC) from the track data.
        pan (str): The Primary Account Number (PAN).
        card_holder_name (str): The cardholder's name.
        expiration_date (str): The card's expiration date in YYMM format.
        service_code (str): The service code from the track data.
        discretionary_data (str): Any additional discretionary data.
        source_string (str): The original track data string that was parsed.
    """
    format_code: str
    pan: str
    card_holder_name: str
    expiration_date: str
    service_code: str
    discretionary_data: str
    source_string: str

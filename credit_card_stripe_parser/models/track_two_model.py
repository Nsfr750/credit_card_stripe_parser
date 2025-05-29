"""
TrackTwoModel class for storing parsed Track 2 data from a credit card magnetic stripe.
"""
from dataclasses import dataclass


@dataclass
class TrackTwoModel:
    """
    A data class that holds the parsed data from Track 2 of a credit card.
    
    ISO 7811-2 Track Two encoding definition:
    SS PAN FS Date SVC CD Discretionary Data ES LRC
    
    Attributes:
        pan (str): The Primary Account Number (PAN).
        expiration_date (str): The card's expiration date in YYMM format.
        service_code (str): The service code from the track data.
        discretionary_data (str): Any additional discretionary data.
        source_string (str): The original track data string that was parsed.
    """
    pan: str
    expiration_date: str
    service_code: str
    discretionary_data: str
    source_string: str

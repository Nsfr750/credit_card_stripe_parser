"""
FullTrackDataModel class for storing parsed track data from both Track 1 and Track 2.
"""
from dataclasses import dataclass
from typing import Optional

from .track_one_model import TrackOneModel
from .track_two_model import TrackTwoModel


@dataclass
class FullTrackDataModel:
    """
    A data class that holds the parsed data from both Track 1 and Track 2 of a credit card.
    
    Attributes:
        is_track_one_valid (bool): Indicates if Track 1 data is valid.
        track_one (Optional[TrackOneModel]): The parsed Track 1 data, or None if invalid.
        is_track_two_valid (bool): Indicates if Track 2 data is valid.
        track_two (Optional[TrackTwoModel]): The parsed Track 2 data, or None if invalid.
    """
    is_track_one_valid: bool
    track_one: Optional[TrackOneModel]
    is_track_two_valid: bool
    track_two: Optional[TrackTwoModel]

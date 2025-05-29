"""
FullTrackParser class for parsing credit card magnetic stripe data.

This module provides functionality to parse Track 1 and Track 2 data from
magnetic stripe cards according to ISO 7811-2 standards.
"""
from typing import Optional, Tuple

from .models import FullTrackDataModel, TrackOneModel, TrackTwoModel
from .exceptions import InvalidTrackOneError, InvalidTrackTwoError


class FullTrackParser:
    """
    A parser for credit card magnetic stripe data that can parse both Track 1 and Track 2.
    """
    
    # Constants for track parsing
    _SS1 = '%'  # Start sentinel for Track 1
    _FS1 = '^'  # Field separator for Track 1
    _ES1 = '?'  # End sentinel for Track 1
    _SS2 = ';'  # Start sentinel for Track 2
    _FS2 = '='  # Field separator for Track 2
    _ES2 = '?'  # End sentinel for Track 2

    def parse_full_track(self, track1: str, track2: str = None) -> FullTrackDataModel:
        """
        Parse both Track 1 and Track 2 data from separate track strings.
        
        Args:
            track1: The Track 1 data string to parse.
            track2: The Track 2 data string to parse (optional).
            
        Returns:
            FullTrackDataModel: An object containing the parsed track data.
            
        Raises:
            InvalidTrackOneError: If there's an error parsing Track 1 data.
            InvalidTrackTwoError: If there's an error parsing Track 2 data.
        """
        track1_model = None
        track2_model = None
        is_track1_valid = False
        is_track2_valid = False
        
        try:
            if track1:
                is_track1_valid = self._validate_track_one(track1)
                if is_track1_valid:
                    track1_model = self.parse_track_one(track1)
        except Exception as e:
            raise InvalidTrackOneError("Failed to parse Track 1 data") from e
            
        try:
            if track2:
                is_track2_valid = self._validate_track_two(track2)
                if is_track2_valid:
                    track2_model = self.parse_track_two(track2)
        except Exception as e:
            raise InvalidTrackTwoError("Failed to parse Track 2 data") from e
            
        return FullTrackDataModel(
            is_track_one_valid=is_track1_valid,
            track_one=track1_model,
            is_track_two_valid=is_track2_valid,
            track_two=track2_model
        )
    
    def parse(self, full_track: str) -> FullTrackDataModel:
        """
        Parse both Track 1 and Track 2 data from a full track string.
        
        Args:
            full_track: The full track data string to parse.
            
        Returns:
            FullTrackDataModel: An object containing the parsed track data.
            
        Raises:
            InvalidTrackOneError: If there's an error parsing Track 1 data.
            InvalidTrackTwoError: If there's an error parsing Track 2 data.
        """
        track1 = None
        track2 = None
        is_track1_valid = False
        is_track2_valid = False
        
        try:
            is_track1_valid = self._validate_track_one(full_track)
            if is_track1_valid:
                track1 = self.parse_track_one(full_track)
        except Exception as e:
            raise InvalidTrackOneError("Failed to parse Track 1 data") from e
            
        try:
            is_track2_valid = self._validate_track_two(full_track)
            if is_track2_valid:
                track2 = self.parse_track_two(full_track)
        except Exception as e:
            raise InvalidTrackTwoError("Failed to parse Track 2 data") from e
            
        return FullTrackDataModel(
            is_track_one_valid=is_track1_valid,
            track_one=track1,
            is_track_two_valid=is_track2_valid,
            track_two=track2
        )
    
    def parse_track1(self, full_track: str) -> TrackOneModel:
        """
        Alias for parse_track_one. Parses Track 1 data from a full track string.
        
        Args:
            full_track: The full track data string to parse.
            
        Returns:
            TrackOneModel: The parsed Track 1 data.
            
        Raises:
            ValueError: If the track data is invalid or malformed.
        """
        return self.parse_track_one(full_track)
        
    def parse_track_one(self, full_track: str) -> TrackOneModel:
        """
        Parse Track 1 data from a full track string.
        
        Args:
            full_track: The full track data string to parse.
            
        Returns:
            TrackOneModel: The parsed Track 1 data.
            
        Raises:
            ValueError: If the track data is invalid or malformed.
        """
        if self._SS1 not in full_track or self._ES1 not in full_track:
            raise ValueError("Invalid Track 1 data: missing start or end sentinel")
            
        # Extract the track string (between SS1 and ES1)
        start_idx = full_track.index(self._SS1) + 1
        end_idx = full_track.index(self._ES1)
        track_string = full_track[start_idx:end_idx]
        
        if len(track_string) > 79:
            raise ValueError("Track 1 data exceeds maximum length of 79 characters")
            
        # Split into segments using the field separator
        track_segments = track_string.split(self._FS1)
        if len(track_segments) < 3:
            raise ValueError("Invalid Track 1 data: missing required fields")
            
        # The first character after SS1 is the format code
        format_code = track_string[0] if track_string else ''
        
        return TrackOneModel(
            format_code=format_code,
            pan=track_segments[0][1:],  # Skip the format code
            card_holder_name=track_segments[1],
            expiration_date=track_segments[2][:4],
            service_code=track_segments[2][4:7],
            discretionary_data=track_segments[2][7:],  # Everything after service code
            source_string=full_track[:end_idx + 1]  # Include the end sentinel
        )
    
    def try_parse_track_one(self, full_track: str) -> Tuple[bool, Optional[TrackOneModel]]:
        """
        Try to parse Track 1 data, returning a success flag and the result.
        
        Args:
            full_track: The full track data string to parse.
            
        Returns:
            A tuple of (success, result) where success is a boolean indicating
            if parsing was successful, and result is the parsed TrackOneModel or None.
        """
        try:
            if self._SS1 not in full_track:
                return False, None
            track_one = self.parse_track_one(full_track)
            return True, track_one
        except Exception:
            return False, None
    
    def parse_track2(self, full_track: str) -> TrackTwoModel:
        """
        Alias for parse_track_two. Parses Track 2 data from a full track string.
        
        Args:
            full_track: The full track data string to parse.
            
        Returns:
            TrackTwoModel: The parsed Track 2 data.
            
        Raises:
            ValueError: If the track data is invalid or malformed.
        """
        return self.parse_track_two(full_track)
        
    def parse_track_two(self, full_track: str) -> TrackTwoModel:
        """
        Parse Track 2 data from a full track string.
        
        Args:
            full_track: The full track data string to parse.
            
        Returns:
            TrackTwoModel: The parsed Track 2 data.
            
        Raises:
            ValueError: If the track data is invalid or malformed.
        """
        if self._SS2 not in full_track or self._ES2 not in full_track:
            raise ValueError("Invalid Track 2 data: missing start or end sentinel")
            
        # Extract the track string (between SS2 and ES2)
        start_idx = full_track.index(self._SS2) + 1
        end_idx = full_track.rindex(self._ES2)  # Use rindex in case of multiple '?'
        track_string = full_track[start_idx:end_idx]
        
        if len(track_string) > 40:
            raise ValueError("Track 2 data exceeds maximum length of 40 characters")
            
        # Split into segments using the field separator
        track_segments = track_string.split(self._FS2)
        if len(track_segments) < 2:
            raise ValueError("Invalid Track 2 data: missing required fields")
            
        # The first segment is PAN, second segment contains expiration date, service code, and discretionary data
        pan = track_segments[0]
        data_segment = track_segments[1]
        
        # Ensure data segment is long enough
        if len(data_segment) < 7:
            raise ValueError("Invalid Track 2 data: data segment too short")
            
        return TrackTwoModel(
            pan=pan,
            expiration_date=data_segment[:4],
            service_code=data_segment[4:7],
            discretionary_data=data_segment[7:],
            source_string=full_track[full_track.index(self._SS2):end_idx + 1]  # Include the end sentinel
        )
    
    def try_parse_track_two(self, full_track: str) -> Tuple[bool, Optional[TrackTwoModel]]:
        """
        Try to parse Track 2 data, returning a success flag and the result.
        
        Args:
            full_track: The full track data string to parse.
            
        Returns:
            A tuple of (success, result) where success is a boolean indicating
            if parsing was successful, and result is the parsed TrackTwoModel or None.
        """
        try:
            if self._SS2 not in full_track:
                return False, None
            track_two = self.parse_track_two(full_track)
            return True, track_two
        except Exception:
            return False, None
    
    def _calculate_lrc(self, data: bytes) -> int:
        """
        Calculate the Longitudinal Redundancy Check (LRC) for the given data.
        
        Args:
            data: The data to calculate the LRC for.
            
        Returns:
            The calculated LRC byte.
        """
        lrc = 0
        for byte in data:
            lrc ^= byte
        return lrc
    
    def _has_lrc_code(self, full_track: str) -> bool:
        """
        Check if the track data includes an LRC code.
        
        Args:
            full_track: The full track data string to check.
            
        Returns:
            bool: True if an LRC code is present, False otherwise.
        """
        if f"{self._ES1}{self._SS2}" in full_track or full_track.endswith(self._ES1):
            return False
        if full_track.endswith(self._ES2):
            return False
        return True
    
    def _validate_track_one(self, full_track: str) -> bool:
        """
        Validate Track 1 data.
        
        Args:
            full_track: The full track data string to validate.
            
        Returns:
            bool: True if the Track 1 data is valid, False otherwise.
        """
        if self._SS1 not in full_track:
            return False
            
        es1_index = full_track.find(self._ES1)
        if es1_index == -1:
            return False
            
        # If there's no LRC code, we're done
        if es1_index == len(full_track) - 1:
            return True
            
        # Check for LRC
        potential_lrc = full_track[es1_index + 1]
        if potential_lrc != self._SS2:  # If not the start of Track 2
            # Calculate expected LRC
            track_data = full_track[full_track.index(self._SS1) + 1:es1_index]
            calculated_lrc = self._calculate_lrc(track_data.encode('ascii'))
            if ord(potential_lrc) != calculated_lrc:
                return False
                
        return True
    
    def _validate_track_two(self, full_track: str) -> bool:
        """
        Validate Track 2 data.
        
        Args:
            full_track: The full track data string to validate.
            
        Returns:
            bool: True if the Track 2 data is valid, False otherwise.
        """
        if self._SS2 not in full_track:
            return False
            
        es2_index = full_track.rfind(self._ES2)
        if es2_index == -1:
            return False
            
        # If there's no LRC code, we're done
        if es2_index == len(full_track) - 1:
            return True
            
        # Check for LRC
        potential_lrc = full_track[es2_index + 1:es2_index + 2]
        if potential_lrc and potential_lrc != '\0':  # If not null terminator
            # Calculate expected LRC
            track_data = full_track[full_track.index(self._SS2) + 1:es2_index]
            calculated_lrc = self._calculate_lrc(track_data.encode('ascii'))
            if ord(potential_lrc) != calculated_lrc:
                return False
                
        return True

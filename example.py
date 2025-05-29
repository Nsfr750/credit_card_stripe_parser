#!/usr/bin/env python3
"""
Example usage of the credit card stripe parser.
"""

from credit_card_stripe_parser import FullTrackParser

def main():
    # Create a parser instance
    parser = FullTrackParser()
    
    # Example track data (without LRC)
    track_data = (
        "%B5168755544412233^PKMMV/UNEMBOXXXX          ^1807111100000000000000111000000?"
        ";5168755544412233=18071111000011100000?"
    )
    
    print(f"Parsing track data: {track_data}\n")
    
    try:
        # Parse the track data
        result = parser.parse(track_data)
        
        # Display results
        if result.is_track_one_valid and result.track_one:
            track1 = result.track_one
            print("=== Track 1 Data ===")
            print(f"Format Code: {track1.format_code}")
            print(f"PAN: {track1.pan}")
            print(f"Cardholder: {track1.card_holder_name.strip()}")
            print(f"Expiration: {track1.expiration_date[:2]}/{track1.expiration_date[2:]} (YY/MM)")
            print(f"Service Code: {track1.service_code}")
            print(f"Discretionary Data: {track1.discretionary_data}")
            print(f"Source: {track1.source_string}")
        else:
            print("No valid Track 1 data found.")
        
        print("\n---\n")
        
        if result.is_track_two_valid and result.track_two:
            track2 = result.track_two
            print("=== Track 2 Data ===")
            print(f"PAN: {track2.pan}")
            print(f"Expiration: {track2.expiration_date[:2]}/{track2.expiration_date[2:]} (YY/MM)")
            print(f"Service Code: {track2.service_code}")
            print(f"Discretionary Data: {track2.discretionary_data}")
            print(f"Source: {track2.source_string}")
        else:
            print("No valid Track 2 data found.")
    except Exception as e:
        print(f"Error parsing track data: {e}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Example usage of the credit card stripe parser.
"""

from pprint import pprint, pformat
from credit_card_stripe_parser import FullTrackParser

def print_section(title, char='-', length=50):
    """Print a formatted section header."""
    print(f"\n{title}")
    print(char * max(len(title), length))

def main():
    # Create a parser instance
    parser = FullTrackParser()
    
    # Example track data (without LRC)
    track_data = (
        "%B5168755544412233^PKMMV/UNEMBOXXXX          ^1807111100000000000000111000000?"
        ";5168755544412233=18071111000011100000?"
    )
    
    print_section("Credit Card Stripe Parser Example", '=')
    print(f"\nParsing track data:\n{track_data}")
    
    try:
        # Parse the track data
        result = parser.parse(track_data)
        
        print_section("Parsing Results")
        print("✓ Parsing completed successfully!")
        
        # Display Track 1 data if available
        if hasattr(result, 'track_one') and result.track_one:
            track1 = result.track_one
            print_section("Track 1 Data")
            print(f"  • PAN: {getattr(track1, 'pan', 'N/A')}")
            print(f"  • Cardholder: {getattr(track1, 'card_holder_name', 'N/A').strip()}")
            print(f"  • Expiration: {getattr(track1, 'expiration_date', 'N/A')} (YYMM)")
            print(f"  • Service Code: {getattr(track1, 'service_code', 'N/A')}")
            print(f"  • Format Code: {getattr(track1, 'format_code', 'N/A')}")
            print(f"  • Discretionary Data: {getattr(track1, 'discretionary_data', 'N/A')}")
            print(f"  • Raw Data: {getattr(track1, 'source_string', 'N/A')}")
        else:
            print("\nℹ️ No Track 1 data found or parsed successfully.")
        
        # Display Track 2 data if available
        if hasattr(result, 'track_two') and result.track_two:
            track2 = result.track_two
            print_section("Track 2 Data")
            print(f"  • PAN: {getattr(track2, 'pan', 'N/A')}")
            print(f"  • Expiration: {getattr(track2, 'expiration_date', 'N/A')} (YYMM)")
            print(f"  • Service Code: {getattr(track2, 'service_code', 'N/A')}")
            print(f"  • Discretionary Data: {getattr(track2, 'discretionary_data', 'N/A')}")
            print(f"  • Raw Data: {getattr(track2, 'source_string', 'N/A')}")
        else:
            print("\nℹ️ No Track 2 data found or parsed successfully.")
            
        # Display validation status
        print_section("Validation Status")
        print(f"  • Track 1 Valid: {'✓' if getattr(result, 'is_track_one_valid', False) else '✗'}")
        print(f"  • Track 2 Valid: {'✓' if getattr(result, 'is_track_two_valid', False) else '✗'}")
        
        # Display validation results
        if hasattr(result, 'validation_warnings') and result.validation_warnings:
            print_section("Validation Warnings")
            for i, warning in enumerate(result.validation_warnings, 1):
                print(f"  {i}. {warning}")
        
        if hasattr(result, 'validation_errors') and result.validation_errors:
            print_section("Validation Errors", '!')
            for i, error in enumerate(result.validation_errors, 1):
                print(f"  {i}. {error}")
        
        # Print the full result object for debugging
        if hasattr(result, '__dict__'):
            print_section("Debug: Full Result Object")
            print("Result object contains the following attributes:")
            for attr, value in result.__dict__.items():
                print(f"  • {attr}: {value if value is not None else 'None'}")
                
    except Exception as e:
        print_section("Error", '!')
        print(f"❌ Error parsing track data: {str(e)}")
        
        # For debugging, you can print the full traceback
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
    print("\n" + "=" * 50)
    print("Example completed. Check the output above for parsing results.")
    print("=" * 50)

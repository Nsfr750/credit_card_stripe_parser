.. _examples:

Examples
========

This page contains practical examples of how to use the Credit Card Stripe Parser.

.. contents:: Table of Contents
   :depth: 2
   :local:
   :backlinks: top

Basic Examples
-------------

Parsing a Full Track
~~~~~~~~~~~~~~~~~~~
.. code-block:: python

   from credit_card_stripe_parser import FullTrackParser
   
   # Initialize the parser
   parser = FullTrackParser()
   
   # Full track data (Track 1 and Track 2)
   track_data = (
       "%B5168755544412233^PKMMV/UNEMBOXXXX          ^1807111100000000000000111000000?"
       ";5168755544412233=18071111000011100000?"
   )
   
   # Parse the track data
   result = parser.parse(track_data)
   
   # Check if tracks were parsed successfully
   print(f"Track 1 Valid: {result.is_track_one_valid}")
   print(f"Track 2 Valid: {result.is_track_two_valid}")
   
   # Access Track 1 data
   if result.track_one:
       print("\nTrack 1 Data:")
       print(f"  • PAN: {result.track_one.pan}")
       print(f"  • Cardholder: {result.track_one.card_holder_name.strip()}")
       print(f"  • Expiration: {result.track_one.expiration_date} (YYMM)")
       print(f"  • Service Code: {result.track_one.service_code}")
   
   # Access Track 2 data
   if result.track_two:
       print("\nTrack 2 Data:")
       print(f"  • PAN: {result.track_two.pan}")
       print(f"  • Expiration: {result.track_two.expiration_date} (YYMM)")
       print(f"  • Service Code: {result.track_two.service_code}")

Parsing Individual Tracks
~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: python

   from credit_card_stripe_parser import FullTrackParser
   
   parser = FullTrackParser()
   
   # Parse only Track 1
   track1 = "%B5168755544412233^PKMMV/UNEMBOXXXX          ^1807111100000000000000111000000?"
   try:
       result1 = parser.parse_track_one(track1)
       print("Track 1 parsed successfully:")
       print(f"  • PAN: {result1.pan}")
       print(f"  • Cardholder: {result1.card_holder_name.strip()}")
   except Exception as e:
       print(f"Error parsing Track 1: {e}")
   
   # Parse only Track 2
   track2 = ";5168755544412233=18071111000011100000?"
   try:
       result2 = parser.parse_track_two(track2)
       print("\nTrack 2 parsed successfully:")
       print(f"  • PAN: {result2.pan}")
       print(f"  • Expiration: {result2.expiration_date} (YYMM)")
   except Exception as e:
       print(f"Error parsing Track 2: {e}")

Advanced Examples
----------------

Batch Processing Multiple Tracks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: python

   import glob
   from pathlib import Path
   from datetime import datetime
   from credit_card_stripe_parser import FullTrackParser
   
   def process_tracks(directory):
       """
       Process all track data files in a directory and extract card information.
       
       Args:
           directory (str): Path to the directory containing track data files
           
       Returns:
           list: List of dictionaries containing parsed card information
       """
       parser = FullTrackParser()
       results = []
       
       # Process all .txt and .dat files in the directory
       for file_path in glob.glob(f"{directory}/*.{'txt','dat'}"):
           with open(file_path, 'r', encoding='utf-8') as f:
               for line_num, line in enumerate(f, 1):
                   line = line.strip()
                   if not line or line.startswith('#'):
                       continue
                       
                   try:
                       result = parser.parse(line)
                       
                       # Create a result entry
                       entry = {
                           'source_file': Path(file_path).name,
                           'line_number': line_num,
                           'track1_valid': result.is_track_one_valid,
                           'track2_valid': result.is_track_two_valid,
                           'pan': None,
                           'expiry': None,
                           'cardholder': None,
                           'service_code': None,
                           'parse_timestamp': datetime.now().isoformat()
                       }
                       
                       # Add Track 1 data if available
                       if result.track_one:
                           entry.update({
                               'pan': result.track_one.pan,
                               'cardholder': result.track_one.card_holder_name.strip(),
                               'expiry': result.track_one.expiration_date,
                               'service_code': result.track_one.service_code
                           })
                       # Fall back to Track 2 data if Track 1 is not available
                       elif result.track_two:
                           entry.update({
                               'pan': result.track_two.pan,
                               'expiry': result.track_two.expiration_date,
                               'service_code': result.track_two.service_code
                           })
                       
                       results.append(entry)
                       
                   except Exception as e:
                       print(f"Error processing line {line_num} in {file_path}: {e}")
       
       return results

Validating and Cleaning Track Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: python

   from typing import Dict, Optional, Tuple
   from credit_card_stripe_parser import FullTrackParser
   from credit_card_stripe_parser.exceptions import (
       InvalidTrackDataException,
       InvalidTrackOneException,
       InvalidTrackTwoException
   )
   
   class TrackDataValidator:
       """Helper class for validating and cleaning track data."""
       
       def __init__(self):
           self.parser = FullTrackParser()
       
       def clean_and_validate(self, track_data: str) -> Dict:
           """
           Clean and validate track data.
           
           Args:
               track_data (str): Raw track data string
               
           Returns:
               Dict: Dictionary containing validation results and cleaned data
           """
           result = {
               'original_data': track_data,
               'is_valid': False,
               'track_type': None,
               'error': None,
               'warnings': [],
               'parsed_data': None
           }
           
           # Basic cleaning
           cleaned = track_data.strip()
           if not cleaned:
               result['error'] = 'Empty track data'
               return result
           
           # Try to determine track type
           if cleaned.startswith('%B') and '^' in cleaned:
               result['track_type'] = 'track1'
               parse_func = self.parser.parse_track_one
           elif cleaned.startswith(';') and '=' in cleaned:
               result['track_type'] = 'track2'
               parse_func = self.parser.parse_track_two
           else:
               result['error'] = 'Unknown track format'
               return result
           
           # Parse and validate
           try:
               parsed = parse_func(cleaned)
               result['is_valid'] = True
               result['parsed_data'] = {
                   'pan': parsed.pan,
                   'expiration_date': parsed.expiration_date,
                   'service_code': parsed.service_code
               }
               
               # Add track-specific data
               if hasattr(parsed, 'card_holder_name'):
                   result['parsed_data']['card_holder'] = parsed.card_holder_name.strip()
               
               # Check for common issues
               if hasattr(parsed, 'discretionary_data') and len(parsed.discretionary_data) > 10:
                   result['warnings'].append('Long discretionary data field')
                   
           except InvalidTrackOneException as e:
               result['error'] = f'Invalid Track 1 data: {str(e)}'
           except InvalidTrackTwoException as e:
               result['error'] = f'Invalid Track 2 data: {str(e)}'
           except InvalidTrackDataException as e:
               result['error'] = f'Invalid track data: {str(e)}'
           except Exception as e:
               result['error'] = f'Unexpected error: {str(e)}'
           
           return result
           
           # Additional validation
           if not result.primary_account_number.startswith(('4', '5', '6')):
               result['warnings'].append('Card number does not start with a major brand (4,5,6)')
               
           # Check expiration date
           current_year = datetime.now().year % 100
           current_month = datetime.now().month
           exp_year = int(result.expiration_date[2:4])
           exp_month = int(result.expiration_date[0:2])
           
           if exp_year < current_year or (exp_year == current_year and exp_month < current_month):
               result['warnings'].append('Card appears to be expired')
               
           return result

Graphical User Interface (GUI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The library includes a simple GUI for parsing track data. Here's how to use it:

.. code-block:: python

   import tkinter as tk
   from tkinter import ttk, scrolledtext, messagebox
   from credit_card_stripe_parser.gui import ParserGUI
   from credit_card_stripe_parser import FullTrackParser
   
   class CreditCardParserApp:
       """Main application window for the Credit Card Parser."""
       
       def __init__(self, root):
           self.root = root
           self.root.title("Credit Card Stripe Parser")
           self.parser = FullTrackParser()
           
           # Configure window
           self.root.minsize(600, 400)
           self.root.columnconfigure(0, weight=1)
           self.root.rowconfigure(1, weight=1)
           
           # Create GUI elements
           self.create_widgets()
       
       def create_widgets(self):
           """Create and arrange all GUI elements."""
           # Input frame
           input_frame = ttk.LabelFrame(self.root, text="Input Track Data", padding=10)
           input_frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=5)
           input_frame.columnconfigure(0, weight=1)
           
           # Track data input
           self.track_data = tk.Text(input_frame, height=3, wrap=tk.WORD)
           self.track_data.grid(row=0, column=0, sticky='nsew', pady=(0, 5))
           self.track_data.insert('1.0', 
               "%B5168755544412233^PKMMV/UNEMBOXXXX          ^1807111100000000000000111000000?;5168755544412233=18071111000011100000?")
           
           # Parse button
           parse_btn = ttk.Button(input_frame, text="Parse Track Data", command=self.parse_track_data)
           parse_btn.grid(row=1, column=0, pady=(0, 5))
           
           # Results notebook
           self.results_notebook = ttk.Notebook(self.root)
           self.results_notebook.grid(row=1, column=0, sticky='nsew', padx=10, pady=5)
           
           # Track 1 tab
           self.track1_frame = ttk.Frame(self.results_notebook, padding=10)
           self.track1_text = scrolledtext.ScrolledText(self.track1_frame, wrap=tk.WORD, state='disabled')
           self.track1_text.pack(expand=True, fill='both')
           self.results_notebook.add(self.track1_frame, text="Track 1")
           
           # Track 2 tab
           self.track2_frame = ttk.Frame(self.results_notebook, padding=10)
           self.track2_text = scrolledtext.ScrolledText(self.track2_frame, wrap=tk.WORD, state='disabled')
           self.track2_text.pack(expand=True, fill='both')
           self.results_notebook.add(self.track2_frame, text="Track 2")
           
           # Status bar
           self.status_var = tk.StringVar()
           self.status_bar = ttk.Label(self.root, textvariable=self.status_var, relief='sunken', anchor='w')
           self.status_bar.grid(row=2, column=0, sticky='ew', padx=10, pady=(0, 5))
           self.status_var.set("Ready")
       
       def parse_track_data(self):
           """Parse the track data and display results."""
           track_data = self.track_data.get('1.0', 'end-1c').strip()
           if not track_data:
               messagebox.showerror("Error", "Please enter track data to parse.")
               return
           
           try:
               result = self.parser.parse(track_data)
               self.display_results(result)
               self.status_var.set("Parsing completed successfully")
           except Exception as e:
               messagebox.showerror("Error", f"Error parsing track data: {str(e)}")
               self.status_var.set("Error parsing track data")
       
       def display_results(self, result):
           """Display the parsing results in the appropriate text widgets."""
           # Track 1
           self.track1_text.config(state='normal')
           self.track1_text.delete('1.0', tk.END)
           if result.track_one:
               track1 = result.track_one
               self.track1_text.insert('1.0', 
                   f"Status: {'✓ Valid' if result.is_track_one_valid else '✗ Invalid'}\n\n"
                   f"PAN: {track1.pan}\n"
                   f"Cardholder: {track1.card_holder_name.strip()}\n"
                   f"Expiration: {track1.expiration_date[:2]}/{track1.expiration_date[2:]} (MM/YY)\n"
                   f"Service Code: {track1.service_code}\n"
                   f"Format Code: {track1.format_code}\n"
                   f"Discretionary Data: {track1.discretionary_data}\n\n"
                   f"Raw Data: {track1.source_string}")
           else:
               self.track1_text.insert('1.0', "No Track 1 data found or parsed successfully.")
           self.track1_text.config(state='disabled')
           
           # Track 2
           self.track2_text.config(state='normal')
           self.track2_text.delete('1.0', tk.END)
           if result.track_two:
               track2 = result.track_two
               self.track2_text.insert('1.0',
                   f"Status: {'✓ Valid' if result.is_track_two_valid else '✗ Invalid'}\n\n"
                   f"PAN: {track2.pan}\n"
                   f"Expiration: {track2.expiration_date[:2]}/{track2.expiration_date[2:]} (MM/YY)\n"
                   f"Service Code: {track2.service_code}\n"
                   f"Discretionary Data: {track2.discretionary_data}\n\n"
                   f"Raw Data: {track2.source_string}")
           else:
               self.track2_text.insert('1.0', "No Track 2 data found or parsed successfully.")
           self.track2_text.config(state='disabled')
   
   if __name__ == "__main__":
       root = tk.Tk()
       app = CreditCardParserApp(root)
       root.mainloop()

   # To run the built-in GUI, you can also use:
   # from credit_card_stripe_parser.gui import main
   # main()

Integration Examples
-------------------

With Flask Web Application
~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: python

   from flask import Flask, request, jsonify
   from credit_card_stripe_parser import FullTrackParser
   
   app = Flask(__name__)
   parser = FullTrackParser()
   
   @app.route('/parse', methods=['POST'])
   def parse_track():
       data = request.get_json()
       track_data = data.get('track_data')
       
       if not track_data:
           return jsonify({"error": "No track data provided"}), 400
           
       try:
           result = parser.parse(track_data)
           return jsonify({
               "status": "success",
               "data": {
                   "card_number": result.primary_account_number,
                   "cardholder_name": result.cardholder_name,
                   "expiration_date": result.expiration_date,
                   "service_code": result.service_code
.. code-block:: python

   import pandas as pd
   import numpy as np
   from datetime import datetime
   from credit_card_stripe_parser import FullTrackParser
   from typing import Dict, Any, Optional
   
   def process_track_data(track_data: str) -> Dict[str, Any]:
       """
       Parse track data and return a dictionary of extracted fields.
       
       Args:
           track_data (str): Raw track data string
           
       Returns:
           Dict[str, Any]: Dictionary containing parsed fields
       """
       parser = FullTrackParser()
       result = {
           'pan': None,
           'cardholder': None,
           'expiry_date': None,
           'service_code': None,
           'track1_valid': False,
           'track2_valid': False,
           'parse_error': None,
           'parse_timestamp': datetime.now().isoformat()
       }
       
       try:
           parsed = parser.parse(track_data)
           result.update({
               'track1_valid': parsed.is_track_one_valid,
               'track2_valid': parsed.is_track_two_valid,
           })
           
           # Get data from Track 1 if available
           if parsed.track_one:
               track1 = parsed.track_one
               result.update({
                   'pan': track1.pan,
                   'cardholder': track1.card_holder_name.strip(),
                   'expiry_date': track1.expiration_date,
                   'service_code': track1.service_code
               })
           # Fall back to Track 2 if Track 1 is not available
           elif parsed.track_two:
               track2 = parsed.track_two
               result.update({
                   'pan': track2.pan,
                   'expiry_date': track2.expiration_date,
                   'service_code': track2.service_code
               })
               
       except Exception as e:
           result['parse_error'] = str(e)
       
       return result
   
   # Example: Process a CSV file with track data
   def process_csv(input_file: str, output_file: str) -> None:
       """
       Process a CSV file containing track data and save results to a new CSV.
       
       Args:
           input_file (str): Path to input CSV file
           output_file (str): Path to save processed results
       """
       # Read input CSV
       df = pd.read_csv(input_file)
       
       # Process track data
       print(f"Processing {len(df)} records...")
       results = df['track_data'].apply(
           lambda x: pd.Series(process_track_data(x))
       )
       
       # Combine with original data
       result_df = pd.concat([df, results], axis=1)
       
       # Save results
       result_df.to_csv(output_file, index=False)
       print(f"Results saved to {output_file}")
   
   # Example usage
   if __name__ == "__main__":
       # Create sample data
       data = {
           'transaction_id': [1, 2, 3],
           'terminal_id': ['T001', 'T002', 'T001'],
           'transaction_time': [
               '2023-01-15 10:30:00',
               '2023-01-15 11:15:00',
               '2023-01-15 12:45:00'
           ],
           'track_data': [
               "%B5168755544412233^PKMMV/UNEMBOXXXX          ^1807111100000000000000111000000?",
               ";5168755544412233=18071111000011100000?",
               "%B5555666677778884^SMITH/JOHN^2512121000000000000000000000000?"
           ]
       }
       
       # Create and process DataFrame
       df = pd.DataFrame(data)
       results = df['track_data'].apply(
           lambda x: pd.Series(process_track_data(x))
       )
       
       # Combine and display results
       result_df = pd.concat([df, results], axis=1)
       print("\nProcessed Results:")
       print(result_df[['transaction_id', 'pan', 'cardholder', 'expiry_date', 'track1_valid', 'track2_valid']])

Web API with FastAPI
~~~~~~~~~~~~~~~~~~~
.. code-block:: python

   from fastapi import FastAPI, HTTPException, Request
   from pydantic import BaseModel
   from typing import Dict, Optional
   from credit_card_stripe_parser import FullTrackParser
   from credit_card_stripe_parser.exceptions import InvalidTrackDataException
   
   app = FastAPI(
       title="Credit Card Parser API",
       description="API for parsing credit card track data",
       version="1.0.0"
   )
   
   parser = FullTrackParser()
   
   class TrackDataRequest(BaseModel):
       track_data: str
       
   class TrackDataResponse(BaseModel):
       success: bool
       data: Optional[Dict]
       error: Optional[str]
   
   @app.post("/api/parse", response_model=TrackDataResponse)
   async def parse_track_data(request: TrackDataRequest):
       """
       Parse credit card track data and return structured information.
       
       - **track_data**: Raw track data string (Track 1, Track 2, or both)
       """
       try:
           result = parser.parse(request.track_data)
           
           response_data = {
               'track1': {
                   'valid': result.is_track_one_valid,
                   'data': {
                       'pan': result.track_one.pan if result.track_one else None,
                       'cardholder': result.track_one.card_holder_name.strip() if result.track_one else None,
                       'expiry': result.track_one.expiration_date if result.track_one else None,
                       'service_code': result.track_one.service_code if result.track_one else None
                   } if result.track_one else None
               },
               'track2': {
                   'valid': result.is_track_two_valid,
                   'data': {
                       'pan': result.track_two.pan if result.track_two else None,
                       'expiry': result.track_two.expiration_date if result.track_two else None,
                       'service_code': result.track_two.service_code if result.track_two else None
                   } if result.track_two else None
               }
           }
           
           return TrackDataResponse(success=True, data=response_data)
           
       except InvalidTrackDataException as e:
           return TrackDataResponse(
               success=False,
               error=f"Invalid track data: {str(e)}"
           )
       except Exception as e:
           return TrackDataResponse(
               success=False,
               error=f"Error processing track data: {str(e)}"
           )
   
   @app.get("/health")
   async def health_check():
       """Health check endpoint"""
       return {"status": "ok", "version": "1.0.0"}
   
   if __name__ == "__main__":
       import uvicorn
       uvicorn.run(app, host="0.0.0.0", port=8000)

   # Example usage with curl:
   # curl -X POST "http://localhost:8000/api/parse" \
   #      -H "Content-Type: application/json" \
   #      -d '{"track_data":"%B5168755544412233^PKMMV/UNEMBOXXXX          ^1807111100000000000000111000000?;5168755544412233=18071111000011100000?"}'

Error Handling Examples
----------------------

Basic Error Handling
~~~~~~~~~~~~~~~~~~~
.. code-block:: python

   from credit_card_stripe_parser import FullTrackParser
   from credit_card_stripe_parser.exceptions import (
       InvalidTrackDataException,
       InvalidTrackOneException,
       InvalidTrackTwoException
   )
   
   def parse_track_safely(track_data: str) -> dict:
       """
       Parse track data with basic error handling.
       
       Args:
           track_data: Raw track data string to parse
           
       Returns:
           dict: Dictionary containing parsing result or error information
       """
       parser = FullTrackParser()
       
       try:
           # Basic input validation
           if not track_data or not isinstance(track_data, str):
               return {
                   'success': False,
                   'error': 'Invalid input: Track data must be a non-empty string',
                   'error_type': 'INVALID_INPUT'
               }
           
           # Attempt to parse
           result = parser.parse(track_data)
           
           # Return parsed data
           return {
               'success': True,
               'data': {
                   'pan': result.primary_account_number,
                   'cardholder': result.cardholder_name.strip() if result.cardholder_name else None,
                   'expiry': result.expiration_date,
                   'service_code': result.service_code,
                   'track1_valid': result.is_track_one_valid,
                   'track2_valid': result.is_track_two_valid
               }
           }
           
       except InvalidTrackOneException as e:
           return {
               'success': False,
               'error': f"Invalid Track 1 data: {str(e)}",
               'error_type': 'INVALID_TRACK1',
               'suggestion': 'Please check the Track 1 data format and try again.'
           }
       except InvalidTrackTwoException as e:
           return {
               'success': False,
               'error': f"Invalid Track 2 data: {str(e)}",
               'error_type': 'INVALID_TRACK2',
               'suggestion': 'Please check the Track 2 data format and try again.'
           }
       except InvalidTrackDataException as e:
           return {
               'success': False,
               'error': f"Invalid track data: {str(e)}",
               'error_type': 'INVALID_TRACK_DATA',
               'suggestion': 'Please verify the track data format and try again.'
           }
       except Exception as e:
           return {
               'success': False,
               'error': f"Unexpected error: {str(e)}",
               'error_type': 'UNEXPECTED_ERROR',
               'suggestion': 'Please contact support if the issue persists.'
           }

   # Example usage
   if __name__ == "__main__":
       # Test with valid track data
       valid_track = "%B5168755544412233^PKMMV/UNEMBOXXXX          ^1807111100000000000000111000000?"
       result = parse_track_safely(valid_track)
       if result['success']:
           print("Parsed successfully:", result['data'])
       else:
           print(f"Error: {result['error']}")
           print(f"Suggestion: {result.get('suggestion', 'No suggestion available')}")

Advanced Error Handling with Logging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: python

   import logging
   from datetime import datetime
   from typing import Dict, Any, Optional
   from credit_card_stripe_parser import FullTrackParser
   from credit_card_stripe_parser.exceptions import InvalidTrackDataException
   
   # Configure logging
   logging.basicConfig(
       level=logging.INFO,
       format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
       handlers=[
           logging.FileHandler('track_parser.log'),
           logging.StreamHandler()
       ]
   )
   logger = logging.getLogger('track_parser')
   
   class TrackDataProcessor:
       """Process track data with comprehensive error handling and logging."""
       
       def __init__(self):
           self.parser = FullTrackParser()
           self.logger = logging.getLogger('track_parser.processor')
       
       def process(self, track_data: str) -> Dict[str, Any]:
           """
           Process track data with error handling and logging.
           
           Args:
               track_data: Raw track data string to process
               
           Returns:
               dict: Processing results with status and data/error information
           """
           # Log the processing attempt
           self.logger.info(f"Processing track data (length: {len(track_data)})")
           
           # Input validation
           if not track_data or not isinstance(track_data, str):
               error_msg = "Invalid input: Track data must be a non-empty string"
               self.logger.error(error_msg)
               return self._format_error_response('INVALID_INPUT', error_msg)
           
           # Basic format validation
           if not any(sep in track_data for sep in ('%', ';', '?')):
               error_msg = "Invalid track data format: Missing track separators"
               self.logger.warning(f"{error_msg}. Sample: {track_data[:50]}...")
               return self._format_error_response('INVALID_FORMAT', error_msg)
           
           try:
               # Parse the track data
               result = self.parser.parse(track_data)
               
               # Log successful parsing
               self.logger.info(
                   f"Successfully parsed track data. PAN: {result.primary_account_number or 'N/A'}, "
                   f"Cardholder: {result.cardholder_name or 'N/A' if hasattr(result, 'cardholder_name') else 'N/A'}"
               )
               
               # Return successful response
               return {
                   'success': True,
                   'timestamp': datetime.utcnow().isoformat(),
                   'data': {
                       'pan': result.primary_account_number,
                       'cardholder': result.cardholder_name.strip() if hasattr(result, 'cardholder_name') and result.cardholder_name else None,
                       'expiry': result.expiration_date,
                       'service_code': result.service_code,
                       'track1_valid': result.is_track_one_valid,
                       'track2_valid': result.is_track_two_valid
                   }
               }
               
           except InvalidTrackDataException as e:
               error_msg = f"Invalid track data: {str(e)}"
               self.logger.warning(f"{error_msg}. Track data sample: {track_data[:50]}...")
               return self._format_error_response('INVALID_TRACK_DATA', error_msg)
               
           except Exception as e:
               error_msg = f"Unexpected error: {str(e)}"
               self.logger.error(error_msg, exc_info=True)
               return self._format_error_response('PROCESSING_ERROR', error_msg)
       
       def _format_error_response(self, error_type: str, message: str) -> Dict[str, Any]:
           """Format an error response with consistent structure."""
           return {
               'success': False,
               'error': {
                   'type': error_type,
                   'message': message,
                   'timestamp': datetime.utcnow().isoformat()
               }
           }
   
   # Example usage
   if __name__ == "__main__":
       # Create processor instance
       processor = TrackDataProcessor()
       
       # Test with valid track data
       valid_track = "%B5168755544412233^PKMMV/UNEMBOXXXX          ^1807111100000000000000111000000?"
       result = processor.process(valid_track)
       print("Processing result:", result)
       
       # Test with invalid track data
       invalid_track = "INVALID_TRACK_DATA"
       result = processor.process(invalid_track)
       print("Processing result:", result)

See Also
--------
- :ref:`quickstart` - Getting started guide
- :ref:`api-reference` - Complete API reference
- :ref:`gui` - GUI documentation

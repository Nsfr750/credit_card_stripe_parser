import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import Toplevel, scrolledtext
from typing import Optional
import webbrowser

from .full_track_parser import FullTrackParser
from .about import get_about_info, APP_NAME, VERSION, AUTHOR

class CreditCardParserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Credit Card Stripe Parser")
        self.root.geometry("800x600")
        
        # Configure style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Create menu bar
        self.create_menu()
        
        # Initialize parser
        self.parser = FullTrackParser()
        
        self.setup_ui()
    
    def setup_ui(self):
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Input section
        input_frame = ttk.LabelFrame(main_frame, text="Input Track Data", padding="10")
        input_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(input_frame, text="Enter Track 1:").pack(anchor=tk.W)
        self.track1_var = tk.StringVar()
        self.track1_entry = ttk.Entry(input_frame, textvariable=self.track1_var, width=80)
        self.track1_entry.pack(fill=tk.X, pady=2)
        
        ttk.Label(input_frame, text="Enter Track 2:").pack(anchor=tk.W, pady=(10, 0))
        self.track2_var = tk.StringVar()
        self.track2_entry = ttk.Entry(input_frame, textvariable=self.track2_var, width=80)
        self.track2_entry.pack(fill=tk.X, pady=2)
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(button_frame, text="Parse Tracks", command=self.parse_tracks).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Clear All", command=self.clear_fields).pack(side=tk.LEFT, padx=5)
        
        # Results section
        results_frame = ttk.LabelFrame(main_frame, text="Parsed Data", padding="10")
        results_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(results_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Track 1 tab
        self.track1_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.track1_tab, text="Track 1")
        self.setup_track_display(self.track1_tab, "track1")
        
        # Track 2 tab
        self.track2_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.track2_tab, text="Track 2")
        self.setup_track_display(self.track2_tab, "track2")
        
        # Combined tab
        self.combined_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.combined_tab, text="Combined")
        self.setup_combined_display()
    
    def setup_track_display(self, parent, track_name):
        # Create a frame with a Text widget and scrollbar
        frame = ttk.Frame(parent)
        frame.pack(fill=tk.BOTH, expand=True)
        
        text = tk.Text(frame, wrap=tk.WORD, height=10, font=('Courier', 10))
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=text.yview)
        text.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Store reference to the text widget
        if track_name == "track1":
            self.track1_text = text
        else:
            self.track2_text = text
    
    def setup_combined_display(self):
        # Create a frame with a Text widget and scrollbar for combined data
        frame = ttk.Frame(self.combined_tab)
        frame.pack(fill=tk.BOTH, expand=True)
        
        self.combined_text = tk.Text(frame, wrap=tk.WORD, height=15, font=('Courier', 10))
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.combined_text.yview)
        self.combined_text.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.combined_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    def parse_tracks(self):
        track1_data = self.track1_var.get().strip()
        track2_data = self.track2_var.get().strip()
        
        if not track1_data and not track2_data:
            messagebox.showerror("Error", "Please enter data for at least one track")
            return
        
        try:
            # Clear previous results
            for text_widget in [self.track1_text, self.track2_text, self.combined_text]:
                text_widget.delete(1.0, tk.END)
            
            # Parse tracks
            if track1_data:
                track1_result = self.parser.parse_track1(track1_data)
                self.display_parsed_data(self.track1_text, track1_result)
            
            if track2_data:
                track2_result = self.parser.parse_track2(track2_data)
                self.display_parsed_data(self.track2_text, track2_result)
            
            # Display combined results if both tracks are present
            if track1_data and track2_data:
                combined_result = self.parser.parse_full_track(track1_data, track2_data)
                self.display_combined_data(combined_result)
                
        except Exception as e:
            messagebox.showerror("Parsing Error", f"An error occurred during parsing: {str(e)}")
    
    def display_parsed_data(self, text_widget, data):
        if data is None:
            text_widget.insert(tk.END, "No data to display")
            return
        
        for field, value in data.__dict__.items():
            if not field.startswith('_'):  # Skip private attributes
                text_widget.insert(tk.END, f"{field.replace('_', ' ').title()}: {value}\n")
    
    def display_combined_data(self, data):
        if data is None:
            self.combined_text.insert(tk.END, "No combined data to display")
            return
        
        self.combined_text.insert(tk.END, "=== Combined Track Data ===\n\n")
        
        # Add track 1 data if available
        if data.track_one:
            self.combined_text.insert(tk.END, "--- Track 1 Data ---\n")
            self.display_parsed_data(self.combined_text, data.track_one)
            self.combined_text.insert(tk.END, "\n")
        
        # Add track 2 data if available
        if data.track_two:
            self.combined_text.insert(tk.END, "--- Track 2 Data ---\n")
            self.display_parsed_data(self.combined_text, data.track_two)
    
    def create_menu(self):
        """Create the application menu bar."""
        menubar = tk.Menu(self.root)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)
        
        self.root.config(menu=menubar)
    
    def show_about(self):
        """Display the About dialog."""
        about_window = Toplevel(self.root)
        about_window.title(f"About {APP_NAME}")
        about_window.geometry("600x500")
        about_window.resizable(False, False)
        about_window.transient(self.root)
        about_window.grab_set()
        
        # Center the about window
        window_width = 600
        window_height = 500
        screen_width = about_window.winfo_screenwidth()
        screen_height = about_window.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        about_window.geometry(f'{window_width}x{window_height}+{x}+{y}')
        
        # Header
        header_frame = ttk.Frame(about_window, padding="10")
        header_frame.pack(fill=tk.X)
        
        ttk.Label(
            header_frame,
            text=f"{APP_NAME} v{VERSION}",
            font=('Helvetica', 16, 'bold')
        ).pack(pady=(0, 5))
        
        ttk.Label(
            header_frame,
            text=f"by {AUTHOR}",
            font=('Helvetica', 10)
        ).pack()
        
        # Separator
        ttk.Separator(about_window, orient='horizontal').pack(fill='x', padx=10, pady=5)
        
        # Scrollable text area for the about information
        text_frame = ttk.Frame(about_window)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        text_area = scrolledtext.ScrolledText(
            text_frame,
            wrap=tk.WORD,
            width=70,
            height=20,
            font=('Consolas', 10),
            padx=10,
            pady=10
        )
        text_area.pack(fill=tk.BOTH, expand=True)
        
        # Add the about text
        about_text = get_about_info()
        text_area.insert(tk.INSERT, about_text)
        text_area.config(state=tk.DISABLED)  # Make it read-only
        
        # OK button
        button_frame = ttk.Frame(about_window)
        button_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(
            button_frame,
            text="OK",
            command=about_window.destroy
        ).pack(side=tk.RIGHT, padx=10)
        
        # Set focus to the window and wait for it to close
        about_window.focus_set()
        about_window.wait_window()
    
    def clear_fields(self):
        self.track1_var.set("")
        self.track2_var.set("")
        self.track1_text.delete(1.0, tk.END)
        self.track2_text.delete(1.0, tk.END)
        self.combined_text.delete(1.0, tk.END)

def main():
    root = tk.Tk()
    app = CreditCardParserApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

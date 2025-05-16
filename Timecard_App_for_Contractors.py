import tkinter as tk  #Here we are importing tkinter library for GUI
from tkinter import messagebox  #Imports the messagebox module from tkinter, which allows us to create pop-up dialogs like warnings, errors, or informational messages
from tkinter import ttk #Imports the ttk module, which provides themed widgets for GUI
import gspread #Imports gspread library, which is used to interact with Google Sheets through the Google Sheets API.
from oauth2client.service_account import ServiceAccountCredentials #used to authenticate with Google APIs (like Google Sheets) using a service account's credentials
from datetime import date #Imports the date class from the datetime module, which is used to retrieve today's date
from datetime import datetime #imports datetime class from datetime module to retrieve live time

# Linking Google Sheets
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"] #Allows us permission to access google drive and google sheets
CREDS = ServiceAccountCredentials.from_json_keyfile_name(
    "C:/Users/johnb/PycharmProjects/PythonProject1/Key Projects Folder/timecardkey.json", SCOPE) #uses service account credentials in a JSON file used to access google sheet service account via API
client = gspread.authorize(CREDS) #Uses the loaded credentials to authorize and create a gspread client, which interacts with the Google Sheets account.
sheet = client.open("timecard").sheet1 #identifies name of google sheet file to access, and then names sheet1 as "sheet"
daily = client.open("timecard").get_worksheet(1) #same as above, but names sheet2 as "daily" will be referred to later in code

#------------------------------------------------------------------------------------------------
# Landing Page
class TimecardApp: #defines a class 'TimecardApp'
    def __init__(self, root): #This sets up the class when it starts and takes in the main window of the app.
        self.root = root #This saves the main window so the rest of the app can use it.
        self.root.title("Level V Construction") #Sets the title of the main window to “Level V Construction”
        self.root.geometry("400x600") #Sets the size of the popup GUI window associated with this class
        self.root.resizable(False, False) #Does not allow user to resize GUI

        # Header Frame
        header_frame = tk.Frame(root, bg="#1A1A1A") #This creates a container (frame) inside the main window with a dark gray background.
        header_frame.pack(fill="x") #This adds the frame to the window and stretches it horizontally across the top.

        header_label = tk.Label(header_frame, text="Timecards",
            font=("Arial", 16, "bold"), bg="#1A1A1A", fg="white", pady=10) #This creates a text label that says "Timecards" with bold white text on a dark background and some padding at the top and bottom.
        header_label.pack() #.pack displays the label inside the frame by placing it in the layout.

        # Logo
        gif = tk.PhotoImage(file="C:/Users/johnb/PycharmProjects/PythonProject1/Key Projects Folder/logoimg_files/lvl5.gif") #This loads a .gif image from your computer so it can be shown in the app.
        tk.Label(header_frame, image=gif, bg="white").pack() #This creates and displays a label in the frame that shows the image with a white background.
        header_frame.image = gif  #This keeps a reference to the image so it doesn't disappear

        # Main Frame
        main_frame = tk.Frame(root, bg="#1A1A1A", padx=20, pady=20) #This creates a main section (frame) in the window with a dark background and padding around the inside.
        main_frame.pack(fill="both", expand=True) #This places the main frame in the window, letting it grow to fill all available space.

        welcome_label = tk.Label(main_frame, text="Select Your Position", font=("Arial", 12, "bold"), bg="#1A1A1A",
                                     fg="white", width=30) #This creates a white-text label that says "Select Your Position" with bold font, centered in a dark-colored area.
        welcome_label.pack(pady=10) #.pack displays the label and adds space (10 pixels) above and below it.

        pm_button = ttk.Button(main_frame, text="Project Manager", command=self.launch_pm) #creates a button within main frame that reads 'Project Manager' and has a command that launches pm page (later connected to new class)
        pm_button.pack(pady=10, ipadx=10) #.pack displays the button and adds padding above and below

        carpenter_button = ttk.Button(main_frame, text="Carpenter", command=self.launch_carpenter) #creates a button within main frame that reads 'Carpenter' and has a command that launches carpenter page (later connected to new class)
        carpenter_button.pack(pady=10, ipadx=10) #.pack displays the button and adds padding above and below

        laborer_button = ttk.Button(main_frame, text="Laborer", command=self.launch_laborer)#creates a button within main frame that reads 'Laborer' and has a command that launches laborer page (later connected to new class)
        laborer_button.pack(pady=10, ipadx=10) #.pack displays the button and adds padding above and below

        exit_button = ttk.Button(main_frame, text="Exit", command=root.quit) #creates an 'Exit' button that destroys the current GUI
        exit_button.pack(pady=10, ipadx=10) #.pack displays the button and adds padding above and below

    def launch_carpenter(self): #def comand for launching new window (carpenter)
        self.root.destroy()  # Close landing page
        CarpenterPage()      # Open carpenter page in new window

    def launch_laborer(self): #def command for launching new window (laborer)
        self.root.destroy()  #closes current page.
        LaborerPage()     #opens the laborer's page

    def launch_pm(self): #def command for launching new window (proj manager)
        self.root.destroy() #closes current page
        ProjectManagerPage() #opens project manager page in new window
#---------------------------------------------------------------------------------------------
# Project Manager Portal
class ProjectManagerPage: #defines a class 'ProjectManagerPage'
    def __init__(self):
        self.root = tk.Tk() #Initializes the main window for the GUI application.
        self.root.title("Level V Construction") #Sets the title of the main window to “Level V Construction”
        self.root.geometry("600x800") #Sets the size of the popup GUI window associated with this class (600p wide and 800p tall)
        self.root.resizable(False, False) #Does not allow user to resize

        # Header Frame
        header_frame = tk.Frame(self.root, bg="#1A1A1A") #This creates a dark-colored top section (frame) inside the main window
        header_frame.pack(fill="x") #.pack adds the frame to the top of the window and stretches it across the full width

        header_label = tk.Label(header_frame, text="Daily Summary Report",
             font=("Arial", 16, "bold"), bg="#1A1A1A", fg="white", pady=5) #This creates a bold white label that says "Daily Summary Report" with a little vertical padding, placed inside the dark header
        header_label.pack() #.pack displays the header label on page

        # Main Frame
        main_frame = tk.Frame(self.root, pady=5) #This creates the main section of the window with some vertical padding around it.
        main_frame.pack(fill="both", expand=True) #.pack displays the frame to the page

        # Fields
        tk.Label(main_frame, text="Job Name", font=("Arial", 10)).pack(pady=5) #creates Label to be displayed above entry box that prompts user
        self.job_name_entry = tk.Entry(main_frame, width=15) #creates an entry box within main frame
        self.job_name_entry.pack(pady=5) #.pack displays entry box to the page

        tk.Label(main_frame, text="Project Manager", font=("Arial", 10)).pack(pady=5) #creates Label to be displayed above entry box that prompts user
        self.name_entry = tk.Entry(main_frame, width=30) #creates an entry box within main frame
        self.name_entry.pack(pady=5) #.pack displays entry box to the page

        tk.Label(main_frame, text="Weather", font=("Arial", 10)).pack(pady=5) #creates Label to be displayed above entry box that prompts user
        self.weather_entry = tk.Entry(main_frame, width=30) #creates an entry box within main frame
        self.weather_entry.pack(pady=5) #.pack displays entry box to the page

        tk.Label(main_frame, text="Subcontractors", font=("Arial", 10)).pack(pady=5) #creates Label to be displayed above entry box that prompts user
        self.subs_entry = tk.Text(main_frame, width=30, height=4) #creates a Text entry box within main frame with a height of four lines, this is so contractor can write several lines of info
        self.subs_entry.pack(pady=5) #.pack displays entry box to the page with padding on both axis

        tk.Label(main_frame, text="Delays:", font=("Arial", 10)).pack(pady=5) #creates Label to be displayed above entry box that prompts user
        self.delays_entry = tk.Text(main_frame, width=50, height=2) #creates a Text entry box within main frame with a height of two lines, this is so contractor can write multiple lines of info
        self.delays_entry.pack(pady=5, padx=20) #.pack displays entry box to the page with padding on both axis

        tk.Label(main_frame, text="Summary of Work Completed", font=("Arial", 10)).pack(pady=5) #creates Label to be displayed above entry box that prompts user
        self.summary_entry = tk.Text(main_frame, width=50, height=5) #creates a Text entry box within main frame with a height of four lines, this is so contractor can write several lines of info
        self.summary_entry.pack(pady=5, padx=20) #.pack displays entry box to the page with padding on both axis

        submit_button = tk.Button(main_frame, text="Submit Daily Report", font=("Arial", 12, "bold"), #creates button, customizes text preferences
          bg="#228B22", fg="white", activebackground="#1A1A1A", activeforeground="white", #customizes color preferences
            command=self.export_to_sheet) #links command to the button, 'export data to spreadsheet'
        submit_button.pack(pady=5) #.pack displays the submit button with a little padding above and below

    def export_to_sheet(self):
            # Get values from form
            pm = self.name_entry.get().strip() #retrieves string from name box and saves as 'pm'
            today_date = date.today().strftime("%m/%d/%Y") #retrieves date in month:day:year format and saves as 'date'
            subs = self.subs_entry.get("1.0", tk.END).strip() ##retrieves string from sub entry box and saves as 'subs'
            job = self.job_name_entry.get().strip() #retrieves string from job name box and saves as 'job'
            delays = self.delays_entry.get("1.0", tk.END).strip() #retrieves string from delays box and saves as 'delays'
            weather = self.weather_entry.get().strip() #retrieves string from weather box and saves as 'weather'
            summary = self.summary_entry.get("1.0", tk.END).strip() #retrieves string from summary box and saves as 'summary'

            # Build the row for Google Sheets
            row = [today_date, job, pm, weather, subs, delays, summary] #establishes the order of the columns to input the variables into the spreadsheet

            # Validate that all fields are filled
            if all(row): #checks that none of the fields are empty before submitting
                try:
                    daily.append_row(row) #attempts to add the collected data as a new row in the google sheet
                    messagebox.showinfo("Success", "Daily Report Submitted!") #Shows a success pop-up if submission is successful
                    self.clear_form() #Clears the form fields after successful submission with def functino
                except Exception as e:
                    messagebox.showerror("Error", f"Submission failed:\n{e}") #Displays an error message if the submission fails
            else:
                messagebox.showwarning("Missing Info", "Please complete all fields before submitting.") #Warns user if any required field is left empty
                self.root.mainloop() #Keeps the form window open after warning to allow the user to complete it

    def clear_form(self): #Clears all input fields in the form to reset for a new entry
        self.name_entry.delete(0, tk.END) #clears all written entry for this name box
        self.weather_entry.delete(0, tk.END) #clears all written entry for this  weather entry box
        self.subs_entry.delete(0, tk.END) #clears all written entry for this subcontractor entry box
        self.summary_entry.delete(0, tk.END) #clears all written entry for this summary box
        self.job_name_entry.delete(0, tk.END) #clears all written entry for this job name box
        self.delays_entry.delete("1.0", tk.END) #clears all written entry for this delays incurred box
#-------------------------------------------------------------------------------------------------------
# Carpenter Timecard Screen Fillout
class CarpenterPage: #creating a Class for the carpenter page
    def __init__(self):
        self.root = tk.Tk() #Initializes the main window for the GUI application.
        self.root.title("Level V Construction") #Sets the title of the main window to “Level V Construction”
        self.root.geometry("400x600") #Sets the size of the popup GUI window associated with this class 400pixels wide by 600pixels tall
        self.root.resizable(False, False) #Does not allow user to resize

        # Header Frame
        header_frame = tk.Frame(self.root, bg="#1A1A1A") #This makes a header area at the top of the window with a dark background color.
        header_frame.pack(fill="x") #.pack displays header frame, filling space from left to right

        header_label = tk.Label(header_frame, text="Carpenter Report",
                font=("Arial", 16, "bold"), bg="#1A1A1A", fg="white", pady=10) #creates a header label for the top of the page, customized
        header_label.pack() #.pack displays header label to page

        # Main Frame
        main_frame = tk.Frame(self.root, pady=10) #This creates the main section of the window with some vertical padding around it.
        main_frame.pack(fill="both", expand=True) #.pack displays the main frame, which fills space vertically and horizontally

        # Fields
        tk.Label(main_frame, text="Name", font=("Arial", 10)).pack(pady=5) #creates Label to be displayed above entry box that prompts user
        self.name_entry = tk.Entry(main_frame, width=30) #creates an entry box within main frame
        self.name_entry.pack(pady=5) #.pack displays entry box for user with padding above and below

        tk.Label(main_frame, text="Total Hours", font=("Arial", 10)).pack(pady=5) #creates Label to be displayed above entry box that prompts user
        self.hoursworked_entry = tk.Entry(main_frame, width=15) #creates an entry box within main frame
        self.hoursworked_entry.pack(pady=5) #.pack displays entry box for user with padding above and below

        tk.Label(main_frame, text="Job Name", font=("Arial", 10)).pack(pady=5) #creates Label to be displayed above entry box that prompts user
        self.job_name_entry = tk.Entry(main_frame, width=15) #creates an entry box within main frame
        self.job_name_entry.pack(pady=10) #.pack displays entry box for user with padding above and below

        tk.Label(main_frame, text="List Tasks and Work Today:", font=("Arial", 10)).pack(pady=15) #creates Label to be displayed above entry box that prompts user
        self.tasks_performed_entry = tk.Text(main_frame, width=50, height=8) #creates a Text entry box within main frame, has multiple lines in case the input is long
        self.tasks_performed_entry.pack(pady=10, padx=20) #.pack displays the entry box with both vertical and horizontal padding

        submit_button = tk.Button(main_frame, text="Submit Timecard", font=("Arial", 12, "bold"), #customized text preferences
            bg="#228B22", fg="white", activebackground="#1A1A1A", activeforeground="white", #color preferences for font and background
            command=self.export_to_sheet) #links command to the button, 'export data to spreadsheet'
        submit_button.pack(pady=10) #.pack displays the submit button with a little padding above and below

    def export_to_sheet(self):
            # get values from form
            name = self.name_entry.get().strip() #Retrieves and trims any extra spaces from the name input field, and assigns to variable name
            timestamp = datetime.now().strftime(" %I:%M %p")  #Gets the current time formatted as hours:minutes with AM/PM., and assigns to variable name
            today_date = date.today().strftime("%m/%d/%Y") #Gets current date formatted as month:day:year, and assigns to variable name
            hours = self.hoursworked_entry.get().strip() #retrieves the string entered into the hours worked box, and assigns to variable name
            job = self.job_name_entry.get().strip() ##retrieves the string entered into the job name entry box, and assigns to variable name
            tasks = self.tasks_performed_entry.get("1.0", tk.END).strip() #retrieves text from entry box, and stores as a variable

            # Build the row for Google Sheets
            row = [today_date, timestamp, name, "Carpenter", job, tasks, hours] #establishes order that variables are to be inputted into the next available row in the spreadsheet

            # Validate that all fields are filled
            if all(row): #checks that none of the fields are empty before submitting
                try:
                    sheet.append_row(row) #attempts to add the collected data as a new row in the google sheet
                    messagebox.showinfo("Success", "Timecard submitted successfully!") #Shows a success pop-up if submission is successful
                    self.clear_form() #Clears the form fields after successful submission with def functino
                except Exception as e:
                    messagebox.showerror("Error", f"Submission failed:\n{e}") #Displays an error message if the submission fails
            else:
                messagebox.showwarning("Missing Info", "Please complete all fields before submitting.") #Warns user if any required field is left empty
                self.root.mainloop() #Keeps the form window open after warning to allow the user to complete it

    def clear_form(self): #Clears all input fields in the form to reset for a new entry
        self.name_entry.delete(0, tk.END) #clears any name entered in this box
        self.hoursworked_entry.delete(0, tk.END) #clears hours worked in this box
        self.job_name_entry.delete(0, tk.END) #clears name of job entered in this box
        self.tasks_performed_entry.delete("1.0", tk.END) #removes all tasks performed from this entry box
#-----------------------------------------------------------------------------------------------------
# Laborer Timecard Fillout Page
class LaborerPage:
    def __init__(self):
        self.root = tk.Tk() #Initializes the main window for the GUI application.
        self.root.title("Level V Construction") #Sets the title of the main window to “Level V Construction”
        self.root.geometry("400x600") #establishes size of GUI popup
        self.root.resizable(False, False) #Does not allow user to resize

        # Header Frame
        header_frame = tk.Frame(self.root, bg="#1A1A1A") #This creates a top frame (section) inside the main window with a dark gray background color.
        header_frame.pack(fill="x") #.pack displays the frame and fills space from left to right

        header_label = tk.Label(header_frame, text="Labor Summary Report",
            font=("Arial", 16, "bold"), bg="#1A1A1A", fg="white", pady=10) #creates a header label for the top of the page, customized
        header_label.pack() #.pack displays header label to page

        # Main Frame
        main_frame = tk.Frame(self.root, pady=20) #This creates the main section of the window with some vertical padding around it.
        main_frame.pack(fill="both", expand=True) #.pack displays frame, expands to fill all open space

        # Fields
        tk.Label(main_frame, text="Name", font=("Arial", 10)).pack(pady=5) #creates Label to be displayed above entry box that prompts user
        self.name_entry = tk.Entry(main_frame, width=30)  #creates entry box in main frame
        self.name_entry.pack(pady=5) #.pack displays entry box for user with padding above and below

        tk.Label(main_frame, text="Total Hours", font=("Arial", 10)).pack(pady=5) #creates Label to be displayed above entry box that prompts user
        self.hoursworked_entry = tk.Entry(main_frame, width=15) #creates entry box in main frame
        self.hoursworked_entry.pack(pady=5) #.pack displays entry box for user with padding above and below

        tk.Label(main_frame, text="Job Name", font=("Arial", 10)).pack(pady=5) #creates Label to be displayed above entry box that prompts user
        self.job_name_entry = tk.Entry(main_frame, width=15) #creates entry box in main frame
        self.job_name_entry.pack(pady=10) #.pack displays entry box for user with padding above and below

        tk.Label(main_frame, text="Labor Performed:", font=("Arial", 10)).pack(pady=15) #creates Label to be displayed above entry box that prompts user
        self.tasks_performed_entry = tk.Text(main_frame, width=50, height=8) #creates a Text entry box within main frame, has multiple lines in case the input is long
        self.tasks_performed_entry.pack(pady=10, padx=20) #.pack displays the entry box with both vertical and horizontal padding

        submit_button = tk.Button(main_frame, text="Submit Timecard", font=("Arial", 12, "bold"), #customized text preferences
            bg="#228B22", fg="white", activebackground="#1A1A1A", activeforeground="white", #olor preferences on font, and backgbround
            command=self.export_to_sheet) #links command to the button, 'export data to spreadsheet'
        submit_button.pack(pady=10) #.pack displays the submit button with a little padding above and below

    def export_to_sheet(self):
            # Get values from form
            name = self.name_entry.get().strip() #retrieves the string entered into the name entry box, and assigns to designated column in spreadsheet
            timestamp = datetime.now().strftime(" %I:%M %p")  #Gets the current time formatted as hours:minutes with AM/PM.
            today_date = date.today().strftime("%m/%d/%Y") #Gets the current date formatted as month:day:year
            hours = self.hoursworked_entry.get().strip() #retrieves the string entered into the hours worked entry box, and assigns to designated column in spreadsheet
            job = self.job_name_entry.get().strip() #retrieves the string entered into the job name entry box, and assigns to designated column in spreadsheet
            tasks = self.tasks_performed_entry.get("1.0", tk.END).strip() #retrieves the string entered into the tasks performed entry box, and assigns to designated column in spreadsheet
            # Build the row for Google Sheets
            row = [today_date, timestamp, name, "Laborer", job, tasks, hours] #This is the order that each label will be entered into the specific spreadsheet. Includes variables defined right above
            # Validate that all fields are filled
            if all(row): #checks that none of the fields are empty before submitting
                try:
                    sheet.append_row(row) #attempts to add the collected data as a new row in the google sheet
                    messagebox.showinfo("Success", "Timecard submitted successfully!") #Shows a success pop-up if submission is successful
                    self.clear_form() #Clears the form fields after successful submission with def functino
                except Exception as e:
                    messagebox.showerror("Error", f"Submission failed:\n{e}") #Displays an error message if the submission fails
            else:
                messagebox.showwarning("Missing Info", "Please complete all fields before submitting.") #Warns user if any required field is left empty
                self.root.mainloop() #Keeps the form window open after warning to allow the user to complete it

    def clear_form(self): #Clears all input fields in the form to reset for a new entry
        self.name_entry.delete(0, tk.END) #Deletes any text entered in the name field
        self.hoursworked_entry.delete(0, tk.END) #Clears the total hours input field
        self.job_name_entry.delete(0, tk.END) #Clears the job name input field
        self.tasks_performed_entry.delete("1.0", tk.END) #Removes all text from the tasks performed text area
#-------------------------------------------------------------------------------------------------
if __name__ == "__main__": #This checks if the script is being run directly (not imported).
    root = tk.Tk() # initializes the main tkinter window for the landing page GUI
    app = TimecardApp(root) #Creates an instance of the TimecardApp class using the main window.
    root.mainloop() #Starts the Tkinter event loop, which keeps the GUI running.

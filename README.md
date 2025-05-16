# timecard-app-for-contractors
This is a timecard app that contractors can use. Specifically, their laborers, carpenters, and project managers can submit daily timecards, which then records the input to a spreadsheet for further integration. 

The app integrates with Google sheets using oAuth and gspread. It then connects a JSON key file so that python can have permission to make changes to the spreadsheet. 

Each GUI allows a user to make contributions to the entry boxes, where those entries are then exported to the correct spreadsheet in Google Sheets. 

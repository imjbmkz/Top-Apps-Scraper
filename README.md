# Top-Apps-Scraper

1. Make sure you have Python 3 and the required packages installed (`requests`, `beautifulsoup4`, `google-auth`, and `google-api-python-client`).
2. Create a JSON configuration file named `config.json` in the same directory as the script. The file should contain the following information:
   - `DESTINATION_SHEET_ID`: The ID of the Google Sheet where you want to write the links. You can find this in the URL of the Google Sheet.
   - `DESTINATION_RANGE`: The range of cells where you want to write the links in the format `Sheet1!A1:B`. By default, the links will be written to the first column of the first sheet in the Google Sheet.
   - `SERVICE_ACCOUNT_FILE`: The path to the service account JSON file that contains the Google Sheets API credentials.
3. Run the script by executing the following command in the terminal: `python3 script.py`
4. The script will scrape the links from `https://topapps.ai/` and write them to the specified Google Sheet.
5. The script will output the number of records that have been added to the Google Sheet.

Note: Make sure you have enabled the Google Sheets API and created a service account with the necessary permissions to write to the Google Sheet. For more information on how to do this, please refer to the Google Sheets API documentation.
